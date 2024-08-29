# Drivers/chrome_driver.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def init_chrome_driver():
    # Setup Chrome options for headless browsing
    options = Options()
    options.headless = True

    # Fetch the appropriate ChromeDriver and create the service
    service = Service(ChromeDriverManager().install())
    
    return service, options
