from model.contact import Contact
import random


def test_delete_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.contact(Contact(firstname="Test", middlename="qqqqq", lastname="Test"))
    old_contact = db.get_contact_list()
    contact = random.choice(old_contact)
    app.contact.delete_contact_by_id(contact.id)
    new_contact = db.get_contact_list()
    assert len(old_contact) - 1 == len(new_contact)
    old_contact.remove(contact)
    assert old_contact == new_contact
    if check_ui:
        assert new_contact == app.contact.get_contact_list()