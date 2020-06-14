class GroupHelper:
    def __init__(self, app):
         self.app = app

    def Return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()


    def Create_group(self, group):
        wd = self.app.wd
        self.Open_group_Pages()
        # Init group creation
        wd.find_element_by_name("new").click()
        # Fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # Submit group creation
        wd.find_element_by_name("submit").click()
        self.Return_to_groups_page()


    def Open_group_Pages(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def Delete_group(self):
        wd = self.app.wd
        self.Open_group_Pages()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("delete").click()
        self.Return_to_groups_page()

    def Update_Group(self, group):
        wd = self.app.wd
        self.Open_group_Pages()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("edit").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("update").click()
        self.Return_to_groups_page()