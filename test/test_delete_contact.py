def test_delete_contact(app):
    app.session.Login(login="admin", password="secret")
    app.contact.Delete_Contact()
    app.session.Logout()