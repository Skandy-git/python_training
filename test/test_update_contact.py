from model.contact import Contact


def test_update_contact(app):
    if app.contact.count() == 0:
        app.contact.contact(Contact(firstname="Nikita", middlename="qqqqq", lastname="Skvortsov"))
    old_groups = app.group.get_group_list()
    app.contact.update_contact(Contact(firstname="TEST", middlename="TEST", lastname="TEST", nickname="TEST",
                                       mobile="TEST", work="TEST", fax="3TEST", email="TEST",
                                       email2="TEST", homepage="TEST", byear="2000"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)