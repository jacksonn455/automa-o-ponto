from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import os
import time

login = os.getenv('LOGIN_PONTO')
password = os.getenv('PASSWORD_PONTO')

browser = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
browser.get("https://pontosecullum4-01.secullum.com.br/ponto4web/821220936#login")
delay = 3
try:
    login_box  = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="login-form-campos"]/p[2]/input')))
    login_box.send_keys(login)
    login_box.submit()

    password_box  = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="login-form-campos"]/p[3]/input')))
    password_box.send_keys(password)
    password_box.submit()

    login_button  = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="login"]')))
    login_button.click()

    menu_button = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="itens-menu"]/li[2]/a')))
    menu_button.click()

    register_button = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="registrar"]')))
    register_button.click()
    time.sleep(3)

except TimeoutException:
    print ("Loading took too much time!")


