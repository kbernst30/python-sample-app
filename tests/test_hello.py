def test_index(client):
    response = client.get('/')
    assert b"Hello World" in response.data
