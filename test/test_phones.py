import re
from random import randrange
import pytest


@pytest.mark.skip()
def test_phones_on_homepage(app):
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_homepage = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_homepage.all_phones_from_homepage == merge_phones_like_on_homepage(contact_from_edit_page)


@pytest.mark.skip()
def test_phones_on_contact_view_page(app):
    contact_from_view = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view.homephone == contact_from_edit_page.homephone
    assert contact_from_view.workphone == contact_from_edit_page.workphone
    assert contact_from_view.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view.secondaryphone == contact_from_edit_page.secondaryphone


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.workphone, contact.mobilephone,
                                        contact.secondaryphone]))))
