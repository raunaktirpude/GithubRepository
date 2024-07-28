import time

import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from test.test_Registration import generate_email_with_timestamp


@pytest.mark.usefixtures("setup_and_teardown", "log_on_failure")
class TestManagement:
    def test_verify_create_user_with_mandatory_field(self):
        # Enter valid credentials
        self.driver.find_element(By.ID, "login_username").send_keys("depenad165@luravel.com")
        self.driver.find_element(By.ID, "login_password").send_keys("Raunak@8390")

        # Select remember me checkbox
        self.driver.find_element(By.ID, "login_checkbox-input").click()

        # Submit login form
        self.driver.find_element(By.ID, "login_submit").click()

        # Wait for the element to be clickable
        menu_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//ion-menu-button[@id='head_ham_btn']")))
        self.driver.execute_script("arguments[0].click();", menu_button)

        # Click on management
        management_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//ion-label[normalize-space()='Management']"))
        )
        self.driver.execute_script("arguments[0].click();", management_button)

        # Click on user option
        user_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//ion-label[normalize-space()='User']"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", user_button)
        self.driver.execute_script("arguments[0].click();", user_button)

        # Perform a right-click if the menu does not close
        # WebDriverWait.driverWait(self.driver,10).until(expected_conditions.invisibility_of_element_located(user_button))
        ActionChains(self.driver).move_by_offset(20, 10).context_click().perform()

        add_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Add']")))
        self.driver.execute_script("arguments[0].click();", add_button)

        # Fill up add user form
        # First name
        self.driver.find_element(By.XPATH, "//input[@placeholder='First name']").send_keys("Create")

        # Last name
        self.driver.find_element(By.XPATH, "//input[@placeholder='Last name']").send_keys("User")

        # Email address
        self.driver.find_element(By.XPATH, "//input[@placeholder='Email Address']").send_keys(
            generate_email_with_timestamp())

        # User permission
        self.driver.find_element(By.XPATH, "//mat-select[@formcontrolname='permission']").click()
        self.driver.find_element(By.XPATH,
                                 "//mat-option[@role='option']//span[contains(text(),'List (User)')]").click()

        self.driver.find_element(By.XPATH,
                                 "//mat-option[@role='option']//span[contains(text(),'List (Integration Bridge)')]").click()

        # Perform Tab key press
        ActionChains(self.driver).send_keys(Keys.TAB).perform()
        time.sleep(3)
        # # Make admin toggle button
        toggle_button = self.driver.find_element(By.XPATH, "//button[@role='switch']")
        toggle_button.click()
        time.sleep(1)
        toggle_button.click()
        #
        # # Click on add button to create or add user
        # user_add_button = self.driver.find_element(By.XPATH, "//span[normalize-space()='Add']")
        # user_add_button.click()
