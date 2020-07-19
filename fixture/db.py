import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, user, password, db):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.connection = pymysql.connect(host=host,
                             user=user,
                             password=password,
                             db=db,
                             autocommit=True
                                          )

    def destroy(self):
        self.connection.close()

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, middlename, lastname, nickname, home, mobile, work, phone2 from addressbook where deprecated = '0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, middlename, lastname, nickname, home, mobile, work, phone2) = row
                list.append(Contact(id=str(id), firstname=firstname, middlename=middlename,
                                  lastname=lastname, nickname=nickname, homephone=home,
                                    mobilephone=mobile, workphone=work, secondaryphone=phone2))
        finally:
            cursor.close()
        return list