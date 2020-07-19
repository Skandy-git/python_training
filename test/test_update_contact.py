from model.contact import Contact
import random


def test_update_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.contact(Contact(firstname="Nikita", middlename="qqqqq", lastname="Skvortsov"))
    old_contacts = db.get_contact_list()
    contact_id = random.choice(old_contacts)
    contact = Contact(firstname="TEST", middlename="TEST", lastname="TEST", nickname="TEST",
                                       mobile="TEST", work="TEST", fax="3TEST", email="TEST",
                                       email2="TEST", homepage="TEST", byear="2000")
    #for i in old_contacts:
    app.contact.update_contact_by_id(contact_id.id, contact)
    new_contacts = db.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert new_contacts == app.contact.get_group_list()