from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.service import Service

# Set up Chrome options for headless mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # Add other options as needed

# Set the path to Chromedriver explicitly
service = Service(executable_path='../chromedriver/chromedriver.exe')
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Open the webpage
    driver.get('http://127.0.0.1:5500/web/pages/homepage.html')

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
    print(f"Message: {str(success_message.text)}")


except TimeoutException as te:
    print(f"Timeout occurred: {str(te)}")
except NoSuchElementException as nse:
    print(f"Element not found: {str(nse)}")
except AssertionError as ae:
    print(f"Assertion error: {str(ae)}")
except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")

finally:
    # Close the browser
    driver.quit()
