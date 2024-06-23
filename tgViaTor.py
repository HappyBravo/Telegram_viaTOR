from stem import Signal
import stem.process
from stem.control import Controller
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time, os, sys, subprocess

load_link = "https://web.telegram.org/k/"
user_dir = "C:/Users/Happy/Desktop/Telegram_viaTOR/Chrome_data" # <--- ENTER FULL PATH ... IMPORTANT !  
tor_process = None
tor_pathh = r"D:\\C\\Program Files\\Tor\\Tor Browser\\Browser\\TorBrowser\\Tor\\tor.exe"
assert os.path.exists(tor_pathh)

def close_tor(tor_process, driver, controller):
    # except KeyboardInterrupt:
    print("Keyboard interruption detected. Stopping Tor service.")
    tor_process.terminate()  # Stop the Tor service

    print("Closing Tor circuit...")
    driver.quit()  # Close Chrome driver
    controller.close()  # Clean up Tor circuit
    # sys.exit(0)

def start_tor_service():
    try:
        print("Starting tor process...")

        # reading material - "https://vincent.bernat.ch/en/blog/2014-tcp-time-wait-state-linux"
        tor_process = stem.process.launch_tor_with_config(
            tor_cmd = tor_pathh,
            config={
                'SocksPort': '9150',  # Set the port to 9151
                'ControlPort': '9151',  # Set the control port (for communication with Tor)
            },
            init_msg_handler=None,
            take_ownership=True,
            close_output=True,
            # timeout=60, # on Windows it does not work, and it will look like it is stuck in this step... ref : "https://stem.torproject.org/api/process.html"
        )
        print("Tor process started...")
        return tor_process
    #     print("Tor service started. Press Ctrl+C to stop.")
    #     tor_process.wait()  # Wait for keyboard interruption
    except Exception as e:
        print(e)

    # except KeyboardInterrupt:
    #     print("Keyboard interruption detected. Stopping Tor service.")
    #     tor_process.terminate()  # Stop the Tor service
    #     sys.exit(0)  # Exit the Python program

# def do_this():
    

if __name__ == "__main__":
    sproc = start_tor_service()

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
            # print("Script interrupted by user.")
            close_tor(tor_process=sproc,
                      driver=driver,
                      controller=controller)
        finally:
            print("Closing chromedriver.")
            driver.quit()  # Close Chrome driver

    print("Clean up Tor circuit")
    controller.close()

    input("PRESS ENTER TO EXIT... ")