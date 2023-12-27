import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base.base_driver import BaseDriver
from pages.search_flight_result_page import SearchFlightResults


class LaunchPage(BaseDriver):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    DEPART_FROM_FIELD = "//input[@id='BE_flight_origin_city']"
    GOING_TO_FIELD = "//input[@id='BE_flight_arrival_city']"
    GOING_TO_RESULT_LIST ="//div[@class='viewport']//div[1]/li"
    SELECT_DATE_FIELD = "//input[@id='BE_flight_origin_date']"
    ALL_DATES = "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"
    SEARCH_BUTTON = "//input[@value='Search Flights']"
    def getDepartFromField(self):
        return self.wait_until_element_is_clickble(By.XPATH, self.DEPART_FROM_FIELD)

    def getGoingToField(self):
        return self.wait_until_element_is_clickble(By.XPATH, self.GOING_TO_FIELD)
    def getGoingToResult(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.GOING_TO_RESULT_LIST)
    def getDepartureDateField(self):
        return self.wait_until_element_is_clickble(By.XPATH,self.SELECT_DATE_FIELD)
    def getAllDatesField(self):
        return self.wait_until_element_is_clickble(By.XPATH, self.ALL_DATES)
    def getSearchButton(self):
        return self.wait_until_element_is_clickble(By.XPATH, self.SEARCH_BUTTON)


    def enterDepartFromLocation(self, departlocation):
        self.getDepartFromField().click()
        time.sleep(3)

        self.getDepartFromField().send_keys(departlocation)
        self.getDepartFromField().send_keys(Keys.ENTER)

    def enterGoingToLocation(self,goingtolocation):
        self.getGoingToField().click()
        time.sleep(2)
        self.getGoingToField().send_keys(goingtolocation)
        time.sleep(3)

        self.getGoingToField().send_keys(Keys.ENTER)
        time.sleep(3)

        search_results = self.getGoingToResult()
        for results in search_results:
            print(results.text)
            if goingtolocation in results.text:
                results.click()
                # time.sleep(3)
                break

    def enterDepatureDate(self,depaturedate):
        self.getDepartureDateField().click()
        time.sleep(3)
        all_dates = self.getAllDatesField().find_elements(By.XPATH,self.ALL_DATES)
        for date in all_dates:
            if date.get_attribute("data-date")==depaturedate:
                date.click()
                time.sleep(3)
                break

    def clickSearchFlightButton(self):
        self.getSearchButton().click()
        time.sleep(3)

    def searchFlights(self,depaturelocation,goingtolocation,depaturedate):
        self.enterDepartFromLocation(depaturelocation)
        self.enterGoingToLocation(goingtolocation)
        self.enterDepatureDate(depaturedate)
        self.clickSearchFlightButton()
        search_flight_result = SearchFlightResults(self.driver)
        return search_flight_result

    # jhhjhjhjh