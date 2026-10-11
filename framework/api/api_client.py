from playwright.sync_api import APIRequestContext, APIResponse


class ApiClient:
    """Thin wrapper over Playwright's APIRequestContext (same tool as UI)."""

    def __init__(self, request_context: APIRequestContext):
        self.request = request_context

    def get_post(self, post_id: int) -> APIResponse:
        return self.request.get(f"/posts/{post_id}")

    def create_post(self, title: str, body: str, user_id: int = 1) -> APIResponse:
        return self.request.post(
            "/posts", data={"title": title, "body": body, "userId": user_id}
        )

    def create_post_with_payload(self, payload: dict) -> APIResponse:
        return self.request.post("/posts", data=payload)

    def update_post(self, post_id: int, payload: dict) -> APIResponse:
        return self.request.put(f"/posts/{post_id}", data=payload)
