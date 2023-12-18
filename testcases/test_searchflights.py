import time
import pytest
import softest
from pages.yatra_launch_page import LaunchPage
from utilities.utils import Utils


@pytest.mark.usefixtures("setup")
class TestSearchAndVerifyFilter(softest.TestCase):
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        self.ut = Utils()

    def test_search_flights_1_stop(self):
        search_flight_result = self.lp.searchFlights("New Delhi" , "JFK" ,  "21/02/2024")
        time.sleep(3)
        self.lp.page_scroll()
        search_flight_result.filter_flights_by_stop("1 Stop")
        allstop = search_flight_result.get_search_flight_results()
        print(len(allstop))

        self.ut.assertListItemText(allstop , "1 Stop")


    # def test_search_flights_2_stop(self):
    #     search_flight_result = self.lp.searchFlights("New Delhi" ,"JFK" ,"24/02/2024")
    #     self.lp.page_scroll()
    #     search_flight_result.filter_flights_by_stop("2 Stop")
    #     allStop1 = search_flight_result.get_search_flight_results()
    #     print(len(allStop1))
    #     self.ut.assertListItemText(allStop1,"2 Stops")








