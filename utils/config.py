from appium import webdriver
from appium.options.android import UiAutomator2Options


def get_driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "emulator-5554"
    options.app_package = "com.android.chrome"
    options.app_activity = "com.google.android.apps.chrome.Main"
    options.auto_grant_permissions = True  
    chrome_options = {"args": 
                            ["--disable-notifications","--disable-infobars","--disable-popup-blocking", "--no-first-run",  "--no-default-browser-check",], 
                      "prefs": 
                            {"profile.default_content_setting_values.notifications": 2 }
                    }
    options.set_capability('goog:chromeOptions', chrome_options)
    # Appium server URL
    appium_server_url = "http://localhost:4723/wd/hub"
    # Initialize the WebDriver
    driver = webdriver.Remote(command_executor=appium_server_url, options=options)
    print("Session ID:", driver.session_id)
    return driver

# if __name__ == "__main__":
#     get_driver()