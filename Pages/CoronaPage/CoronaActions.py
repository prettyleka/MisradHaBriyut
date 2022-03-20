from Infra.SeleniumInfra import SeleniumInfra
from Pages.CoronaPage.CoronaLocators import CoronaLocators

class CoronaActions:
    def __init__(self, seleniumInfra:SeleniumInfra):
        self.seleniumInfra = seleniumInfra
        self.locators = CoronaLocators()

    def scrollToGeneralSituation(self):
        bigEl= self.seleniumInfra.findElementBy(*self.locators.bigEl)
        self.seleniumInfra.genericScroll(element=bigEl, direction="upToDown", locatorTypeToWait=self.locators.generalSituationBtn[0], locatorValueToWait=self.locators.generalSituationBtn[1])

    def clickGeneralSituation(self):
        self.seleniumInfra.clickButton(*self.locators.generalSituationBtn)