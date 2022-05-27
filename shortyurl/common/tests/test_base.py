def test_admin_page_login_view_returns_200(client):
    assert client.get("/admin/login/").status_code == 200
