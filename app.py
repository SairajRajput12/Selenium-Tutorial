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
from flask import Flask, render_template_string


# Creting an instance of app 
app = Flask(__name__) 
# mongodb+srv://sairajrajput6:6vSCv00wWovlA3NU@sample.41iou.mongodb.net/



if __name__ == '__main__': 
    app.run(debug=True)