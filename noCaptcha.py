from selenium import webdriver
import os
import json
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

current_dir = os.getcwd()
noCaptcha_folder = os.path.join(current_dir, "noCaptcha")

## Initialize Selenium
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--load-extension=" + noCaptcha_folder)
chromedriver_path = current_dir + "\\chromedriver.exe"
driver = webdriver.Chrome(options=options, executable_path=chromedriver_path)
 

def main():
    driver.get("https://google.com")
    #proxy = '10.124.0.242:1080'   
    #options.add_argument('--proxy-server=socks5://' + proxy)


def checkRecaptcha(driver):
    try:
        driver.find_elements(By.CLASS_NAME, "recaptcha-checkbox goog-inline-block recaptcha-checkbox-unchecked rc-anchor-checkbox")
        ## FOUND CAPTCHA
        while True:
            try: ##Checks for "Your computer or network may be sending automated queries" error.
                driver.find_elements(By.CLASS_NAME, "rc-doscaptcha-body-text")
                print("ERROR: Captcha automation detected. It returns Your computer or network may be sending automated queries error. ")
                break
            except NoSuchElementException:
                pass
            ## If no error then tries to find checkmark.
            try:
                driver.find_elements(By.CLASS_NAME, "recaptcha-checkbox goog-inline-block recaptcha-checkbox-unchecked rc-anchor-checkbox recaptcha-checkbox-checked")
                print("Solved!")
            except NoSuchElementException:
                print("Captcha still solving..")
                time.slep(5)
                pass
    except:
        print("No recaptcha detected.")
        pass


if __name__ == '__main__':
    main()



