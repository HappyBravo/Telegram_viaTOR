from stem import Signal
from stem.control import Controller
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time, os

load_link = "https://web.telegram.org/k/"
user_dir = "C:/Users/Happy/Desktop/Telegram_viaTOR/Chrome_data" # <--- ENTER FULL PATH ... IMPORTANT !  

# TRY 9051 OR 9151, WHICHEVER WORKS
# with Controller.from_port(port=9051) as controller:
with Controller.from_port(port=9151) as controller:
    """
    FIRST OPEN TOR SERVICE 
    THEN CONNECT IT VIA PORT 9050 OR 9051
    RUN `netstat -ano | findstr :9051` TO SEE IF IT IS ACTIVE OR NOT
    """

    controller.authenticate()  # AUTHENTICATE WITH TOR 
    controller.signal(Signal.NEWNYM) # CREATE A NEW TOR CIRCUIT 

    print("Tor circuit started...")

    chrome_options = webdriver.ChromeOptions()

    chrome_options.add_argument(f'--user-data-dir={user_dir}')     # SET USER DATA DIRECTORY 
    chrome_options.add_argument('--profile-directory=Default')     # PROFILE DIRECTORY

    # Set up Chrome options to use Tor proxy

    # TRY 9050 OR 9150, WHICHEVER WORKS
    # chrome_options.add_argument("--proxy-server=socks5://127.0.0.1:9050") 
    chrome_options.add_argument("--proxy-server=socks5://127.0.0.1:9150")

    print("Browser (Chrome) options added...")
    
    driver = webdriver.Chrome(options=chrome_options)  # START CHROME

    try:
        # OPEN LINK
        driver.get(load_link)
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("Script interrupted by user.")
    finally:
        print("Closing chromedriver.")
        driver.quit()  # Close Chrome driver

print("Clean up Tor circuit")
controller.close()

input("PRESS ENTER TO EXIT... ")