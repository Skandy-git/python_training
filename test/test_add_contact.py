# -*- coding: utf-8 -*-
from model.contact import Contact
import allure


def test_add_contact(app, db, data_contacts):
    contact = data_contacts
    with allure.step("Given a contact list"):
        old_contacts = db.get_contact_list()
    with allure.step("When I add a contact %s to the list" % contact):
        app.contact.contact(contact)
    with allure.step("Then the new contact list is equal to the old contact list with the added contact"):
        new_contact = db.get_contact_list()
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
