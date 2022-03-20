from selenium.webdriver.common.by import By


class CoronaLocators:
    def __init__(self):
        self.bigEl = (By.XPATH, '//body[@class="govil-he"]')
        self.generalSituationBtn = (By.XPATH, "//a[.='תמונת מצב כללית - נתוני קורונה']//parent::div[@class='col-lg-3 col-xl-2 w-auto']")
