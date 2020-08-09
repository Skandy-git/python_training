from model.group import Group
import random
import allure


def test_delete_group(app, db, check_ui):
    with allure.step("Сheck for not empty list of groups"):
        if len(db.get_group_list()) == 0:
            app.group.create_group(Group(name="123", header="123", footer="123"))
    with allure.step("Given a group list"):
        old_groups = db.get_group_list()
    with allure.step("When I delete a random group from the list"):
        group = random.choice(old_groups)
        app.group.delete_group_by_id(group.id)
    with allure.step("Then the new group list is equal to the old group list with the deleted group"):
        new_groups = db.get_group_list()
        assert len(old_groups) - 1 == len(new_groups)
        old_groups.remove(group)
        assert old_groups == new_groups