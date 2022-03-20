from Infra.SeleniumInfra import SeleniumInfra
from Pages.CoronaPage.ControlPanel.TermsOfUsePopUp.TermsOfUseLocators import TermsOfUseLocators

class TermsOfUseActions:
    def __init__(self, seleniumInfra:SeleniumInfra):
        self.seleniumInfra = seleniumInfra
        self.locators = TermsOfUseLocators()


    def handlePopUp(self):
        h=self.seleniumInfra.driver.window_handles
        self.seleniumInfra.driver.switch_to.window(h[1])
        if self.seleniumInfra.isElementExist(*self.locators.popUpTermsOfUse):
            self.seleniumInfra.clickButton(*self.locators.btnClosePopUp)
        else:
            pass
