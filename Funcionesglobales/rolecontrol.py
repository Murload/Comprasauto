import unittest
from os import remove
from selenium import webdriver
from time import sleep
import random  
from pyunitreport import HTMLTestRunner
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from Funcionesglobales.funciselenium import Funciones_Globales
from selenium.webdriver.common.action_chains import ActionChains



class Control(unittest.TestCase):
    def __init__(self,driver):
        self.driver=driver


    def managerequestContdAvailable(self):
        f = Funciones_Globales(self.driver)
        f.Click_Mixto("xpath", "(//div[@class='mat-list-item-content'][contains(.,'Solicitudes')])[4]", 1)
        f.Click_Mixto("xpath", "(//span[@class='mat-button-wrapper'][contains(.,'Gestionar')])[1]", 2)
        f.Click_Mixto("xpath", "(//div[contains(.,'Estado')])[17]", 2)
        f.Click_Mixto("xpath", "(//span[@class='mat-option-text'])[1]", 2)
        f.Texto_Mixto("xpath", "(//input[contains(@type,'text')])[2]", "Observación automatica disponible", 2)
        f.Click_NotScroll("//button[@type='submit'][contains(.,'Enviar')]")
        sleep(6)

    def managerequestContNotAvailable(self):
        f = Funciones_Globales(self.driver)
        sleep(3)
        f.Click_Mixto("xpath", "(//div[@class='mat-list-item-content'][contains(.,'Solicitudes')])[4]", 5)
        f.Click_Mixto("xpath", "(//span[@class='mat-button-wrapper'][contains(.,'Gestionar')])[1]", 3)
        f.Click_Mixto("xpath", "(//div[contains(.,'Estado')])[17]", 2)
        f.Click_Mixto("xpath", "(//span[@class='mat-option-text'])[2]", 2)
        f.Texto_Mixto("xpath", "(//input[contains(@type,'text')])[2]", "Observación automatica no disponible", 2)
        f.Click_NotScroll("//button[@type='submit'][contains(.,'Enviar')]")
        sleep(8)
        
    def entry_product(self):
        f = Funciones_Globales(self.driver)
        sleep(3)
        f.Click_Mixto("xpath", "(//div[@class='mat-list-item-content'][contains(.,'Solicitudes')])[4]", 4)
        f.Click_NotScroll("(//div[contains(.,'Ingresos')])[7]")
        f.Click_Mixto("xpath", "(//i[contains(@class,'fi-rr-edit')])[1]", 4)
        f.Click_Mixto("xpath", "(//div[contains(.,'Remisión')])[8]", 4)
        quantitysol = self.driver.find_element(By.XPATH, "(//input[@placeholder='Escribe la cantidad'])[1]")
        quantitysolc = quantitysol.get_attribute('value')
        f.Click_NotScroll("//div[@class='mat-checkbox-inner-container']")
        f.Texto_Mixto("xpath", "(//input[contains(@type,'number')])[2]", quantitysolc, 2)
        f.Texto_Mixto("xpath", "//input[@formcontrolname='observation']", "Observaciones remisión automatiza.", 2)
        f.Click_NotScroll("//button[contains(.,'Enviar')]")
        f.Click_NotScroll("//button[contains(.,'Aceptar')]")
        sleep(6)
