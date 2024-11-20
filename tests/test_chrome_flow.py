import pytest
import sys
import os
import allure
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.config import get_driver
from utils.reporting import capture_screenshot
from pages.chrome_page import ChromePage
from selenium.webdriver.common.action_chains import ActionChains
from utils.data_loader import load_test_data


@pytest.fixture(scope="function")
def setup():
    driver = get_driver()
    yield driver
    # driver.quit()

@allure.severity(allure.severity_level.NORMAL)
def test_chrome_flow(setup):
    driver = setup
    chrome_page = ChromePage(driver)
    driver.implicitly_wait(10)

    #Step 1: In case I have not logged in to my Google account when I just created a new device so i click "Use Without An Account" button
    chrome_page.click_use_without_an_account_btn()
    driver.implicitly_wait(10)

    #Step 2: Click "Got it" button in noti = "Enhanced ad privacy in Chrome"
    chrome_page.click_got_it_btn()
    driver.implicitly_wait(10)
    
    #Step 3: Navigate to "https://www.google.com/"
    chrome_page.open_url()
    driver.implicitly_wait(20)

    #Step 4: Search for a keyword = Elfie
    test_data = load_test_data("data/test_data.json")
    chrome_page.search_keyword(test_data['keyword'])
    driver.implicitly_wait(20)

    #Step 5: Click on the first result
    chrome_page.click_first_result()
    driver.implicitly_wait(20)

    #Step 6: Verify logo and capture
    assert chrome_page.verify_logo_displayed(), "Logo not displayed"
    driver.implicitly_wait(30)
    capture_screenshot(driver, "step_logo_displayed")

    #Step 7: Toggle menu and verify
    assert chrome_page.toggle_menu_and_verify(), "Menu toggle failed"
    driver.implicitly_wait(20)
    capture_screenshot(driver, "step_menu_toggled")

    #Step 8: Click X menu
    chrome_page.click_x_menu_btn()

    #Step 9: Click Accept All button
    chrome_page.click_accept_all_btn()

    #Step 10: Scroll to bottom, verify copyright text, and capture
    chrome_page.scroll_to_bottom()
    driver.implicitly_wait(20)
    assert chrome_page.verify_copyright_text(), "Copyright text missing"
    driver.implicitly_wait(20)
    capture_screenshot(driver, "step_copyright_verified")