import pytest
# from selenium import webdriver
# from selenium.common import InvalidArgumentException
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager

from HybridFramework_TestAutomationFramework.Pages.Air_India_LaunchPage import LaunchPage
from HybridFramework_TestAutomationFramework.Pages.search_flight_results_page import SearchFlightResults


@pytest.mark.usefixtures("setup")
class TestSearchandVerifyFilter():
    def test_search_flights(self):
        #launching browser and opening travel website
        lp = LaunchPage(self.driver,)
        lp.handle_cookie_popup()
        lp.searchFlights("New Delhi","Chennai","2025/9/16","2025/10/26")
        # select the Origin
        #lp.departfrom("New Delhi")
        # lp.enter_DepartFromLocation("New Delhi")
        # # select the Destination
        # #lp.goingto("Chennai")
        # lp.enter_GoingToLocation("Chennai")
        # # departure date
        # #lp.departdate("2025/9/16")
        # lp.enter_departdate("2025/9/16")
        # # return date
        # lp.enter_returndate("2025/10/26")
        #driver.find_element(By.ID, "calendar-icon-departureDate-0").click()
        #lp.click_searchbutton()
        # === Scroll & scrape flights ===
        lp.page_scroll()
        # Creating Object for Search_flight_results_page
        # Get & parse results
        # Parse flight results
                # Get flights data from page object
        sf = SearchFlightResults(self.driver)
        flights_data = sf.filter_flights()  # <--- already extracted via Utils

