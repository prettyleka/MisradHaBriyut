import time

import pytest as pytest
from Test.initPagesWithDriver import init


class TestFirstTest:
    def setup_class(self):
        self.initial = init.pageWithDriver()

    def test_FirstTest(self):
        self.initial.goTo.bp.moveToSite("https://www.gov.il/he/departments/ministry_of_health/govil-landing-page")
        self.initial.goTo.lp.clickOnUperMenuBtn("נגיף קורונה")
        time.sleep(3)
        self.initial.goTo.cp.clickGeneralSituation()
        self.initial.goTo.tp.handlePopUp()
        numberOfContagious = self.initial.goTo.fp.getYesterdayNumberOfContagious()
        fromMidnightData = self.initial.goTo.fp.getFromMidnightNumberOfContagious()
        normalDeviation = int(numberOfContagious)*0.2
        if int(fromMidnightData)>=(int(numberOfContagious)-normalDeviation) and int(fromMidnightData)<=(int(numberOfContagious)+normalDeviation):
            print("the result is within deviation range")
        else:
            print("the result is out of deviation range")









if __name__ == '__main__':
    import sys, inspect, os

    clsmembers = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    class_name = getattr(sys.modules[__name__], clsmembers[0][0])
    module_name = os.path.splitext(os.path.basename(__file__))[0]
    method_list = [func for func in dir(class_name) if
                   callable(getattr(class_name, func)) and not func.startswith("__") and func.startswith("test")]
    function_dict = {}
    function_dict["0"] = "run all tests"
    for i in range(1, len(method_list) + 1):
        function_dict[str(i)] = method_list[i - 1]
    print(function_dict)
    txt = input("please choose test you want to run or debug and then press enter")
    command = "-v " + module_name + ".py::" + clsmembers[0][0] + "::" + function_dict[txt] + ""
    if txt != "0":
        pytest.main(command.split(" "))
    else:
        pytest.main(["-v", module_name + ".py"])