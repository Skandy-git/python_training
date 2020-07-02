from model.group import Group
from random import randrange


def test_update_group_name(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name="123", header="123", footer="123"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="456")
    group.id = old_groups[index].id
    app.group.update_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_update_group_footer(app):
#    if app.group.count() == 0:
#        app.group.create_group(Group(name="123", header="123", footer="123"))
#    app.group.update_group(Group(footer="456"))
