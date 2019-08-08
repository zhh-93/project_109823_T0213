from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature, timeout=10, poll=1):
        """
        根据特征，找元素
        :param feature: 特征
        :param timeout: 超时时间
        :param poll: 频率
        :return: 元素
        """
        feature_by, feature_value = feature
        element = WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(feature_by, feature_value))
        return element

    def find_elements(self, feature, timeout=10, poll=1):
        """
        根据特征，找多个符合条件的元素
        :param feature: 特征
        :param timeout: 超时时间
        :param poll: 频率
        :return: 元素
        """
        feature_by, feature_value = feature
        element = WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(feature_by, feature_value))
        return element

    def click(self, feature):
        self.find_element(feature).click()

    def input(self, feature, content):
        self.find_element(feature).send_keys(content)

    def clear(self, feature):
        self.find_element(feature).clear()

    def click_back(self):
        self.driver.press_keycode(4)

