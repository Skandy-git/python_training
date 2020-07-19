# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app, db, data_contacts, check_ui):
    contact = data_contacts
    old_contacts = db.get_contact_list()
    app.contact.contact(contact)
    new_contact = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
    if check_ui:
        assert new_contact == app.contact.get_contact_list()