from model.group import Group

class GroupHelper:
    def __init__(self, app):
         self.app = app

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def create_group(self, group):
        wd = self.app.wd
        self.open_group_pages()
        # Init group creation
        wd.find_element_by_name("new").click()
        # Fill group form
        self.fill_group_form(group)
        # Submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def open_group_pages(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_link_text("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def delete_group(self):
        wd = self.app.wd
        self.open_group_pages()
        self.select_first_group()
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def update_group(self, group):
        wd = self.app.wd
        self.open_group_pages()
        self.select_first_group()
        wd.find_element_by_name("edit").click()
        self.fill_group_form(group)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        self.open_group_pages()
        return len(wd.find_elements_by_name("selected[]"))

    def get_group_list(self):
        wd = self.app.wd
        self.open_group_pages()
        group_list = []
        for element in wd.find_elements_by_css_selector("span.group"):
            text = element.text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            group_list.append(Group(name=text, id=id))
        return group_list