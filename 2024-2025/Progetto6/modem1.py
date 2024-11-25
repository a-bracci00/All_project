from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
import time

def ravvia_modem():
    
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    wait = WebDriverWait(driver, 4)
    try:
        driver.get("http://192.168.1.1/login.html")
        time.sleep(5)
    except:
        print('PROBLEMA NEL RAGGIUNGERE 192.168.1.1/login.html')
    try:
        input_password = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.row:nth-child(3) > div:nth-child(2) > input:nth-child(1)")))
        input_password.send_keys("admin")
        time.sleep(3)
    except:
        print('PROBLEMA CON L\'INSERIMENTO DELLA PASSWORD "ADMIN"')
    try:
        login_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#start")))
        login_button.click()
        time.sleep(3)
    except:
        print('PROBLEMA CON IL BOTTONE "START"')
    try:
        status_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#status-and-support > a:nth-child(1)")))#status-and-support > a:nth-child(1)
        status_button.click()
        time.sleep(3)
    except:
        print('PROBLEMA CON IL BOTTONE "STATUS"')
    try:
        restart0_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#lang906007")))#\34 1 > a:nth-child(1)
        restart0_button.click()
        time.sleep(3)
    except:
        print('PROBLEMA CON IL BOTTONE "RESTART0"')
    try:
        restart1_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#restartB")))#restartB#\34 1 
        restart1_button.click()
        time.sleep(5)
        print('MODEM RIAVVIATO')
    except:
        print('PROBLEMA CON IL BOTTONE "RESTART1"')#\34 1 > a:nth-child(1)
    time.sleep(5)
    driver.quit()

ravvia_modem()