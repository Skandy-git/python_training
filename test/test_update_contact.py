from model.contact import Contact


def test_update_contact(app):
    if app.contact.count() == 0:
        app.contact.contact(Contact(firstname="Nikita", middlename="qqqqq", lastname="Skvortsov"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="TEST", middlename="TEST", lastname="TEST", nickname="TEST",
                                       mobile="TEST", work="TEST", fax="3TEST", email="TEST",
                                       email2="TEST", homepage="TEST", byear="2000")
    contact.id = old_contacts[0].id
    app.contact.update_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)