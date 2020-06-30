# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Nikita", middlename="qqqqq", lastname="Skvortsov", nickname="sssss",
                                mobile="11111111111", work="2222222222", fax="3333333", email="test1@mail.ru",
                                email2="test2@gmail.com", homepage="qweasd.ru", byear="1990")
    app.contact.contact(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contact)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


#def test_add_pers_info(app):
#    app.contact.contact(Contact(firstname="Nikita", middlename="qqqqq", lastname="Skvortsov"))
