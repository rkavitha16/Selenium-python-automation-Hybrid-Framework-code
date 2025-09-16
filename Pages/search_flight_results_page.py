from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from HybridFramework_TestAutomationFramework.Utilities.utils import Utils


class SearchFlightResults():
    def __init__(self,driver):
        self.driver = driver
        self.utils = Utils()

    def filter_flights(self):
        wait = WebDriverWait(self.driver,10)
        flights = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@aria-label,'Departure')]")))
        print(f"Total flights found: {len(flights)}")

        # Use utils to extract flight data
        flights_data = self.utils.extract_flight_data(flights)
        # print nicely
        for flight in flights_data:
            print(f"\nFlight {flight[0]}")
            print(f" Airline: {flight[1]}")
            print(f" Details: {flight[2]}")
            print(f" Stops: {flight[3]}")
            print(f" Price: {flight[4]}")

        return flights_data

