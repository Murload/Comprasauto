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

t = 2


class Coordinator(unittest.TestCase):
    def __init__(self,driver):
        self.driver=driver

    def manageaccept(self):
        # Llamado de funciones globales
        f = Funciones_Globales(self.driver)
        sleep(4)
        # Entra al modulo del rol coordinador
        f.Click_Mixto("xpath", "(//div[contains(.,'Solicitudes')])[9]", t)
        # Se da click en el icono de aceptar
        f.Click_NotScroll("(//i[contains(@class,'fi-rr-check')])[1]", t)
        # Diligencia el campo de observaciones 
        f.Texto_Mixto("xpath", "(//input[contains(@placeholder,'Observaciones')])[1]", "Observación aceptada coordinador automatica.", t)
        # Se da click en el botón de aceptar
        f.Click_NotScroll("//button[contains(.,'Aceptar')]", t)
    
    def managedecline(self):
        # Llamado de funciones globales
        f = Funciones_Globales(self.driver)
        sleep(4)
        # Entra al modulo del rol coordinador
        f.Click_Mixto("xpath", "(//div[contains(.,'Solicitudes')])[9]", t)
        # Se da click en el icono de rechazar
        f.Click_NotScroll("(//i[contains(@class,'fi-rr-cross')])[1]", t)
        # Diligencia el campo de observaciones 
        f.Texto_Mixto("xpath", "(//input[@placeholder='Motivo de rechazo'])[1]", "Observación rechazada coordinador automatica.", t)
        # Se da click en el botón de aceptar
        f.Click_NotScroll("//button[contains(.,'Aceptar')]", t)
        # Entra al modulo del rol Solicitante
        f.Click_Mixto("xpath", "(//div[contains(.,'Solicitudes')])[8]", t)


    