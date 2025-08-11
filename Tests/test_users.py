import requests

def test_get_users(base_url):
    response = requests.get(f"{base_url}/users")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_create_user(base_url):
    payload = {
        "name": "John Doe",
        "username": "johndoe",
        "email": "john@example.com"
    }
    response = requests.post(f"{base_url}/users", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == payload["name"]
    assert data["username"] == payload["username"]

def test_update_user(base_url):
    payload = {"name": "Jane Doe"}
    response = requests.put(f"{base_url}/users/1", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Jane Doe"

def test_delete_user(base_url):
    response = requests.delete(f"{base_url}/users/1")
    assert response.status_code == 200
