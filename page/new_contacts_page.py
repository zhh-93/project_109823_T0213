import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class NewContactsPage(BaseAction):
    contact_name = By.XPATH, "//*[contains(@text,'姓名')]"
    contact_phone = By.XPATH, "//*[contains(@text,'电话')]"

    @allure.step(title="输入姓名")
    def input_name(self, name):
        allure.attach("姓名", name, allure.attach_type.TEXT)
        self.input(self.contact_name, name)
        allure.attach("截图：", self.driver.get_screenshot_as_png(), allure.attach_type.PNG)

    @allure.step(title="输入电话")
    def input_phone(self, phone):
        # allure.attach("姓名", phone, allure.attach_type.TEXT)
        self.input(self.contact_phone, phone)
        allure.attach("截图：", self.driver.get_screenshot_as_png(), allure.attach_type.PNG)
