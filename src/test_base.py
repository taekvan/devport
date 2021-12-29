'''
Created on Dec 29, 2021
@author: a.volkodatov
'''
import unittest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from framework.urls import Urls


class LoginTest(unittest.TestCase):
    """class to start the browser with default page"""

    driver = None


class TestBase(unittest.TestCase):
    """Class to create driver instance"""
    driver = None

    @classmethod
    def setUp(cls):
        """  The testing framework will automatically call this method
        before tests. """

        driver_path = os.path.abspath(
            os.path.join(os.getcwd(), "src", "drivers", "chromedriver.exe"))
        service = Service(driver_path)
        cls.driver = webdriver.Chrome(service=service,
                                      options=TestBase.prepare_chrome_options())
        cls.driver.get(Urls.start_page)

    @classmethod
    def tearDown(cls):
        """
        The testing framework will automatically call this method
        to tidy up the environment after the tests"""

        cls.driver.quit()

    @staticmethod
    def prepare_chrome_options():
        """method to prepare chrome option"""
        chrome_options = ChromeOptions()
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-software-rasterizer')
        return chrome_options
