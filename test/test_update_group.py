from model.group import Group

def test_Update_Group(app):
    app.session.login(login="admin", password="secret")
    app.group.update_group(Group(name="456", header="456", footer="456"))
    app.session.logout()