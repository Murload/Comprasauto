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


class Control(unittest.TestCase):
    def __init__(self,driver):
        self.driver=driver


    def managerequestCoordAvailable(self):
        f = Funciones_Globales(self.driver)
        f.Click_Mixto("xpath", "(//div[@class='mat-list-item-content'][contains(.,'Solicitudes')])[4]", 1)
        f.Click_Mixto("xpath", "(//span[@class='mat-button-wrapper'][contains(.,'Gestionar')])[1]", 2)
        f.Click_Mixto("xpath", "(//div[contains(.,'Estado')])[17]", 2)
        f.Click_Mixto("xpath", "(//span[@class='mat-option-text'])[1]", 2)
        f.Texto_Mixto("xpath", "(//input[contains(@type,'text')])[2]", "Observación automatica disponible", 2)
        f.Click_NotScroll("//button[@type='submit'][contains(.,'Enviar')]")
        sleep(6)

    def managerequestCoordNotAvailable(self):
        f = Funciones_Globales(self.driver)
        sleep(3)
        f.Click_Mixto("xpath", "(//div[@class='mat-list-item-content'][contains(.,'Solicitudes')])[4]", 1)
        sleep(4)
        f.Click_Mixto("xpath", "(//span[@class='mat-button-wrapper'][contains(.,'Gestionar')])[1]", 2)
        f.Click_Mixto("xpath", "(//div[contains(.,'Estado')])[17]", 2)
        f.Click_Mixto("xpath", "(//span[@class='mat-option-text'])[2]", 2)
        f.Texto_Mixto("xpath", "(//input[contains(@type,'text')])[2]", "Observación automatica no disponible", 2)
        f.Click_NotScroll("//button[@type='submit'][contains(.,'Enviar')]")
        sleep(6)
        
