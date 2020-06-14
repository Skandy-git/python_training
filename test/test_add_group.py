# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.Login(login="admin", password="secret")
    app.group.Create_group(Group(name="123", header="123", footer="123"))
    app.session.Logout()


def test_add_empty_group(app):
    app.session.Login(login="admin", password="secret")
    app.group.Create_group(Group(name="", header="", footer=""))
    app.session.Logout()


