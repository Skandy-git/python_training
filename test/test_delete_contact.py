def test_delete_contact(app):
    app.session.login(login="admin", password="secret")
    app.contact.delete_contact()
    app.session.logout()