import re
from model.contact import Contact


def test_db_matches_ui_for_contact(app, db):
    contact_from_homepage = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contact_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    i = 0
    for contact_home_page in contact_from_homepage:
        contact_db = contact_from_db[i]
        assert contact_home_page.address == contact_db.address
        assert contact_home_page.firstname == contact_db.firstname
        assert contact_home_page.lastname == contact_db.lastname
        assert contact_home_page.all_phones_from_homepage == merge_phones_like_on_homepage(contact_db)
        assert contact_home_page.all_emails_from_homepage == merge_emails_like_on_homepage(contact_db)
        i += 1


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))


def merge_emails_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))
