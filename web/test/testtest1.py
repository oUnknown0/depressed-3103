from testtest2 import SeleniumChromeDriver
from selenium.webdriver.common.by import By
import unittest

class TestWebpage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = SeleniumChromeDriver()
        cls.submit_button = "submit"
        cls.search_input = "search"
        cls.search_result = "search_result"
        cls.error_message = "failure"

        cls.home_page = "http://192.168.1.4:5500/web/pages/homepage.html"
        cls.search_page = "http://192.168.1.4:5500/web/pages/homepage.html"

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def setUp(self):
        self.driver.open_page(self.home_page)

    def test_home_page_exists(self):
        self.assertEqual(self.driver.get_current_url(), self.home_page, "Home page did not load.")

    def test_search_field_exists(self):
        self.assertTrue(self.driver.element_exists(By.ID, self.search_input), "Search input does not exist on home page.")

    def test_submit_button_exists(self):
        self.assertTrue(self.driver.element_exists(By.ID, self.submit_button), "Submit button does not exist on home page.")

    def test_safe_input_redirects_to_search_page(self):
        text_to_input = "hello"
        self.driver.input_text(By.ID, self.search_input, text_to_input)
        self.driver.click_button(By.ID, self.submit_button)
        
        # Assert that you are in the "nextpage.html"
        current_url = self.driver.get_current_url()
        self.assertIn("nextpage.html", current_url, "Not on the expected page 'nextpage.html'")
        
        # Continue with the existing assertions for the search result
        self.assertTrue(self.driver.element_exists(By.ID, self.search_result), "Search result element does not exist")
        search_result_text = self.driver.get_element_text(By.ID, self.search_result)
        self.assertIn(text_to_input, search_result_text, "Search result page does not display user's input")

    def test_xss_input_doesnt_redirect(self):
        text_to_input = "<script>alert()</script>"
        self.driver.input_text(By.ID, self.search_input, text_to_input)
        self.driver.click_button(By.ID, self.submit_button)

        error_message = self.driver.get_element_text(By.ID, self.error_message)
        self.assertEqual(self.driver.get_current_url(), self.home_page, "XSS input redirects user")
        self.assertIn("Invalid characters in the search term. Please enter a valid search term.", error_message)

    def test_sql_injection_input_doesnt_redirect(self):
        text_to_input = "SELECT * FROM Users"
        self.driver.input_text(By.ID, self.search_input, text_to_input)
        self.driver.click_button(By.ID, self.submit_button)

        error_message = self.driver.get_element_text(By.ID, self.error_message)
        self.assertEqual(self.driver.get_current_url(), self.home_page, "SQL Injection input redirects user")
        self.assertIn("Invalid characters in the search term. Please enter a valid search term.", error_message)

if __name__ == '__main__':
    unittest.main()
