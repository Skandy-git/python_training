from model.contact import Contact


def test_update_contact(app):
    app.session.login(login="admin", password="secret")
    app.contact.update_contact(Contact(firstname="TEST", middlename="TEST", lastname="TEST", nickname="TEST",
                                       mobile="TEST", work="TEST", fax="3TEST", email="TEST",
                                       email2="TEST", homepage="TEST", byear="2000"))
    app.session.logout()