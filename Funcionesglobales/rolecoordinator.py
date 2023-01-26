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
        # Llamado de funciones globales
        f = Funciones_Globales(self.driver)
        sleep(3)
        # Entra al modulo del rol coordinador
        f.Click_Mixto("xpath", "(//div[@class='mat-list-item-content'][contains(.,'Solicitudes')])[3]", 6)
        # Se da click en el icono de aceptar
        f.Click_NotScroll("(//i[contains(@class,'fi-rr-check')])[1]", 2)
        # Diligencia el campo de observaciones 
        f.Texto_Mixto("xpath", "(//input[contains(@placeholder,'Observaciones')])[1]", "Observación aceptada coordinador automatica.", 3)
        # Se da click en el botón de aceptar
        f.Click_NotScroll("//button[contains(.,'Aceptar')]", 6)
    
    def managedecline(self):
        # Llamado de funciones globales
        f = Funciones_Globales(self.driver)
        # Entra al modulo del rol coordinador
        f.Click_Mixto("xpath", "(//div[@class='mat-list-item-content'][contains(.,'Solicitudes')])[3]", 6)
        # Se da click en el icono de rechazar
        f.Click_NotScroll("(//i[contains(@class,'fi-rr-cross')])[1]", 2)
        # Diligencia el campo de observaciones 
        f.Texto_Mixto("xpath", "(//input[@placeholder='Motivo de rechazo'])[1]", "Observación rechazada coordinador automatica.", 3)
        # Se da click en el botón de aceptar
        f.Click_NotScroll("//button[contains(.,'Aceptar')]", 6)
        # Entra al modulo del rol Solicitante
        f.Click_Mixto("xpath", "(//div[@class='mat-list-item-content'][contains(.,'Solicitudes')])[2]", 6)


    