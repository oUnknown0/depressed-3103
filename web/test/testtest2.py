from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.common.exceptions import NoSuchElementException
import os 
import requests
from abc import ABC, abstractmethod

class SeleniumChromeDriver:
    """Provides functionality like finding elements, submiting inputs on webpage using ChromeDriver"""
    def __init__(self):
        self.driver = self.init_driver()

    def init_driver(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-web-security')
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        # driver = webdriver.Chrome(options=chrome_options)
        driver = webdriver.Remote(
            command_executor='http://192.168.1.4:4444/wd/hub',
            options=chrome_options
        )
        return driver

    def validate_driver_path(self):
        return os.path.exists(self.driver_path) and os.path.isfile(self.driver_path)

    def open_page(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def find_element(self, by, value, wait_time=10):
        try:
            element = WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_element_located((by, value))
            )
            return element
        except TimeoutException:
            print(f"Timeout occurred while trying to find element: {value}")
        except NoSuchElementException:
            print(f"Element not found: {value}")

    def get_element_text(self, by, value, wait_time=10):
        try:
            element = WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_element_located((by, value))
            )
            return element.text if element else None
        except TimeoutException:
            print(f"Timeout occurred while trying to find element: {value}")
        except NoSuchElementException:
            return None

    def element_exists(self, by, value, wait_time=10):
        try:
            WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_element_located((by, value))
            )
            return True
        except (TimeoutException, NoSuchElementException):
            return False

    def input_text(self, by, value, text):
        element = self.find_element(by, value)
        if element:
            element.send_keys(text)

    def click_button(self, by, value):
        button = self.find_element(by, value)
        if button:
            button.click()

    def close(self):
        self.driver.quit()