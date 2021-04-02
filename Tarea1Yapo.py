import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def abrirPagina():
  path = "D:\Reespaldo\Guias y documentos\Criptografia\chromedriver.exe"
  driver = webdriver.Chrome(path)
  driver.get("https://yapo.cl/")
  time.sleep(3)
  return driver

def crearCuenta():
  driver = abrirPagina()
  driver.get("https://www2.yapo.cl/cuenta/form/0")
  time.sleep(2)
  pyautogui.press('tab', 1)
  pyautogui.press('left') 
  driver.find_element_by_id("account_name").send_keys("Matias Gutierrez")
  pyautogui.press('tab', 1)  
  driver.find_element_by_id("account_commune").click()
  pyautogui.press('q')  
  pyautogui.press('enter')
  driver.find_element_by_id("phone").send_keys("87057173")
  driver.find_element_by_id("account_email").send_keys("matiasfgutierrezgonzalez@gmail.com")
  driver.find_element_by_id("account_password").send_keys("12345678")
  driver.find_element_by_id("account_password_verify").send_keys("12345678")
  driver.find_element_by_id("label_accept_conditions").click()
  time.sleep(3)
  driver.find_element_by_id("edit_profile_btn").click()
  time.sleep(3)


def iniciarSesion():
  driver = abrirPagina()
  time.sleep(2)
  driver.find_element_by_id("login-account-link").click()
  pyautogui.write("matiasfgutierrezgonzalez")
  pyautogui.hotkey('altright', 'q')
  pyautogui.write("gmail.com")
  pyautogui.press('tab', 1)
  pyautogui.write("12345678")
  time.sleep(2)
  pyautogui.press('tab', 1)
  pyautogui.press('enter')
  time.sleep(2)


def restablecerPass():
  driver = abrirPagina()
  time.sleep(2)
  driver.find_element_by_id("login-account-link").click()
  time.sleep(2)
  driver.get("https://www2.yapo.cl/reset_password?op=1")
  driver.find_element_by_id("email").send_keys("matiasfgutierrezgonzalez@gmail.com")
  time.sleep(2)

def modificarPass():
  driver = abrirPagina()
  time.sleep(2)
  driver.find_element_by_id("login-account-link").click()
  pyautogui.write("matiasfgutierrezgonzalez")
  pyautogui.hotkey('altright', 'q')
  pyautogui.write("gmail.com")
  pyautogui.press('tab', 1)
  pyautogui.write("12345678")
  time.sleep(2)
  pyautogui.press('tab', 1)
  pyautogui.press('enter')
  time.sleep(2)

  driver.get("https://www2.yapo.cl/cuenta/edit")
  time.sleep(2)

  for x in range(11):
    pyautogui.press('tab', 1)
    x += 1
  pyautogui.press('enter')
  time.sleep(1)
  driver.find_element_by_id("account_password").send_keys("87654321")
  driver.find_element_by_id("account_password_verify").send_keys("87654321")
  time.sleep(2)
  pyautogui.press('tab', 1)
  pyautogui.press('tab', 1)
  time.sleep(2)
  pyautogui.press('enter')

modificarPass()