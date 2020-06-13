class SessionHelper:
    def __init__(self, app):
        self.app = app

    def Login(self, login, password):
        wd = self.app.wd
        self.app.Open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(login)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def Logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()