from model.group import Group
import random


def test_update_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create_group(Group(name="123", header="123", footer="123"))
    old_groups = db.get_group_list()
    group_id = random.choice(old_groups)
    group = Group(name="456")
    app.group.update_group_by_id(group_id.id, group)
    new_groups = db.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert new_groups == app.group.get_group_list()