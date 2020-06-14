from model.group import Group

def test_Update_Group(app):
    app.session.Login(login="admin", password="secret")
    app.group.Update_Group(Group(name="456", header="456", footer="456"))
    app.session.Logout()