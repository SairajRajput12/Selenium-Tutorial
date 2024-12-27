from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

load_dotenv()

# Credentials
username_value = os.getenv("USER_NAME")
password_value = os.getenv("USER_PASSWORD")

# Path to Edge WebDriver
driver_path = 'msedgedriver.exe'

# Edge Options and Service
options = Options()
# Uncomment these options as needed
# options.add_argument("--start-maximized")  
# options.add_argument("--headless")
service = Service(executable_path=driver_path)

# Initialize WebDriver
driver = webdriver.Edge(service=service, options=options)

# Create WebDriverWait instance
wait = WebDriverWait(driver, 10)

# Open Twitter login page
driver.get("https://x.com/i/flow/login")

# Locate username input field and enter the username
username = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'input[autocomplete="username"]'))
)
username.send_keys(username_value)

# Locate and click the login button
login_button = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '[role="button"].r-13qz1uu'))
)
login_button.click()


password = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR,'input[autocomplete="current-password"]'))
)

password.send_keys(password_value) 

login_button = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid*=Login_Button]'))
)
login_button.click()

direct_message_link = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid=AppTabBar_DirectMessage_Link]'))
)


