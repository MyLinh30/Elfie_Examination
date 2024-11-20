from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from utils.reporting import capture_screenshot
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os



class ChromePage(BasePage):
    URL = "https://www.google.com/"
    USE_WITHOUT_AN_ACCOUNT_BTN = (By.ID, "signin_fre_dismiss_button")
    GOT_IT_BTN = (By.ID, "ack_button")
    SEARCH_BOX = (By.XPATH, '//android.view.View[@resource-id="tsf"]/android.view.View[1]/android.widget.EditText')
    FIRST_RESULT = (By.XPATH, '//android.widget.TextView[@text="https://vi.elfie.co"]')
    LOGO = (By.XPATH, '	//android.widget.Image[@text="Elfie Logotype"]')
    HAMBURGER_MENU = (By.XPATH, '//android.widget.Button[@text="menu"]')
    CLOSE_MENU = (By.XPATH, '//android.widget.Button[@text="menu"]') 
    ACCEPT_ALL_BTN = (By.XPATH, '//android.widget.Button[@text="Accept All"]')        
    COPYRIGHT_TEXT = (By.XPATH, '//android.widget.TextView[@text="Bản quyền © 2024 Elfie Pte. Ltd."]')


    def open_url(self):
        self.driver.get(self.URL)

    def click_use_without_an_account_btn(self):
        self.click(self.USE_WITHOUT_AN_ACCOUNT_BTN) 

    def click_got_it_btn(self):
        self.click(self.GOT_IT_BTN) 

    def search_keyword(self, keyword):
        try:
            search_box = self.find_element(self.SEARCH_BOX)
            self.click(self.SEARCH_BOX)
            search_box.send_keys(keyword)
            is_focused = search_box.get_attribute("focused")
            print(f"Is input box focused: {is_focused}")
            if is_focused == "true":
                self.driver.press_keycode(66)  # Keycode for Enter
            else:
                raise Exception("Input box is not focused. Cannot proceed.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def click_first_result(self):
        self.click(self.FIRST_RESULT)

    def verify_logo_displayed(self):
        return self.find_element(self.LOGO).is_displayed()

    def toggle_menu_and_verify(self):
        self.click_wait_for_element_visible(self.HAMBURGER_MENU)
        return self.find_element(self.CLOSE_MENU).is_displayed()
    
    def click_x_menu_btn(self):
        self.click_wait_for_element_visible(self.CLOSE_MENU) 

    def click_accept_all_btn(self):
        self.click_wait_for_element_visible(self.ACCEPT_ALL_BTN) 
        
    def verify_copyright_text(self):
        return self.find_element(self.COPYRIGHT_TEXT).is_displayed()


        