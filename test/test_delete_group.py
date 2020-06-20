from model.group import Group


def test_Delete_Group(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name="123", header="123", footer="123"))
    app.group.delete_group()
