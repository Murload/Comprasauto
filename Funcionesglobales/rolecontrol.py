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


t = 2

class Control(unittest.TestCase):
    def __init__(self,driver):
        self.driver=driver


    def managerequestContdAvailable(self):
        # Llamado de funciones globales
        f = Funciones_Globales(self.driver)
        sleep(4)
        # Entra al modulo del rol control
        f.Click_Mixto("xpath", "(//div[@class='mat-list-item-content'][contains(.,'Solicitudes')])[4]", t)
        # Se da click en el botón de gestionar del la solicitud más reciente
        f.Click_Mixto("xpath", "(//span[@class='mat-button-wrapper'][contains(.,'Gestionar')])[1]", t)
        # le da click al seleccionable de estado
        f.Click_Mixto("xpath", "(//div[contains(.,'Estado')])[17]", t)
        # Selecciona la opcion de Disponible
        f.Click_Mixto("xpath", "(//span[@class='mat-option-text'])[1]", t)
        # Diligencia el campo de observaciones 
        f.Texto_Mixto("xpath", "(//input[contains(@type,'text')])[2]", "Observación automatica disponible", t)
        # Se da click en el botón de Enviar
        f.Click_NotScroll("//button[@type='submit'][contains(.,'Enviar')]", t)
        sleep(5)

    def managerequestContNotAvailable(self):
        # Llamado de funciones globales
        f = Funciones_Globales(self.driver)
        sleep(6)
        # Entra al modulo del rol control
        f.Click_Mixto("xpath", "(//div[contains(.,'Solicitudes')])[10]", t)
        # Se da click en el botón de gestionar del la solicitud más reciente
        f.Click_Mixto("xpath", "(//span[@class='mat-button-wrapper'][contains(.,'Gestionar')])[1]", t)
        # le da click al seleccionable de estado
        f.Click_Mixto("xpath", "(//div[contains(.,'Estado')])[17]", t)
        # Selecciona la opcion de No Disponible
        f.Click_Mixto("xpath", "(//span[@class='mat-option-text'])[2]", t)
        # Diligencia el campo de observaciones 
        f.Texto_Mixto("xpath", "(//input[contains(@type,'text')])[2]", "Observación automatica no disponible", t)
        # Se da click en el botón de Enviar
        f.Click_NotScroll("//button[@type='submit'][contains(.,'Enviar')]", t)
        
    def entry_product(self):
        # Llamado de funciones globales
        f = Funciones_Globales(self.driver)
        sleep(4)
        # Entra al modulo del rol control
        f.Click_Mixto("xpath", "(//div[contains(.,'Solicitudes')])[10]", 4)
        # Se da click en el botón tap de Ingresos
        f.Click_NotScroll("(//div[contains(.,'Ingresos')])[7]",1 )
        # Se da click en el botón icono de Editar
        f.Click_Mixto("xpath", "(//i[contains(@class,'fi-rr-edit')])[1]", 4)
        # Se da click en el botón tap de Remision
        f.Click_Mixto("xpath", "(//div[contains(.,'Remisión')])[8]", 4)
        # Se busca el campo el cual se quiere tomar el valor
        quantitysol = self.driver.find_element(By.XPATH, "(//input[@placeholder='Escribe la cantidad'])[1]")
        # Se toma el valor del campo
        quantitysolc = quantitysol.get_attribute('value')
        # Da click en el checklist
        f.Click_NotScroll("//div[@class='mat-checkbox-inner-container']", 1)
        # Diligencia el campo de Cantidad recibida
        f.Texto_Mixto("xpath", "(//input[contains(@type,'number')])[2]", quantitysolc, 2)
        # Diligencia el campo de Observaciones
        f.Texto_Mixto("xpath", "//input[@formcontrolname='observation']", "Observaciones remisión automatiza.", 2)
        # Se da click en el botón de Enviar
        f.Click_NotScroll("//button[contains(.,'Enviar')]", 1)
        # Se da click en el botón de Aceptar
        f.Click_NotScroll("//button[contains(.,'Aceptar')]", 6)
        sleep(10)

    def entry_product_frag(self):
        # Llamado de funciones globales
        f = Funciones_Globales(self.driver)
        sleep(4)
        # Entra al modulo del rol control
        f.Click_Mixto("xpath", "(//div[contains(.,'Solicitudes')])[10]", 7)
        # Se da click en el botón tap de Ingresos
        f.Click_NotScroll("(//div[contains(.,'Ingresos')])[7]",1)
        # Se hace un cantador para el for de acontinuación
        # El for hace que se realice la accion 2 veces que en este caso es la remision de una Orden fragmentada
        for i in range(1,3):
            # Dar click en la obligacion para que se despliegue el acordeon
            f.Click_NotScroll("(//td[@role='gridcell'])[2]", 2)
            # Se da click en el icono de editar añadiendo el contador para que por cada recorrida tome un valor y se puedan tomar los diferentes localizadores
            f.Click_NotScroll("(//i[contains(@class,'fi-rr-edit')])[1]",2)
            # Se da click en el botón tap de Remision
            f.Click_Mixto("xpath", "(//div[contains(.,'Remisión')])[8]", 4)
            # Da click en el checklist
            f.Click_NotScroll("//div[@class='mat-checkbox-inner-container']", 1)
            # Se busca el campo el cual se quiere tomar el valor
            quantitysol = self.driver.find_element(By.XPATH, "(//input[@placeholder='Escribe la cantidad'])[1]")
            # Se toma el valor del campo
            quantitysolc = quantitysol.get_attribute('value')
            # Diligencia el campo de Cantidad recibida
            f.Texto_Mixto("xpath", "(//input[contains(@type,'number')])[2]", quantitysolc, 2)
            # Diligencia el campo de Observaciones
            f.Texto_Mixto("xpath", "//input[@formcontrolname='observation']", "Observaciones remisión automatiza.", 2)
            # Se da click en el botón de Enviar
            f.Click_NotScroll("//button[contains(.,'Enviar')]",1)
            # Se da click en el botón de Aceptar
            f.Click_NotScroll("//button[contains(.,'Aceptar')]",1)
            sleep(6)
        sleep(5)
    
        