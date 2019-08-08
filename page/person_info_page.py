import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class PersonInfoPage(BaseAction):
    title = By.ID, "com.android.contacts:id/large_title"

    @allure.step(title="获取页面标题")
    def get_title(self):
        return self.find_element(self.title).text
