# coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


try:
    driver = webdriver.Chrome()
    driver.get('http://10.4.1.86:8100/WebReport/ReportServer?op=fs_load&cmd=fs_signin&_=1525421398786')
    wait=WebDriverWait(driver,10)
    input_email = driver.find_element_by_class_name('fs-login-username')
    input_password = driver.find_element_by_class_name('fs-login-password')
    button = wait.until(EC.element_to_be_clickable((By.ID, 'fs-login-btn')))
    input_email.send_keys('09403')
    input_password.send_keys('Aa654321')
    # button.send_keys(Keys.ENTER)
    button.click()
finally:
    time.sleep(5)
    driver.close()

