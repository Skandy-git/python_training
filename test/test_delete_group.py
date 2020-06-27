from model.group import Group


def test_Delete_Group(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name="123", header="123", footer="123"))
    old_groups = app.group.get_group_list()
    app.group.delete_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
