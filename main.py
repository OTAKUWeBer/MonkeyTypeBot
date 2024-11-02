from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import subprocess
from getpass import getpass
import time
import os

# Specify the browser to use: "Firefox" or "Chrome"
browser = "Firefox"


# Clears the screen before start up
def clear_screen():
    if os.name == 'nt':  # For Windows
        subprocess.run(['cls'], shell=True)
    else:  # For Unix/Linux/Mac
        subprocess.run(['clear'])
clear_screen()

def initialize_driver():
    if browser == "Firefox":
        return webdriver.Firefox()
    elif browser == "Chrome":
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)  # Prevent Chrome from closing
        return webdriver.Chrome(options=chrome_options)
    else:
        raise ValueError("Unsupported browser specified. Use 'Firefox' or 'Chrome'.") # You have to remove "executable_path=path" line if you use linux

def login():
    clear_screen()
    print("------------Note----------------")
    print("1. Once on the practice page, switch to 'Text Mode' for better accuracy. 'Time Mode' has unlimited words, so it might stop after typing a certain number.")
    print("2. Please note that the bot gets detected around 200 WPM, so it's recommended to keep the speed lower than that.\n")
    print("Please enter your email and password to log in.")

    email = input("Enter Email: ")
    password = getpass("Enter Password: ")
    
    while True:
        try:
            speed = float(input("Enter the time between typing each character (e.g., 0.1 for around 100 WPM): "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    while True:
        try:
            switch = int(input("Enter seconds to change the mode (0 for no change): "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.") 
    
    driver = initialize_driver()

    # Go to the website
    driver.get("https://monkeytype.com/login")

    # Accept Cookies
    try:
        accept_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'accept all')]"))
        )
        accept_button.click()
    except Exception as e:
        print("Could not find or click the accept all button:", e)

    # Wait for the email input to be present and fill it
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "current-email"))
    )
    email_input.send_keys(email)

    # Wait for the password input to be present and fill it
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "current-password"))
    )
    password_input.send_keys(password)
    
    # Wait for the login button to be present and click it
    driver.execute_script("window.scrollBy(0, 1000);")
    time.sleep(0.5)
    submit = driver.find_element(By.CLASS_NAME, "signIn")
    submit.click()
    
    time.sleep(10)  # Time to load the page
    
    # Find and click the start test button
    start_test = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "startTestButton"))
    )
    start_test.click()
    
    time.sleep(switch)  # Time to change the mode
    
    # Wait until the element with ID "words" is present
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "words"))
    )
    # Get the text from the element with ID "words"
    texts = driver.find_element(By.ID, "words").text.replace("\n", " ")
    input_field = driver.find_element(By.ID, "wordsInput")
    for alphabet in texts:
        input_field.send_keys(alphabet)
        time.sleep(speed)

def without_login():
    clear_screen()
    print("------------Note----------------")
    print("1. Once on the practice page, switch to 'Text Mode' for better accuracy. 'Time Mode' has unlimited words, so it might stop after typing a certain number.")
    print("2. Please note that the bot gets detected around 200 WPM, so it's recommended to keep the speed lower than that.\n")
    
    while True:
        try:
            speed = float(input("Enter the time between typing each character (e.g., 0.1 for around 100 WPM): "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    while True:
        try:
            switch = int(input("Enter seconds to change the mode (0 for no change): "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")      
              
    driver = initialize_driver()

    # Go to the website
    driver.get("https://monkeytype.com/")
    
    # Accept Cookies
    try:
        accept_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'accept all')]"))
        )
        accept_button.click()
    except Exception as e:
        print("Could not find or click the accept all button:", e)
    
    time.sleep(switch)  # Time to change the mode
    
    # Wait until the element with ID "words" is present
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "words"))
    )

    # Get the text from the element with ID "words"
    texts = driver.find_element(By.ID, "words").text.replace("\n", " ")
    input_field = driver.find_element(By.ID, "wordsInput")

    for alphabet in texts:
        input_field.send_keys(alphabet)
        time.sleep(speed)
        

def choose():
    print("Choose your login method:")
    print("1. Login with your email and password.")
    print("2. Start without login.")
    
    while True:
        try:
            choice = int(input("Enter your choice (1/2): "))
            if choice in [1, 2]:
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter an integer (1 or 2).")

    if choice == 1:
        login()
    elif choice == 2:
        without_login()
    else:
        print("Invalid choice. Exiting...")

if __name__ == "__main__":
    choose()
