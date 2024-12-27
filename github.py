from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Credentials
username = "xxxxxx"
password = "xxxxxx"

# Path to Edge WebDriver
driver_path = 'msedgedriver.exe'

# Edge Options and Service
options = Options()
# Uncomment these options as needed
# options.add_argument("--start-maximized")  
options.add_argument("--headless")
service = Service(executable_path=driver_path)

# Initialize WebDriver
driver = webdriver.Edge(service=service, options=options)

# Open GitHub login page
driver.get("https://github.com/login")

# Find username/email field and send the username to the input field
driver.find_element(By.ID, "login_field").send_keys(username)
# Find password input field and insert password
driver.find_element(By.ID, "password").send_keys(password)
# Click the login button
driver.find_element(By.NAME, "commit").click()

# Wait for the page to load completely
WebDriverWait(driver, 10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)

# Error message to look for
error_message = "Incorrect username or password."
# Get the errors (if any)
errors = driver.find_elements(By.CSS_SELECTOR, ".flash-error")

# Check for login success or failure
if any(error_message in e.text for e in errors):
    print("[!] Login failed")
else:
    print("[+] Login successful")

# Wait for the repositories container to load
repos = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".js-repos-container"))
)

# Print public repositories
repo_items = repos.find_elements(By.CSS_SELECTOR, "li.public")  # Use "li.private" for private repos
for repo in repo_items:
    repo_link = repo.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
    print(repo_link)

# Close the driver
driver.close()
