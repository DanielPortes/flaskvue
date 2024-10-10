import json


def test_get_whiskies(client, init_database):
    response = client.get('/whiskies')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data['whiskies']) == 1
    assert data['whiskies'][0]['name'] == "Test Whisky"


def test_create_whisky(client):
    new_whisky = {
        "name": "New Whisky",
        "type": "Scotch",
        "proof": 90
    }
    response = client.post('/whiskies', json=new_whisky)
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['whisky']['name'] == "New Whisky"


def test_update_whisky(client, init_database):
    response = client.get('/whiskies')
    whisky_id = json.loads(response.data)['whiskies'][0]['id']

    updated_whisky = {
        "name": "Updated Whisky",
        "type": "Irish",
        "proof": 85
    }
    response = client.put(f'/whiskies/{whisky_id}', json=updated_whisky)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['whisky']['name'] == "Updated Whisky"


def test_delete_whisky(client, init_database):
    response = client.get('/whiskies')
    whisky_id = json.loads(response.data)['whiskies'][0]['id']

    response = client.delete(f'/whiskies/{whisky_id}')
    assert response.status_code == 200

    response = client.get('/whiskies')
    data = json.loads(response.data)
    assert len(data['whiskies']) == 0