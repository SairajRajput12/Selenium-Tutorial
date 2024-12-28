### Twitter Trends Fetcher

---

## **Project Overview**

This project fetches the latest trending topics from Twitter using **Selenium** and displays them dynamically on a Flask-powered web application. The data is stored in a **MongoDB** collection, including the trends, timestamp, and IP address used for the query. Users can fetch new trends by clicking a button on the web page.

---

## **Features**

- Fetches trending topics from Twitter using Selenium WebDriver.
- Stores fetched data in a MongoDB database.
- Displays trends dynamically on an interactive HTML page.
- Includes metadata like the unique query ID and IP address.
- Allows users to retrieve and display raw JSON records.

---

## **Tech Stack**

- **Backend:**
  - Python
  - Flask
- **Frontend:**
  - HTML, CSS, JavaScript
- **Database:**
  - MongoDB
- **Web Scraping:**
  - Selenium with Microsoft Edge WebDriver

---

## **Installation and Setup**

### **Prerequisites**
- Python 3.x
- MongoDB Server
- Microsoft Edge Browser
- Edge WebDriver
- Environment variables for user credentials and MongoDB URI.

### **Steps to Set Up**
1. Clone the repository:
   ```bash
   git clone Selenium-Tutorial
   cd <project-directory>
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up `.env` file with the following variables:
   ```env
   USER_NAME=<your-twitter-username>
   USER_PASSWORD=<your-twitter-password>
   USER_EMAIL=<your-twitter-email>
   MONGO_URI=<your-mongodb-uri>
   ```
4. Download and configure Microsoft Edge WebDriver:
   - Ensure the `msedgedriver.exe` file is in the project directory or set in the PATH.

5. Start MongoDB server if not already running.

6. Run the Flask app:
   ```bash
   python app.py
   ```

7. Open the web page in your browser:
   ```
   http://127.0.0.1:5000
   ```

---

## **Usage**

1. Navigate to the home page.
2. Click the "Fetch Trends" button to retrieve the latest trends.
3. View trends, metadata, and JSON data directly on the page.

---

## **Project Structure**

```
├── app.py                # Main application file
├── templates/
│   └── index.html        # HTML template for the frontend
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables
├── msedgedriver.exe      # Microsoft Edge WebDriver
```

---

## **Important Notes**

- **Proxy Configuration:**
  - Update the proxy settings in `app.py` if required.
- **Twitter OTP Prompt:**
  - If Twitter prompts for additional authentication (OTP), ensure email credentials are correct for auto-input.
- **MongoDB Connection:**
  - Ensure the MongoDB URI and collection names match your database setup.

---

## **Future Enhancements**

- Add OAuth2-based authentication for safer Twitter scraping.
- Implement error logging and monitoring.
- Deploy the application using a cloud provider (e.g., AWS, Heroku).
- Improve UI/UX with a modern JavaScript framework like React.

---


