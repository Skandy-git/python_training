# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.session.Login(login="admin", password="secret")
    app.contact.Contact(Contact(firstname="Nikita", middlename="qqqqq", lastname="Skvortsov", nickname="sssss",
                                mobile="11111111111", work="2222222222", fax="3333333", email="test1@mail.ru",
                                email2="test2@gmail.com", homepage="qweasd.ru", byear="1990"))
    app.contact.Return_to_contact_page()
    app.session.Logout()