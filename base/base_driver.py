import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseDriver():
    def __init__(self,driver):
        self.driver = driver

    def page_scroll(self):
        pageLength = self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight")
        time.sleep(5)
        match = False
        while (match==False):
            lastcount=pageLength
            time.sleep(3)
            pageLength = self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight")
            if lastcount==pageLength:
                match=True
        time.sleep(4)

    def wait_for_presence_of_all_elements(self,locator_type,locator):
        wait = WebDriverWait(self.driver,10)
        list_of_elements=wait.until(EC.presence_of_all_elements_located((locator_type,locator)))
        return list_of_elements

    def wait_until_element_is_clickble(self,locator_type,locator):
        wait = WebDriverWait(self.driver,10)
        element = wait.until(EC.element_to_be_clickable((locator_type,locator)))
        return element


