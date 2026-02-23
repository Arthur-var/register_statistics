def test_register_success(test_client):
    response = test_client.post(
        "/register",
        json={"username": "testuser"}
    )
    assert response.status_code == 200 # check
    assert response.json()["message"] == "User created"


def test_register_without_username(test_client):
    response = test_client.post("/register", json={})
    assert response.status_code == 422