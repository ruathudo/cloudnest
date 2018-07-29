def test_get_user(client, first_user):
    # test get user success
    response = client.get('/api/v1/users/1')
    assert response.status_code == 200
    assert first_user.first_name.encode() in response.data
    assert first_user.last_name.encode() in response.data
    assert first_user.username.encode() in response.data
    assert first_user.email.encode() in response.data

    # test user not found
    response = client.get('/api/v1/users/2')
    assert response.status_code == 404
    assert b'User Not Found' in response.data
