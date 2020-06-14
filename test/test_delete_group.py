def test_Delete_Group(app):
    app.session.Login(login="admin", password="secret")
    app.group.Delete_group()
    app.session.Logout()