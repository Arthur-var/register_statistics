def test_create_task_success(test_client):
    # Сreate user
    test_client.post("/register", json={"username": "taskuser"})

    response = test_client.post(
        "/tasks?user_id=1",
        json={"title": "Test task"}
    )
    #check
    assert response.status_code == 200
    assert response.json()["message"] == "Task created"


def test_get_tasks(test_client):
    response = test_client.get("/tasks?user_id=1")
    assert response.status_code == 200
    assert isinstance(response.json(), list)