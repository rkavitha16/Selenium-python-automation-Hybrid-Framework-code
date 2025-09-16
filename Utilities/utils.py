from selenium.webdriver.common.by import By


class Utils():

    def extract_flight_data(self,flights):
        flights_data = []
        for i, flight in enumerate(flights, 1):
            try:
                airline = flight.find_element(By.CSS_SELECTOR, "div[aria-label*='Airlines']").get_attribute(
                    "aria-label")
            except:
                airline = "N/A"

            details = flight.get_attribute("aria-label") or "N/A"

            try:
                stops = flight.find_element(By.CSS_SELECTOR, "p.css-bh30xj").text
            except:
                stops = "N/A"

            try:
                price = flight.find_element(By.CSS_SELECTOR, "div[data-test-id='price']").text
            except:
                price = "N/A"

            flights_data.append([i, airline, details, stops, price])

        return flights_data

