import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class ConcatPage(BaseAction):
    new_contacter = By.ID, "com.android.contacts:id/floating_action_button"

    @allure.step(title="点击新建联系人")
    def click_new_contacter(self):
        self.click(self.new_contacter)
