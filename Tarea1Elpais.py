import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def abrirPagina():
  path = "D:\Reespaldo\Guias y documentos\Criptografia\chromedriver.exe"
  driver = webdriver.Chrome(path)
  driver.get("https://elpais.com/")
  time.sleep(3)
  return driver

def crearCuenta():
  driver = abrirPagina()
  driver.get("https://elpais.com/subscriptions/#/register?prod=REG&o=CABEP&backURL=https%3A%2F%2Felpais.com%2Famerica%2F")
  time.sleep(2)
  driver.find_element_by_id("subsEmail").send_keys("matiasfgutierrezgonzalez@gmail.com")
  driver.find_element_by_id("subsPassword").send_keys("12345678")
  driver.find_element_by_id("subsConfirmPassword").send_keys("12345678")  
  driver.find_element_by_link_text("Dia")
  time.sleep(3)

def iniciarSesion():
  pass

def restablecerPass():
  pass

def modificarPass():
  pass

crearCuenta()