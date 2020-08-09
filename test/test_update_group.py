from model.group import Group
import random
import allure


def test_update_group_name(app, db):
    with allure.step("Сheck for not empty list of groups"):
        if len(db.get_group_list()) == 0:
            app.group.create_group(Group(name="123", header="123", footer="123"))
    with allure.step("Given a group list"):
        old_groups = db.get_group_list()
    with allure.step("When I modify a random group from the list"):
        group_id = random.choice(old_groups)
        group = Group(name="456")
        app.group.update_group_by_id(group_id.id, group)
    with allure.step("Then the new group list is equal to the old group list with the modified group"):
        new_groups = db.get_group_list()
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)