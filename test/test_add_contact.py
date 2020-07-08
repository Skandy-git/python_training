# -*- coding: utf-8 -*-
import pytest
import random
import string
from model.contact import Contact


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdatas = [Contact(firstname="", middlename="", lastname="")] + [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10), lastname=random_string("lastname", 10),
            nickname=random_string("nickname", 10), email=random_string("email", 10), email2=random_string("email2", 10)
            )
    for i in range(5)
]


@pytest.mark.parametrize("contact", testdatas, ids=[repr(x) for x in testdatas])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.contact(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)