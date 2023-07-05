from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_by_locator(self, *locator):
        element = self.driver.find_element(locator)
        element.click()

    def is_visible(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return bool(element)
        except:
            return False

    def input_text(self, locator, text):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)
        except:
            print("Exception! Can't write in the field.")

    def scroll_into_view(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def is_clickable(self, element):
        try:
            WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable(element))
            return True
        except:
            return False
