import os
import tempfile
import pytest
from .. import flask_portal

@pytest.fixture
def client(request):
    db_fd, flask_portal.app.config['DATABASE'] = tempfile.mkstemp()
    flask_portal.app.config['TESTING'] = True
    client = flask_portal.app.test_client()
    with flask_portal.app.app_context():
        flask_portal.init_db()
        client.post("/register_new", data=dict(
            username= flask_portal.app.config['USERNAME'],
            password= flask_portal.app.config['PASSWORD']
        ), follow_redirects=True)

    def teardown():
        os.close(db_fd)
        os.unlink(flask_portal.app.config['DATABASE'])
    request.addfinalizer(teardown)

    return client

def login(client, username, password):
    return client.post('/login', data=dict(
        username=username,
        password=password
    ), follow_redirects=True)

def logout(client):
    return client.get('/logout', follow_redirects=True)


def test_empty_db(client):
    """Start with a blank database."""
    rv = client.get('/')
    assert b'No apps here so far' in rv.data


def test_login_logout(client):
    """Make sure login and logout works"""
    rv = login(client, flask_portal.app.config['USERNAME'],
               flask_portal.app.config['PASSWORD'])
    assert b'You were logged in' in rv.data
    rv = logout(client)
    assert b'You were logged out' in rv.data
    rv = login(client, flask_portal.app.config['USERNAME'] + 'x',
                flask_portal.app.config['PASSWORD'])
    assert b'Invalid username' in rv.data
    rv = login(client, flask_portal.app.config['USERNAME'],
                flask_portal.app.config['PASSWORD'] + 'x')
    assert b'Invalid password' in rv.data

def test_add_app(client):
    login(client, flask_portal.app.config['USERNAME'],
               flask_portal.app.config['PASSWORD'])
    rv = client.post('/add', data=dict(
        title='<Hello>',
        link='http://google.com/'
    ), follow_redirects=True)

    assert b'No apps here so far' not in rv.data
    assert b'&lt;Hello&gt;' in rv.data
    assert b'http://google.com/' in rv.data

def test_subscribe_to_app(client):
    login(client, flask_portal.app.config['USERNAME'],
               flask_portal.app.config['PASSWORD'])
    client.post('/add', data=dict(
        title='<Hello>',
        link='http://google.com/'
    ), follow_redirects=True)
    rv = client.post('/add', data=dict(
        title='<Hello>',
        link='http://google.com/',
        submit='Keep me posted!',
        app_id='1',
        user_id='1'
    ), follow_redirects=True)

    assert b'No apps here so far' not in rv.data
    assert b'&lt;Hello&gt;' in rv.data
    assert b'http://google.com/' in rv.data

def test_unsub_from_app(client):
    login(client, flask_portal.app.config['USERNAME'],
               flask_portal.app.config['PASSWORD'])
    client.post('/add', data=dict(
        title='<Hello>',
        link='http://google.com/'
    ), follow_redirects=True)
    rv = client.post('/add', data=dict(
        title='<Hello>',
        link='http://google.com/',
        submit='DO NOT WANT',
        app_id='1',
        user_id='1'
    ), follow_redirects=True)

    assert b'No apps here so far' not in rv.data
    assert b'&lt;Hello&gt;' in rv.data
    assert b'http://google.com/' in rv.data

def test_add_app_unauth(client):
    rv = client.post('/add', data=dict(
        title='<Hello>',
        link='http://google.com/'
    ), follow_redirects=True)

    assert b'401 Unauthorized' in rv.data

def test_register_get(client):
    rv = client.get("/register_new")
    assert b'Register a new account!' in rv.data

def test_register_user(client):
    rv = client.post("/register_new",data=dict(
        username='new_test_user',
        password='new_test_password'
    ), follow_redirects=True)

    assert b'New user was successfully added' in rv.data
