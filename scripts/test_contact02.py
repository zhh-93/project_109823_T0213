import time
import pytest

from base.base_data import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestConcat:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    @pytest.mark.parametrize("args",analyze_file("contact_data.yaml","test_contact"))
    def test_contact(self,args):
        name = args["name"]
        phone = args["phone"]
        self.page.Concat_Page().click_new_contacter()
        self.page.New_Contacts_Page().input_name(name)
        self.page.New_Contacts_Page().input_phone(phone)
        self.page.Person_Info_Page().click_back()
        time.sleep(3)
        assert name == self.page.Person_Info_Page().get_title()