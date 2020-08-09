from model.contact import Contact
import random
import allure


def test_update_contact(app, db):
    with allure.step("Сheck for not empty list of contacts"):
        if len(db.get_contact_list()) == 0:
            app.contact.contact(Contact(firstname="Nikita", middlename="qqqqq", lastname="Skvortsov"))
    with allure.step("Given a contact list"):
        old_contacts = db.get_contact_list()
    with allure.step("When I modify a random contact from the list"):
        contact_id = random.choice(old_contacts)
        contact = Contact(firstname="TEST", middlename="TEST", lastname="TEST", nickname="TEST",
                                           mobile="TEST", work="TEST", fax="3TEST", email="TEST",
                                           email2="TEST", homepage="TEST", byear="2000")
        app.contact.update_contact_by_id(contact_id.id, contact)
    with allure.step("Then the new contact list is equal to the old contact list with the modified contact"):
        new_contacts = db.get_contact_list()
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)