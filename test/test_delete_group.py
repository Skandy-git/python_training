from model.group import Group


def test_Delete_Group(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name="123", header="123", footer="123"))
    old_groups = app.group.get_group_list()
    app.group.delete_group()
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0:1] = []
    assert old_groups == new_groups
