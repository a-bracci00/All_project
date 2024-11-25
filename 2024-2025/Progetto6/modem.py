from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
import time

def ravvia_modem():
    try:
        print('Riavvio modem in corso...')

        firefox_options = webdriver.FirefoxOptions()
        firefox_options.set_preference('browser.cache.disk.enable', False) #ok
        firefox_options.set_preference('browser.cache.memory.enable', False) #ok
        firefox_options.set_preference('network.prefetch-next', False) #ok
        firefox_options.set_preference('network.dns.disablePrefetch', True) #ok
        firefox_options.set_preference('browser.cache.offline.enable', False) #forse
        firefox_options.set_preference('network.http.use-cache', False) #ok
        firefox_options.add_argument('--headless')

        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)
        wait = WebDriverWait(driver, 20)
    except:
        try:
            print('Problema inizializzazione driver, pausa di 5 minuti')
            time.sleep(500)
            print('Riavvio modem in corso...')

            firefox_options = webdriver.FirefoxOptions()
            firefox_options.set_preference('browser.cache.disk.enable', False) #ok
            firefox_options.set_preference('browser.cache.memory.enable', False) #ok
            firefox_options.set_preference('network.prefetch-next', False) #ok
            firefox_options.set_preference('network.dns.disablePrefetch', True) #ok
            firefox_options.set_preference('browser.cache.offline.enable', False) #forse
            firefox_options.set_preference('network.http.use-cache', False) #ok
            firefox_options.add_argument('--headless')

            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)
            wait = WebDriverWait(driver, 20)
        except:
            print('PROBLEMA CONNESSIONE INTERNET, MODEM NON RIAVVIATO')

    try:
        driver.get("http://192.168.1.1")
        time.sleep(5)
    except:
        print('PROBLEMA NEL RAGGIUNGERE 192.168.1.1')
    try:
        input_password = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#srp_password")))
        input_password.send_keys("admin")
        time.sleep(3)
    except:
        print('PROBLEMA CON L\'INSERIMENTO DELLA PASSWORD "ADMIN"')
    try:
        login_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#sign-me-in")))
        login_button.click()
        time.sleep(3)
    except:
        print('PROBLEMA CON IL BOTTONE "SIGN-ME-IN"')

    try:
        old_pass_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#close-config")))
        old_pass_button.click()
        time.sleep(3)
    except:
        print('PROBLEMA CON IL BOTTONE "SIGN-ME-IN"')

    try:
        system_info = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#System\ Info")))#status-and-support > a:nth-child(1)
        system_info.click()
        time.sleep(3)
    except:
        print('PROBLEMA CON IL BOTTONE "SYSTEM INFO"')
    try:
        configuration_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#Configuration")))#\34 1 > a:nth-child(1)
        configuration_button.click()
        time.sleep(3)
    except:
        print('PROBLEMA CON IL BOTTONE "CONFIGURATION"')
    try:
        restart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#btn-system-reboot")))#restartB#\34 1 
        restart_button.click()
        time.sleep(3)
    except:
        print('PROBLEMA CON IL BOTTONE "RESTART"')#\34 1 > a:nth-child(1)
    try:
        restart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#ok")))#restartB#\34 1 
        restart_button.click()
        time.sleep(5)
        print('MODEM RIAVVIATO')
    except:
        print('PROBLEMA CON IL BOTTONE "OK"')#\34 1 > a:nth-child(1)
    try:
        time.sleep(5)
        driver.quit()
    except:
        pass

ravvia_modem()
