from selenium.webdriver.common.by import By


class FocusOnLocators:
    def __init__(self):
        self.fromMidnightData = (By.XPATH, "//bdc-generic-kpi//div[2]/h4")
        self.yesterdayData = (By.XPATH, "//bdc-generic-kpi//div[1]/h4")
