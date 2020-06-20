from model.group import Group

def test_update_group_name(app):
    app.group.update_group(Group(name="456"))


def test_update_group_footer(app):
    app.group.update_group(Group(footer="456"))
