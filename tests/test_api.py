
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_user():
    response = requests.get(
        f"{BASE_URL}/users/1",
        timeout=10
    )

    assert response.status_code == 200

    user = response.json()

    assert isinstance(user, dict)
    assert {"id", "name", "email"}.issubset(user.keys())

    assert user["id"] == 1
    assert user["name"] == "Leanne Graham"
    assert user["email"] == "Sincere@april.biz"


def test_create_user():
    payload = {
        "name": "Test User",
        "username": "testuser",
        "email": "testuser@example.com"
    }

    response = requests.post(
        f"{BASE_URL}/users",
        json=payload,
        timeout=10
    )

    assert response.status_code == 201

    user = response.json()

    assert isinstance(user, dict)
    assert {"id", "name", "username", "email"}.issubset(
        user.keys()
    )

    assert user["name"] == payload["name"]
    assert user["username"] == payload["username"]
    assert user["email"] == payload["email"]


def test_update_user():
    payload = {
        "id": 1,
        "name": "Updated User",
        "username": "updateduser",
        "email": "updated@example.com"
    }

    response = requests.put(
        f"{BASE_URL}/users/1",
        json=payload,
        timeout=10
    )

    assert response.status_code == 200

    user = response.json()

    assert isinstance(user, dict)
    assert {"id", "name", "username", "email"}.issubset(
        user.keys()
    )

    assert user["id"] == 1
    assert user["name"] == payload["name"]
    assert user["username"] == payload["username"]
    assert user["email"] == payload["email"]
