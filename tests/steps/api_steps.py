from pytest_bdd import when, then, parsers

from framework.utils.data_loader import load_payload


@when(parsers.parse("the client requests post number {post_id:d}"), target_fixture="response")
def get_post(api_client, post_id):
    return api_client.get_post(post_id)


@when(parsers.parse('the client creates a post with title "{title}"'), target_fixture="response")
def create_post(api_client, title):
    return api_client.create_post(title=title, body="Simple body text")


@when(parsers.parse('the client creates a post using the "{payload_name}" payload'), target_fixture="response")
def create_post_from_payload(api_client, payload_name):
    return api_client.create_post_with_payload(load_payload(payload_name))


@when(parsers.parse('the client updates post {post_id:d} using the "{payload_name}" payload'), target_fixture="response")
def update_post(api_client, post_id, payload_name):
    return api_client.update_post(post_id, load_payload(payload_name))


@then(parsers.parse("the response status is {status:d}"))
def check_status(response, status):
    assert response.status == status


@then(parsers.parse("the post id in the response is {post_id:d}"))
def check_post_id(response, post_id):
    assert response.json()["id"] == post_id


@then(parsers.parse('the response title is "{title}"'))
def check_title(response, title):
    assert response.json()["title"] == title


@then(parsers.parse('the response body is "{body}"'))
def check_body(response, body):
    assert response.json()["body"] == body
