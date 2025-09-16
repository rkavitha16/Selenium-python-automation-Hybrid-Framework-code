import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from HybridFramework_TestAutomationFramework.Base.base_driver import BaseDriver

class LaunchPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # ✅ New method for handling cookies
    def handle_cookie_popup(self):
        try:
            accept_btn = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Accept All')]"))
            )
            accept_btn.click()
            print("✅ Cookie popup closed")
        except:
            print("ℹ️ No cookie popup found")

    # ---------Locators----------
    DEPART_FROM_FIELD = "//input[@id='searchForm-singleBound-origin-input']"
    GOING_TO_FIELD = "//input[@id='searchForm-singleBound-destination-input']"
    GOING_TO_SEARCH_FIELD = "//ul[@class='css-123so4a']//li"
    SELECT_DEPART_DATE_ICON = "calendar-icon-departureDate-0"
    SELECT_DEPART_DATE_FIELD = "//tbody[@class='rdp-weeks']//tr//td[contains(@class,'rdp-day')]"
    SELECT_RETURN_DATE_ICON = "calendar-icon-returnDate-0"
    MOVE_TO_NEXT_MONTH_BUTTON = "//button[@aria-label='Go to the Next Month']"
    SELECT_RETURN_DATE_FIELD = "//tbody[@class='rdp-weeks']//tr//td[contains(@class,'rdp-day')]"
    SEARCH_BUTTON = "button[type='submit']"

    def getDepartFromField(self):
        return self.wait_until_element_is_clickable(By.XPATH,self.DEPART_FROM_FIELD)

    def getgoingtoField(self):
        return self.wait_until_element_is_clickable(By.XPATH,self.GOING_TO_FIELD)

    def goingtosearchfield(self):
        return self.wait_for_presence_of_all_elements(By.XPATH,self.GOING_TO_SEARCH_FIELD)

    def getdeparticon(self):
        return self.wait_until_element_is_clickable(By.ID,self.SELECT_DEPART_DATE_ICON)

    def getdepartdatefield(self):
        return self.wait_until_element_is_clickable(By.XPATH,self.SELECT_DEPART_DATE_FIELD)

    def getreturnicon(self):
        return self.wait_until_element_is_clickable(By.ID, self.SELECT_RETURN_DATE_ICON)

    def movetonextmonth(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.MOVE_TO_NEXT_MONTH_BUTTON)

    def getreturndatefield(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.SELECT_RETURN_DATE_FIELD)

    def searchbutton(self):
        return self.wait_until_element_is_clickable(By.CSS_SELECTOR,self.SEARCH_BUTTON)

    def enter_DepartFromLocation(self, departLocation):
        self.getDepartFromField().click()
        self.getDepartFromField().send_keys(departLocation)
        time.sleep(2)
        self.getDepartFromField().send_keys(Keys.ENTER)

    def enter_GoingToLocation(self,goingLocation):
        self.getgoingtoField().click()
        self.getgoingtoField().send_keys(goingLocation)
        time.sleep(2)
        search_results = self.goingtosearchfield()
        for results in search_results:
            if goingLocation in results.text:
                results.click()
                break

    # def enter_departdate(self,depart_date):
    #     self.getdeparticon().click()
    #     depart_date = self.getdepartdatefield().find_elements(By.XPATH,self.SELECT_DEPART_DATE_FIELD)
    #     for dates in depart_date:
    #         if dates.get_attribute("data-day") == depart_date:
    #             dates.click()
    #             break
    #
    # def enter_returndate(self,return_date):
    #     self.getreturnicon().click()
    #     return_date = self.getreturndatefield().find_elements(By.XPATH,self.SELECT_RETURN_DATE_FIELD)
    #     for dates in return_date:
    #         if dates.get_attribute("data-day") == return_date:
    #             dates.click()
    #             break
    def enter_departdate(self, depart_date):
        self.getdeparticon().click()
        date_elements = self.getdepartdatefield().find_elements(By.XPATH, self.SELECT_DEPART_DATE_FIELD)
        for date_element in date_elements:
            if date_element.get_attribute("data-day") == depart_date:
                date_element.click()
                break

    def enter_returndate(self, return_date):
        self.getreturnicon().click()
        date_elements = self.getreturndatefield().find_elements(By.XPATH, self.SELECT_RETURN_DATE_FIELD)
        for date_element in date_elements:
            if date_element.get_attribute("data-day") == return_date:
                date_element.click()
                break

    # def click_searchbutton(self):
    #     btn = self.searchbutton()
    #     btn.click()
    #     time.sleep(3)

    def click_searchbutton(self):
        try:
            btn = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, "button[data-testid='searchForm-searchFlights-button']"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)
            time.sleep(1)
            try:
                btn.click()
                print("✅ Search button clicked successfully")
            except:
                print("⚠️ Normal click failed, using JS click...")
                self.driver.execute_script("arguments[0].click();", btn)
        except Exception as e:
            print(f"❌ Search button not found: {e}")

    def searchFlights(self,departlocation,goingtolocation,departuredate,returningdate):
        self.enter_DepartFromLocation(departlocation)
        self.enter_GoingToLocation(goingtolocation)
        self.enter_departdate(departuredate)
        self.enter_returndate(returningdate)
        self.click_searchbutton()

        try:
            self.driver.find_element(By.TAG_NAME, "body").click()
        except:
            pass

        time.sleep(3)
        # def goingto(self, goingtolocation):
    #     going_to = self.wait_until_element_is_clickable(By.XPATH, "//input[@id='searchForm-singleBound-destination-input']")
    #     going_to.click()
    #     going_to.send_keys(goingtolocation)
    #     time.sleep(2)
    #
    #     search_results = self.wait_for_presence_of_all_elements(By.XPATH, "//ul[@class='css-123so4a']//li")
    #     for results in search_results:
    #         if "Chennai" in results.text:
    #             results.click()
    #             break

    # def departdate(self, departuredate):
    #     self.wait_until_element_is_clickable(By.ID, "calendar-icon-departureDate-0").click()
    #
    #     depart_date = self.wait_until_element_is_clickable(By.XPATH, "//tbody[@class='rdp-weeks']//tr//td[contains(@class,'rdp-day')]").find_elements(By.XPATH, "//tbody[@class='rdp-weeks']//tr//td[contains(@class,'rdp-day')]")
    #     for dates in depart_date:
    #         if dates.get_attribute("data-day") == departuredate:
    #             dates.click()
    #             break

    # def returndate(self, returningdate):
    #     self.wait_until_element_is_clickable(By.ID, "calendar-icon-returnDate-0").click()
    #     self.wait_until_element_is_clickable(By.XPATH, "//button[@aria-label='Go to the Next Month']").click()
    #     return_date = self.driver.find_elements(By.XPATH, "//tbody[@class='rdp-weeks']//tr//td[contains(@class,'rdp-day')]")
    #     for date in return_date:
    #         if date.get_attribute("data-day") == returningdate:
    #             date.click()
    #             break
    #
    # def clicksearch(self):
    #     self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    #     time.sleep(5)
