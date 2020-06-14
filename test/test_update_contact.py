from model.contact import Contact


def test_update_contact(app):
    app.session.Login(login="admin", password="secret")
    app.contact.Update_Contact(Contact(firstname="TEST", middlename="TEST", lastname="TEST", nickname="TEST",
                                mobile="TEST", work="TEST", fax="3TEST", email="TEST",
                                email2="TEST", homepage="TEST", byear="2000"))
    app.session.Logout()