from model.group import Group

def test_update_group_name(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name="123", header="123", footer="123"))
    old_groups = app.group.get_group_list()
    group = Group(name="456")
    group.id = old_groups[0].id
    app.group.update_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_update_group_footer(app):
#    if app.group.count() == 0:
#        app.group.create_group(Group(name="123", header="123", footer="123"))
#    app.group.update_group(Group(footer="456"))
