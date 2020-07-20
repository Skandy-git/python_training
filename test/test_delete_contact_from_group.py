from model.group import Group
from model.contact import Contact
import random


def test_delete_contact_from_group(app, orm):
    if len(orm.get_group_list()) == 0:
        app.group.create_group(Group(name="123", header="123", footer="123"))
    if len(orm.get_contact_list()) == 0:
        app.contact.contact(Contact(firstname="Nikita", middlename="qqqqq", lastname="Skvortsov"))
    contact = random.choice(orm.get_contact_list())
    group = random.choice(orm.get_group_list())
    if Contact(id=contact.id) in orm.get_contacts_not_in_group(Group(id=group.id)):
        app.contact.add_to_group(group.id, contact.id)
        assert Contact(id=contact.id) in orm.get_contacts_in_group(Group(id=group.id))
    app.contact.delete_contact_from_group(group.id, contact.id)
    assert Contact(id=contact.id) in orm.get_contacts_not_in_group(Group(id=group.id))