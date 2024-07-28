import time

import pyautogui
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture()
def setup_and_teardown():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://carbon.bizdata360.com/#/login")

    # Perform zoom out using keyboard
    for _ in range(2):
        pyautogui.hotkey('ctrl', '-')
        time.sleep(0.5)
    yield
    driver.quit()


def test_verify_login_with_valid_credentials(setup_and_teardown):
    # Enter valid credentials
    driver.find_element(By.ID, "login_username").send_keys("todafeh107@luravell.com")
    driver.find_element(By.ID, "login_password").send_keys("Raunak@8390")

    # Select remember me checkbox
    driver.find_element(By.ID, "login_checkbox-input").click()

    # Click on login submit button
    driver.find_element(By.ID, "login_submit").click()

    # Wait for the "Organization Admin" element to be visible
    organization_admin_element = WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//span["
                                                                     "@class='profile"
                                                                     "-name']"
                                                           )))

    # Assert that the "Organization Admin" element is displayed
    assert organization_admin_element.is_displayed(), "Organization Admin text is not displayed after login"
