from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from selenium.webdriver.common.proxy import Proxy, ProxyType
import os

load_dotenv()

# Credentials
username_value = os.getenv("USER_NAME")
password_value = os.getenv("USER_PASSWORD")
email_value = os.getenv("USER_EMAIL")

# Path to Edge WebDriver
driver_path = 'msedgedriver.exe'
proxy_host = "192.168.1.100"
proxy_port = "8080"
proxy = f"{proxy_host}:{proxy_port}"



# Edge Options and Service
options = Options()
options.add_argument(f"--proxy-server={proxy}")
options.add_argument("--headless=new")
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



# they can ask for otp 
try:
    # Wait for the input field to be present and interactable
    usernumber = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[autocomplete="on"]'))
    )
    usernumber.send_keys('rapsaij1@gmail.com') 

    # Wait for the next button to be present and interactable
    next_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="ocfEnterTextNextButton"]'))
    )
    next_button.click()
    print('Clicked next button successfully')
except:
    print("The element was not found within the time limit.")


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



# Wait for the page to load (adjust as needed for network speed)
driver.implicitly_wait(10)

# Locate the container with class "css-175oi2r r-vacyoi r-ttdzmv"
trend_container = driver.find_element(By.CLASS_NAME, "css-175oi2r.r-vacyoi.r-ttdzmv")

# Extract all spans with the specified class inside the container
trend_spans = trend_container.find_elements(By.CLASS_NAME, "css-1jxf684.r-bcqeeo.r-1ttztb7.r-qvutc0.r-poiln3")

# Get the text content of each trend
trends = [span.text for span in trend_spans]

# Print the trends
for i, trend in enumerate(trends, start=1):
    print(f"Trend {i}: {trend}")

# Close the browser
driver.quit()
