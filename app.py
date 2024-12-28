from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from selenium.webdriver.common.proxy import Proxy, ProxyType
import os
from pymongo import MongoClient
import uuid
import datetime
import json
from flask import Flask,jsonify,render_template
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import random


load_dotenv() 

username_value = os.getenv("USER_NAME")
password_value = os.getenv("USER_PASSWORD")
email_value = os.getenv("USER_EMAIL")



# Creting an instance of app 
app = Flask(__name__) 
driver_path = 'msedgedriver.exe'
proxy_host = "xxxxx"
proxy_port = "xxxx"
proxy = f"{proxy_host}:{proxy_port}"


def give_tweets(): 
    # Create WebDriverWait instance
    # Path to Edge WebDriver
    

    # Edge Options and Service
    options = Options()
    options.add_argument(f"--proxy-server={proxy}")
    options.add_argument("--headlesss")
    service = Service(executable_path=driver_path)

    # Initialize WebDriver
    driver = webdriver.Edge(service=service, options=options)

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

   

    # Wait for the page to load (adjust as needed for network speed)
    driver.implicitly_wait(10)

    # Locate the container with class "css-175oi2r r-vacyoi r-ttdzmv"
    trend_container = driver.find_element(By.CLASS_NAME, "css-175oi2r.r-vacyoi.r-ttdzmv")

    # Extract all spans with the specified class inside the container
    trend_spans = trend_container.find_elements(By.CLASS_NAME, "css-1jxf684.r-bcqeeo.r-1ttztb7.r-qvutc0.r-poiln3")

    # Get the text content of each trend
    trends = [span.text for span in trend_spans]

    # Print the trends
    trending_tweets = []
    for i, trend in enumerate(trends, start=1):
        trending_tweets.append({i:trend})

    print('tweets fetched')
    # Close the browser
    driver.quit()
    return trending_tweets
    

@app.route('/')
def home(): 
    return render_template('index.html')



@app.route('/fetch_tweet') 
def get_tweets(): 
    try:
        trending_tweets = give_tweets()
        unique_id = str(uuid.uuid4())  
        print('i got tweets') 
        print(trending_tweets) 
        data_to_send = {
            'id': unique_id,
            'trends': trending_tweets,
            'ip_address': proxy,
            'timestamp':datetime.datetime.now().isoformat()
        }

        uri = os.getenv("MONGO_URI")  
        client = MongoClient(uri)
        db = client['Sample_d']
        trends = db['Sample_c']

        insert_doc = trends.insert_one(data_to_send)
        client.close()

        return jsonify({"message": "Trends Fetched Successfully!", "data": data_to_send})
    except Exception as e:
        return jsonify({"message": "Error fetching trends", "error": str(e)})




if __name__ == '__main__': 
    app.run(debug=True)