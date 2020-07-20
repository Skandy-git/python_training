from sys import maxsize


class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, mobile=None, work=None, fax=None, email=None, email2=None, email3=None, homepage=None,
                       byear=None, homephone=None, mobilephone=None, workphone=None, secondaryphone=None, id=None , all_phones_from_homepage=None,
                 all_emails_from_homepage=None, address=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.byear = byear
        self.id = id
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.all_phones_from_homepage = all_phones_from_homepage
        self.all_emails_from_homepage = all_emails_from_homepage
        self.address = address

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s:%s:%s" % (self.id, self.firstname, self.lastname, self.middlename, self.nickname, self.email, self.email2, self.address)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == self.firstname and self.lastname == self.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize