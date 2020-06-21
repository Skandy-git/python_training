class ContactHelper:
    def __init__(self, app):
         self.app = app

    def return_to_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def open_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def contact(self, contact):
        wd = self.app.wd
        # Init contact creation
        wd.find_element_by_link_text("add new").click()
        # Fill contact form
        self.fill_contact_form(contact)
        # Submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_contact_page()

    def delete_contact(self):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def update_contact(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # Fill contact form
        self.fill_contact_form(contact)
        # Submit contact creation
        wd.find_element_by_name("update").click()
        self.return_to_contact_page()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_value("byear", contact.byear)
        wd.find_element_by_name("bday").click()
        wd.find_element_by_xpath("//option[@value='1']").click()
        wd.find_element_by_name("bmonth").click()
        wd.find_element_by_xpath("//option[@value='January']").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_name("selected[]"))