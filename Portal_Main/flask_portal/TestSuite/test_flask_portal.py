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


