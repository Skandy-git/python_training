# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login(login="admin", password="secret")
    app.group.create_group(Group(name="123", header="123", footer="123"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(login="admin", password="secret")
    app.group.create_group(Group(name="", header="", footer=""))
    app.session.logout()


