import pytest

from utils.data_loader import load_payload

pytestmark = pytest.mark.api


@pytest.mark.smoke
def test_get_an_existing_post(api):
    response = api.get("/posts/1")

    assert response.status == 200
    assert response.json()["id"] == 1


@pytest.mark.regression
def test_create_a_new_post(api):
    response = api.post("/posts", data={"title": "My first post", "body": "Simple body text", "userId": 1})

    assert response.status == 201
    assert response.json()["title"] == "My first post"


@pytest.mark.regression
def test_request_a_post_that_does_not_exist(api):
    response = api.get("/posts/99999")

    assert response.status == 404


@pytest.mark.regression
def test_create_a_post_using_a_payload_file(api):
    payload = load_payload("create_post")
    response = api.post("/posts", data=payload)

    assert response.status == 201
    assert response.json()["title"] == payload["title"]
    assert response.json()["body"] == payload["body"]


@pytest.mark.regression
def test_update_a_post_using_a_payload_file(api):
    payload = load_payload("update_post")
    response = api.put("/posts/1", data=payload)

    assert response.status == 200
    assert response.json()["id"] == 1
    assert response.json()["title"] == payload["title"]
