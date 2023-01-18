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
from random import choice


typeadquiran = random.randint(1, 2)
companyran = random.randint(1, 8)
categoryran = random.randint(1, 4)
name = random.randint(1, 999999)

productos = ["Escritorios", "Sillas", "Sillas ergónomica", "Mesedoras", "Descansa Pies ", "Pad mouse","Mesas","Lamparas","Teclados","Mouse","Pantallas","Audifonos",
"Cpu","Portatil","Impresora","Emgrapadora","Organizadores","Telefono","Archiveros","Toner","Mesa Laptop","Papelera","Porta Laptop","Carpetas","Alfombrilla para PC","Disco duro para laptop","Adaptador multiuso PC","Organizador de cables",
"Soporte de celulares"," Portalápices"]

productos_alea = choice(productos)

class Applicant(unittest.TestCase):
    def __init__(self,driver):
        self.driver=driver


    def product(self): 
        productos = ["Escritorios", "Sillas", "Sillas ergónomica", "Mesedoras", "Descansa Pies ", "Pad mouse","Mesas","Lamparas","Teclados","Mouse","Pantallas","Audifonos",
        "Cpu","Portatil","Impresora","Emgrapadora","Organizadores","Telefono","Archiveros","Toner","Mesa Laptop","Papelera","Porta Laptop","Carpetas","Alfombrilla para PC","Disco duro para laptop","Adaptador multiuso PC","Organizador de cables",
        "Soporte de celulares"," Portalápices"]
        productos_alea = choice(productos)
        return productos_alea
       
    def createnewrequest(self):
        f = Funciones_Globales(self.driver)
        sleep(3)
        f.Click_NotScroll("//button[@color='primary'][contains(.,'Crear nueva solicitud')]")
        sleep(3)
        f.Click_NotScroll("(//div[contains(.,'Tipo de adquisición *')])[7]")
        f.Click_NotScroll("(//span[contains(@class,'mat-option-text')])[{}]".format(typeadquiran))
        sleep(3)
        f.Click_NotScroll("(//div[contains(.,'Categoría *')])[7]")
        f.Click_Mixto("xpath", "(//span[contains(@class,'mat-option-text')])[1]".format(categoryran), 2)
        f.Click_NotScroll("(//div[contains(.,'Empresa *')])[7]")
        f.Click_Mixto("xpath","(//mat-option[contains(@role,'option')])[{}]".format(companyran), 2)
        campaingauto = self.driver.find_element(By.XPATH, "(//input[contains(@type,'text')])[4]")
        campaingauto.click()
        campaingauto.send_keys("CampañapruebaAutomatica", Keys.TAB, str(productos_alea)+" {}".format(name), Keys.TAB,"Detalles automatico", 
        Keys.TAB, "16", "01", "2023", Keys.TAB, "Observación de  ejecución automatica", Keys.TAB, str(productos_alea) ,Keys.TAB, companyran)
        sleep(3)
        f.Click_NotScroll("//button[@type='submit'][contains(.,'Guardar')]")
        sleep(2)
        self.driver.refresh()
        
