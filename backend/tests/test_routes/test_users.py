import json


# clientは、conftest.pyで定義しているものが使える
def test_create_user(client):
    data = {"username": "testusername", "email": "abc@test.com", "password": "1234556"}
    response = client.post("/users/create-user", json.dumps(data))
    assert response.status_code == 200
    assert response.json()["email"] == "abc@test.com"
    assert response.json()["is_active"] == True
        