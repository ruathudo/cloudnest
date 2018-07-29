PATH = '/api/v1/users'


def test_get_user(client, first_user):
    # test get user success
    rv = client.get(PATH + '/1')
    assert rv.status_code == 200
    assert first_user.first_name.encode() in rv.data
    assert first_user.last_name.encode() in rv.data
    assert first_user.username.encode() in rv.data
    assert first_user.email.encode() in rv.data

    # test user not found
    rv = client.get(PATH + '/0')
    assert rv.status_code == 404
    assert b'User Not Found' in rv.data


def test_create_user(client, db):
    # test create user success
    data = dict(
        first_name='Test',
        last_name='User',
        username='testing',
        password='abc123',
        email='testing@example.com'
    )

    rv = client.post(PATH + '/', json=data)
    assert rv.status_code == 200
    assert rv.is_json
    assert b'token' in rv.data
    assert b'user' in rv.data

    # test duplicated user
    rv = client.post(PATH + '/', json=data)
    assert rv.status_code == 409
