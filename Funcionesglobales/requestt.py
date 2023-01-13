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


typeadquiran = random.randint(1, 2)
companyran = random.randint(1, 8)


class Request(unittest.TestCase):
    def __init__(self,driver):
        self.driver=driver

    def createnewrequest(self):
        f = Funciones_Globales(self.driver)
        sleep(5)
        f.Click_NotScroll("//button[@color='primary'][contains(.,'Crear nueva solicitud')]")
        sleep(3)
        f.Click_NotScroll("(//div[contains(.,'Tipo de adquisición *')])[7]")
        f.Click_NotScroll("(//span[contains(@class,'mat-option-text')])[{}]".format(typeadquiran))
        # f.Click_NotScroll("(//div[contains(.,'Categoría *')])[7]")
        f.Click_NotScroll("(//div[contains(.,'Empresa *')])[7]")
        selectcompany = self.driver.find_element(By.XPATH, "(//span[contains(@class,'mat-option-text')])[{}]".format(companyran))
        selectcompany.click()
        sleep(5)
        selectcompany.send_keys("Campañaprueba", Keys.TAB, "SolicitudAutomatica", Keys.TAB,"Detalles automatico", 
        Keys.TAB, "Detalles automaticos", Keys.TAB, companyran)