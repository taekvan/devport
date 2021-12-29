'''
Created on Dec 29, 2021
@author: a.volkodatov
'''

import unittest
import string
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from framework.pages.start_page import StartPageLocators
from test_base import TestBase


class RegistrationTest(TestBase):
    """Class to test registration and displayed games quantity"""
    psw_len_error = "Password must contain at least 8 characters include letters, "\
        "numbers and special characters."

    def test_registration_positive(self):
        """Method to check positive registration"""
        # Check the page is displayed
        self.open_registration_form()
        # Fill the form
        user_email = self.string_generator(10) + "@gmail.com"
        user_login = self.string_generator(10)
        user_password = self.password_generator(10)
        self.fill_the_form(user_email, user_login, user_password)
        # Click registration button
        self.driver.find_element(By.XPATH, StartPageLocators.RGSTR_SUBMIT_XPATH).click()
        WebDriverWait(self.driver, 5).until(
            EC.invisibility_of_element(
                (By.XPATH, StartPageLocators.RGSTR_FORM_WRAPPER_XPATH)),
            message="The registration form should not be visible")
        # Check the user logged in
        self.check_user_logged_in(user_email)

    def test_registration_short_password(self):
        """Method to check negative registration due to short password"""
        # Check the page is displayed
        self.open_registration_form()
        # Fill the form
        user_email = self.string_generator(8) + "@gmail.com"
        user_login = self.string_generator(8)
        user_password = self.password_generator(7)
        self.fill_the_form(user_email, user_login, user_password)
        # Check the registration button is disabled
        regisrt_btn = self.driver.find_element(By.XPATH, StartPageLocators.RGSTR_SUBMIT_XPATH)
        self.assertFalse(regisrt_btn.is_enabled())
        # Check the error
        length_err_txt = self.driver.find_element(
            By.XPATH, StartPageLocators.RGSTR_PASSWORD_LENGTH_ERROR_XPATH).text
        self.assertEqual(
            length_err_txt, self.psw_len_error,
            f"The password length error should be {self.psw_len_error}, but got {length_err_txt}")

    def test_check_sport_ivents(self):
        """Method to check the quantity of sport ivents"""
        # Load the Live page
        live_btn = WebDriverWait(self.driver, 8).until(
            EC.visibility_of_element_located(
                (By.XPATH, StartPageLocators.LIVE_BTN_XPATH)),
            message="The live button should be displayed")
        live_btn.click()
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(
                (By.XPATH, StartPageLocators.FAV_BLOCK_XPATH)),
            message="The sport slider should be displayed")
        # Get list of sport types
        list_of_elem = self.driver.find_elements(By.XPATH, StartPageLocators.SLIDER_ITEM_LIST_XPATH)
        # Check for each sport type the amount of game rows and displayed amount of games
        for i, sport_tab in enumerate(list_of_elem):
            if i % 3 == 0 and i != 0:
                # Press further arrow every 3d sport type
                try:
                    further_arrow = self.driver.find_element(
                        By.XPATH, StartPageLocators.FURTHER_ARROW_XPATH)
                    further_arrow.click()
                except NoSuchElementException:
                    pass

            sport_tab.click()
            sport_name = sport_tab.find_element(By.XPATH, StartPageLocators.SPORT_NAME_XPATH).text
            WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located(
                    (By.XPATH, StartPageLocators.TABLE_ITEM_XPATH)),
                message=f"The games in {sport_name} section didn't load")

            row_games = len(self.driver.find_elements(By.XPATH, StartPageLocators.TABLE_ITEM_XPATH))
            events_amount = int(sport_tab.find_element(
                By.XPATH, StartPageLocators.SPORT_COUNT_XPATH).text)

            self.assertEqual(
                row_games, events_amount,
                f"There are {row_games} rows for {sport_name}, \
                    but event amount {events_amount} is displayed")

    def open_registration_form(self):
        """Method to open registration form"""
        # Check the main page is displayed
        main_page_wrapper = self.driver.find_element(
            By.XPATH, StartPageLocators.MAIN_PAGE_WRAPPER_XPATH)
        self.assertTrue(main_page_wrapper.is_displayed(),
                        "The main page should be displayed")
        # Open registration form
        regist_button = self.driver.find_element(By.XPATH, StartPageLocators.RGSTR_BTN_XPATH)
        regist_button.click()
        # Check the registration form is displayed
        reg_form = self.driver.find_element(By.XPATH, StartPageLocators.RGSTR_FORM_WRAPPER_XPATH)
        self.assertTrue(reg_form.is_displayed(), "The registration form should be displayed")

    def fill_the_form(self, user_email, user_login, user_password):
        """Method to fill in the registration form"""
        # Fill and check email field
        email = self.driver.find_element(By.XPATH, StartPageLocators.RGSTR_EMAIL_XPATH)
        email.send_keys(user_email)
        actual_email = email.get_property('value')
        self.assertEqual(actual_email, user_email,
                         f"The email value should be {user_email}, but got {actual_email}")
        # Fill and check login field
        login = self.driver.find_element(By.XPATH, StartPageLocators.RGSTR_LOGIN_XPATH)
        login.send_keys(user_login)
        actual_login = login.get_property('value')
        self.assertEqual(actual_login, user_login,
                         f"The login value should be {user_login}, but got {actual_login}")
        # Fill and check password field
        pswd = self.driver.find_element(By.XPATH, StartPageLocators.RGSTR_PASSWORD_XPATH)
        pswd.send_keys(user_password)
        actual_pswrd = pswd.get_property('value')
        self.assertEqual(actual_pswrd, user_password,
                         f"The password value should be {user_password}, but got {actual_pswrd}")
        # Fill and check confirm password field
        pswd_conf = self.driver.find_element(
            By.XPATH, StartPageLocators.RGSTR_CONFIRM_PASSWORD_XPATH)
        pswd_conf.send_keys(user_password)
        actual_pswrd_conf = pswd_conf.get_property('value')
        self.assertEqual(
            actual_pswrd_conf, user_password,
            f"The confirm password value should be {user_password}, but got {actual_pswrd_conf}")
        # Set checkbox
        self.click_registration_checkbox()

    def check_user_logged_in(self, email):
        """Method to check user logged in successfully"""
        logged_user = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(
                (By.XPATH, StartPageLocators.LOGGED_USER_EMAIL_XPATH)),
            message=f"Logged user {email} should be displayed at the top")
        self.assertEqual(logged_user.text, email,
                         f"The expected logged user should be {email}, but got {logged_user.text}")

    @staticmethod
    def string_generator(num):
        """Method to generate string with certain length"""
        return "".join(random.choice(string.ascii_letters) for x in range(num))

    @staticmethod
    def password_generator(num):
        """Method to generate password with certain symbols and length"""
        num = max(num, 5)
        let, dig, symbols = list(string.ascii_letters), list(string.digits), list("!@#$%^&*()")
        for elem in (let, dig, symbols):
            random.shuffle(elem)
        password_list = (dig[:2]+symbols[:2]+let[:(num-4)])
        random.shuffle(password_list)
        return "".join(password_list)

    def click_registration_checkbox(self):
        """Method to click on checkbox"""
        checkbox = self.driver.find_element(
            By.XPATH, StartPageLocators.RGSTR_LICENSE_CHECKBOX_XPATH)
        ActionChains(self.driver).click(checkbox).perform()


if __name__ == '__main__':
    unittest.main()
