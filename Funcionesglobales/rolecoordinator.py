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

class Coordinator(unittest.TestCase):
    def __init__(self,driver):
        self.driver=driver

    def manageaccept(self):
        f = Funciones_Globales(self.driver)
        #Aqui el coordinador acepta o rechaza la solicitudes
        f.Click_Mixto("xpath", "(//div[@class='mat-list-item-content'][contains(.,'Solicitudes')])[3]", 4)
        f.Click_NotScroll("(//i[contains(@class,'fi-rr-check')])[1]")
        sleep(2) 
        # f.Click_NotScroll("(//button[contains(@type,'button')])[7]")
        f.Texto_Mixto("xpath", "(//input[contains(@placeholder,'Observaciones')])[1]", "Observación aceptada coordinador automatica.", 3)
        f.Click_NotScroll("//button[contains(.,'Aceptar')]")
        sleep(6)
    
    def managedecline(self):
        f = Funciones_Globales(self.driver)
        #Aqui el coordinador rechaza la solicitudes
        f.Click_Mixto("xpath", "(//div[@class='mat-list-item-content'][contains(.,'Solicitudes')])[3]", 4)
        f.Click_NotScroll("(//i[contains(@class,'fi-rr-cross')])[1]")
        sleep(2)
        f.Texto_Mixto("xpath", "(//input[@placeholder='Motivo de rechazo'])[1]", "Observación rechazada coordinador automatica.", 3)
        f.Click_NotScroll("//button[contains(.,'Aceptar')]")
        sleep(6)

    