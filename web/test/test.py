from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class CustomWebDriverException(Exception):
    pass

# Set up Chrome options for headless mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')  # Required when running as root (e.g., in Docker)
chrome_options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems
chrome_options.add_argument('--disable-gpu')

# Set up the WebDriver with Chrome options
driver = webdriver.Remote(
    command_executor='http://192.168.1.4:4444/wd/hub',
    options=chrome_options
)

try:
    # Open the webpage
    driver.get('http://192.168.1.4:5500/web/pages/homepage.html')
    # driver.get('https://www.google.com')

    # Explicit wait for the search input
    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'search'))
    )

    # Find and interact with elements
    search_input.send_keys('hello')

    submit_button = driver.find_element(By.ID, 'submit')
    submit_button.click()

    # Explicit wait for the success message
    success_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'success'))
    )

    # Perform assertions to validate the results
    assert 'hello' in success_message.text, "Success message does not contain the expected text."
    print("Correct Input Test:", success_message.text)

except TimeoutException as te:
    raise CustomWebDriverException(f"Timeout occurred: {str(te)}")
except NoSuchElementException as nse:
    raise CustomWebDriverException(f"Element not found: {str(nse)}")
except AssertionError as ae:
    raise CustomWebDriverException(f"Assertion error: {str(ae)}")
except Exception as e:
    raise CustomWebDriverException(f"An unexpected error occurred: {str(e)}")

try:
    # Open the webpage
    driver.get('http://192.168.1.4:5500/web/pages/homepage.html')
    # driver.get('https://www.google.com')

    # Explicit wait for the search input
    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'search'))
    )

    # Find and interact with elements
    search_input.send_keys('105 OR 1=1')

    submit_button = driver.find_element(By.ID, 'submit')
    submit_button.click()

    # Explicit wait for the success message
    success_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'failure'))
    )

    # Perform assertions to validate the results
    assert 'Invalid characters in the search term. Please enter a valid search term.' in success_message.text, "Failure message does not contain the expected text."
    print("SQL Injection Test:", success_message.text)

except TimeoutException as te:
    raise CustomWebDriverException(f"Timeout occurred: {str(te)}")
except NoSuchElementException as nse:
    raise CustomWebDriverException(f"Element not found: {str(nse)}")
except AssertionError as ae:
    raise CustomWebDriverException(f"Assertion error: {str(ae)}")
except Exception as e:
    raise CustomWebDriverException(f"An unexpected error occurred: {str(e)}")

try:
    # Open the webpage
    driver.get('http://192.168.1.4:5500/web/pages/homepage.html')
    # driver.get('https://www.google.com')

    # Explicit wait for the search input
    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'search'))
    )

    # Find and interact with elements
    search_input.send_keys('<script>alert(123)</script>')

    submit_button = driver.find_element(By.ID, 'submit')
    submit_button.click()

    # Explicit wait for the success message
    success_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'failure'))
    )

    # Perform assertions to validate the results
    assert 'Invalid characters in the search term. Please enter a valid search term.' in success_message.text, "Failure message does not contain the expected text."
    print("XSS Attack Test:", success_message.text)
    
except TimeoutException as te:
    raise CustomWebDriverException(f"Timeout occurred: {str(te)}")
except NoSuchElementException as nse:
    raise CustomWebDriverException(f"Element not found: {str(nse)}")
except AssertionError as ae:
    raise CustomWebDriverException(f"Assertion error: {str(ae)}")
except Exception as e:
    raise CustomWebDriverException(f"An unexpected error occurred: {str(e)}")

finally:
    # Close the browser
    driver.quit()
