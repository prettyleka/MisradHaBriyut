from Infra.SeleniumInfra import SeleniumInfra
from Pages.CoronaPage.ControlPanel.FocusOn.FocusOnLocators import FocusOnLocators

class FocusOnActions:
    def __init__(self, seleniumInfra:SeleniumInfra):
        self.seleniumInfra = seleniumInfra
        self.locators = FocusOnLocators()

    def getYesterdayNumberOfContagious(self):
        el = self.seleniumInfra.findElementBy(*self.locators.yesterdayData)
        numb = el.text.split(' ')
        numberOfContagious=numb[0]+numb[1]
        return numberOfContagious

    def getFromMidnightNumberOfContagious(self):
        el = self.seleniumInfra.findElementBy(*self.locators.fromMidnightData)
        fromMidnightData = el.text
        return fromMidnightData