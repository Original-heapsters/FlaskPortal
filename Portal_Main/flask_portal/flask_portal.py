import os
from sqlite3 import dbapi2 as sqlite3
from flask.ext.bcrypt import Bcrypt
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__)
bcrypt = Bcrypt(app)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flask_portal.db'),
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='test_user',
    PASSWORD='test_password'
))

app.config.from_envvar('FLASK_PORTAL_SETTINGS', silent=True)


def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def init_db():
    """Initializes the database."""
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


@app.route('/')
def show_apps():
    #init_db()
    db = get_db()
    cur = db.execute('select title, link from apps order by id desc')
    apps = cur.fetchall()

    return render_template('show_apps.html', apps=apps)

@app.route('/add', methods=['POST'])
def add_app():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('insert into apps (title, link) values (?, ?)',
               [request.form['title'], request.form['link']])
    db.commit()
    flash('New app was successfully posted')
    return redirect(url_for('show_apps'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user_login, error = get_credentials(request.form['username'],request.form['password'])
        if user_login and error is None:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_apps'))
    return render_template('login.html', error=error)

@app.route('/register_new', methods=['GET', 'POST'])
def register_new():
    error = None
    if request.method == 'POST':
        add_user(request.form['username'] , request.form['password'] )
        return redirect(url_for('login'))
    return render_template('register_account.html', error=error)

def get_credentials(uName, uPassword):
    error = None
    found_user = None
    db = get_db()
    creds = db.execute('select username,password from users where username=?',[uName])

    found_user = creds.fetchone()

    if found_user:
        print(bcrypt.check_password_hash(found_user["password"], uPassword))
        if bcrypt.check_password_hash(found_user["password"], uPassword) is True:
            return found_user, None
        else:
            error = "Invalid password"
            return None, error
    else:
        error = "Invalid username"
        return None, error

def add_user(uName, uPassword):
    db = get_db()
    pwHash = bcrypt.generate_password_hash(uPassword)
    db.execute('insert into users (username, password) values (?, ?)',
               [uName, pwHash])
    db.commit()
    flash('New user was successfully added')



@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_apps'))

if __name__ == "__main__":
   app.run(debug=True, host='0.0.0.0', port=4000)
