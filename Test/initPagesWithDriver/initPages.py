from Infra.SeleniumInfra import SeleniumInfra
from Pages.BasePage import BasePage
from Pages.LandingPage.LPActions import LandingActions
from Pages.CoronaPage.CoronaActions import CoronaActions
from Pages.CoronaPage.ControlPanel.TermsOfUsePopUp.TermsOfUseActions import TermsOfUseActions
from Pages.CoronaPage.ControlPanel.FocusOn.FocusOnActions import FocusOnActions


class InitPagesWithDriver:
    def __init__(self):
        self.seleniumInfra = SeleniumInfra()
        self.bp = BasePage(self.seleniumInfra)
        self.lp = LandingActions(self.seleniumInfra)
        self.cp = CoronaActions(self.seleniumInfra)
        self.tp = TermsOfUseActions(self.seleniumInfra)
        self.fp = FocusOnActions(self.seleniumInfra)