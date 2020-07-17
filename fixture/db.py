import pymysql.cursors
from model.group import Group


class DbFixture:

    def __init__(self, host, user, password, db):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.connection = pymysql.connect(host=host,
                             user=user,
                             password=password,
                             db=db)

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