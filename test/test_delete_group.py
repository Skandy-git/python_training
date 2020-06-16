def test_Delete_Group(app):
    app.session.login(login="admin", password="secret")
    app.group.delete_group()
    app.session.logout()