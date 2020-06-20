from model.group import Group

def test_update_group_name(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name="123", header="123", footer="123"))
    app.group.update_group(Group(name="456"))


def test_update_group_footer(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name="123", header="123", footer="123"))
    app.group.update_group(Group(footer="456"))
