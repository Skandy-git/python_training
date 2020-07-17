import pymysql.cursors

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