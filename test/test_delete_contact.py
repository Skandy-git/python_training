from model.contact import Contact
import random
import allure


def test_delete_contact(app, db):
    with allure.step("Сheck for not empty list of contacts"):
        if len(db.get_contact_list()) == 0:
            app.contact.contact(Contact(firstname="Test", middlename="qqqqq", lastname="Test"))
    with allure.step("Given a contact list"):
        old_contact = db.get_contact_list()
    with allure.step("When I delete a random contact from the list"):
        contact = random.choice(old_contact)
        app.contact.delete_contact_by_id(contact.id)
    with allure.step("Then the new contact list is equal to the old contact list with the deleted contact"):
        new_contact = db.get_contact_list()
        assert len(old_contact) - 1 == len(new_contact)
        old_contact.remove(contact)
        assert old_contact == new_contact