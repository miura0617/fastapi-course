import json


# clientは、conftest.pyで定義しているものが使える
def test_create_job(client, normal_user_token_headers):
    # ジョブ作成
    data = {
        "title": "title123",
        "company": "company123",
        "company_url": "https://www.fdj.com",
        "location": "Japan",
        "description": "This is emergency!!!",
        "date_posted": "2022-07-28"
    }
    response = client.post("/jobs/create-job", json.dumps(data), headers=normal_user_token_headers)
    assert response.status_code == 200
    assert response.json()["title"] == "title123"
    assert response.json()["company"] == "company123"
    assert response.json()["location"] == "Japan"
    assert response.json()["description"] == "This is emergency!!!"


# We need to modify each and every unit test in which we are making a post/delete request. Since we are not restricting get requests. We do not need headers for get requests.

def test_retreive_job_by_id(client, normal_user_token_headers):
    # ジョブ作成
    data = {
        "title": "title123",
        "company": "company123",
        "company_url": "https://www.fdj.com",
        "location": "Japan",
        "description": "This is emergency!!!",
        "date_posted": "2022-07-28"
    }
    client.post("/jobs/create-job", json.dumps(data), headers=normal_user_token_headers)

    response = client.get("/jobs/get/1")
    assert response.status_code == 200
    assert response.json()["title"] == "title123"