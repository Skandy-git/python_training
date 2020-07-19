from fixture.orm import ORMFixture
from model.group import Group

db = ORMFixture(host="127.0.0.1", user="root", db="addressbook", password="")

#def test_contact_list(app, db):
#    ui_list = app.contact.get_contact_list()
#    #def clean(contact):
#     #   return Contact(id=contact.id, name=contact.name.strip())
#    db_list = db.get_contact_list()
#  # db_list = map(clean, db.get_group_list())
#    assert sorted(ui_list, key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)


try:
    l = db.get_contacts_not_in_group(Group(id="79"))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass #db.destroy