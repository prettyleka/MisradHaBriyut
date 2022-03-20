from selenium.webdriver.common.by import By


class LPLocators:
    def __init__(self):
        self.upperMenuBtn = lambda text: (By.XPATH, f"//ul[@id='officeMenu']//a[.='{text}']/parent::li")
