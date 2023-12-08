import logging

import pytest
import requests
from selenium import webdriver

from src.pageFactory.utils.url_s import URLS


def setup_logger():
    logs = logging.getLogger(__name__)
    logs.setLevel(logging.DEBUG)

    # Create a log formatter with the desired format
    formatter = logging.Formatter('%(asctime)s [%(filename)s.%(funcName)s:%(lineno)d] - %(levelname)s: %('
                                  'message)s')

    # Define a log file path
    logfile = 'test.log'

    # Create a file handler for logging to a file
    file_handler = logging.FileHandler(logfile)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # Create a console handler for logging to the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # Add the handlers to the logs
    logs.addHandler(file_handler)
    logs.addHandler(console_handler)

    return logs


def clear_log_file(logfile):
    try:
        with open(logfile, 'w'):
            pass
        print(f"Cleared logs in {logfile}")
    except Exception as e:
        print(f"Error clearing logs: {str(e)}")


# Usage
log_file = 'test.log'
clear_log_file(log_file)

# Initialize the logger
logger = setup_logger()


@pytest.fixture(scope="module")
def driver():
    # Initialize the WebDriver instance (you can choose the browser here)
    driver = webdriver.Chrome()
    logger.info("Browser started")

    driver.maximize_window()

    # Code to navigate to the login page
    logger.info("Entered homepage url")
    driver.get(URLS.homepage_url)

    # Get the current URL from Selenium
    current_url = driver.current_url

    # Send an HTTP GET request to the same URL
    response = requests.get(current_url)

    # Get the status code from the response
    status_code = response.status_code

    # Asserting user is navigated to homepage
    if status_code == 200:
        # Log the status code
        logger.info(f"HTTP Status Code of " + current_url + f": {status_code}")
        logger.info("Navigated to home page")

        # Taking screenshot of homepage
        logger.info("Taking homepage screenshot")
        driver.save_screenshot('screenshots/homepage/navigation/homepage.png')
    else:
        logger.error("failed to navigate to home page")

    yield driver  # Provide the WebDriver instance to tests

    # Teardown - close the browser
    driver.quit()
    logger.info("Browser closed")