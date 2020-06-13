# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.Open_home_page()
    app.Login(login="admin", password="secret")
    app.Create_contact(Contact(firstname="Nikita", middlename="qqqqq", lastname="Skvortsov", nickname="sssss",
                                        mobile="11111111111", work="2222222222", fax="3333333", email="test1@mail.ru",
                                        email2="test2@gmail.com", homepage="qweasd.ru", byear="1990"))
    app.Return_to_contact_page()
    app.Logout()