from model.contact import Contact


def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.contact(Contact(firstname="Nikita", middlename="qqqqq", lastname="Skvortsov"))
    old_contact = app.contact.get_contact_list()
    app.contact.delete_contact()
    assert len(old_contact) - 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact[0:1] = []
    assert old_contact == new_contact