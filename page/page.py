from page.contact_page import ConcatPage
from page.new_contacts_page import NewContactsPage
from page.person_info_page import PersonInfoPage


class Page:
    def __init__(self,driver):
        self.driver = driver

    def Concat_Page(self):
        self.contact_page = ConcatPage(self.driver)
        return self.contact_page

    def New_Contacts_Page(self):
        self.new_contacts_page = NewContactsPage(self.driver)
        return self.new_contacts_page

    def Person_Info_Page(self):
        self.person_info_page = PersonInfoPage(self.driver)
        return self.person_info_page