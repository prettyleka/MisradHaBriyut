from Infra.SeleniumInfra import SeleniumInfra
from Pages.LandingPage.LPLocstors import LPLocators

class LandingActions:
    def __init__(self, seleniumInfra:SeleniumInfra):
        self.seleniumInfra = seleniumInfra
        self.locators = LPLocators()

    def clickOnUperMenuBtn(self, text):
        self.seleniumInfra.clickButton(*self.locators.upperMenuBtn(text))