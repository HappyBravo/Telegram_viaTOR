from stem import Signal
import stem.process
from stem.control import Controller
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time, os, sys, subprocess

load_link = "https://web.telegram.org/k/"
user_dir = "E:/Downloads/Telegram_viaTOR/Chrome_data" # <--- ENTER FULL PATH ... IMPORTANT ⭕!  
tor_process = None
tor_pathh = r"D:\\C\\Program Files\\Tor\\Tor Browser\\Browser\\TorBrowser\\Tor\\tor.exe"
assert os.path.exists(tor_pathh)

SOCKET_PORT = '9150'
CONTROL_PORT = '9151'

def check_browser_status(driver):
    try:
        # CHECK IF BROWSER IS RUNNING
        driver.find_element(By.TAG_NAME, "body")
        return True  # BRROWSER IS OPEN 
    except Exception:
        return False  # BROWSER IS NOT OPEN 

def close_tor(tor_process, driver, controller):
    # Stop the Tor service
    print("Stopping Tor service.")
    print("Closing Tor circuit...")
    tor_process.terminate()  

    # Close Chrome driver
    print("Closing browser...")
    driver.quit() 
    controller.close()  # Clean up Tor circuit
    # sys.exit(0)

def start_tor_service():
    try:
        print("Starting tor process...")

        # reading material - "https://vincent.bernat.ch/en/blog/2014-tcp-time-wait-state-linux"
        tor_process = stem.process.launch_tor_with_config(
            tor_cmd = tor_pathh,
            config={
                'SocksPort': SOCKET_PORT,  # Set the socket port
                'ControlPort': CONTROL_PORT,  # Set the control port (for communication with Tor)
            },
            init_msg_handler=None,
            take_ownership=True,
            close_output=True,
            # timeout=60, # on Windows it does not work, and it will look like it is stuck in this step... ref : "https://stem.torproject.org/api/process.html"
        )
        print("Tor process started...")
        return tor_process
    #     print("Tor service started. Press Ctrl+C to stop.")

    except Exception as e:
        print(e)

if __name__ == "__main__":
    sproc = start_tor_service()

    # TRY 9051 OR 9151, WHICHEVER WORKS
    # with Controller.from_port(port=9051) as controller:
    # with Controller.from_port(port=9151) as controller:
    with Controller.from_port(port = int(CONTROL_PORT)) as controller:
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
        # chrome_options.add_argument("--proxy-server=socks5://127.0.0.1:9150")
        chrome_options.add_argument(f"--proxy-server=socks5://127.0.0.1:{SOCKET_PORT}")

        print("Browser (Chrome) options added...")
        
        driver = webdriver.Chrome(options=chrome_options)  # START CHROME

        try:
            # OPEN LINK
            driver.get(load_link)
            while True and check_browser_status(driver):
                time.sleep(2)

        except KeyboardInterrupt:
            print("Script interrupted by user.")

        finally:
            print("Closing chromedriver.")
            close_tor(tor_process=sproc,
                      driver=driver,
                      controller=controller)

    print("Clean up Tor circuit")
    controller.close()

    input("PRESS ENTER TO EXIT... ")