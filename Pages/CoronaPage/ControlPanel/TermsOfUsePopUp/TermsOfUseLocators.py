from selenium.webdriver.common.by import By


class TermsOfUseLocators:
    def __init__(self):
        self.popUpTermsOfUse = (By.XPATH, "//*[@class='cdk-global-scrollblock nb-global-scrollblock']")
        self.btnClosePopUp = (By.XPATH, "//div[@class='btn-x-close']/button")
        self.newPopUp=(By.XPATH, "//div[@class='cdk-overlay-container']")
