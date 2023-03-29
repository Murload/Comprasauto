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



item = random.randint(1, 15)
t = 1
#  Variable para el campo de tipo de adquisicion aleatorio
typeadquiran = random.randint(1, 2)
#  Variable para el campo de tipo de adquisicion aleatorio
companyran = random.randint(1, 8)
# Variable para el campo de Categoria aleatorio
categoryran = random.randint(1, 4)
#  Variable para número de el titulo de solicitud aleatorio
name = random.randint(1, 999999)

# Lista de productos para el nombre de la solicitud 
productos = ["Escritorios", "Sillas", "Sillas ergónomica", "Mesedoras", "Descansa Pies ", "Pad mouse","Mesas","Lamparas","Teclados","Mouse","Pantallas","Audifonos",
"Cpu","Portatil","Impresora","Emgrapadora","Organizadores","Telefono","Archiveros","Toner","Mesa Laptop","Papelera","Porta Laptop","Carpetas","Alfombrilla para PC","Disco duro para laptop","Adaptador multiuso PC","Organizador de cables",
"Soporte de celulares"," Portalápices"]

# Selecciona de la lista pasada un producto aleatorio
productos_alea = choice(productos)

class Applicant(unittest.TestCase):
    def __init__(self,driver):
        self.driver=driver
       
    def createnewrequest(self):
        # Llamado de funciones globales
        f = Funciones_Globales(self.driver)
        sleep(4)
        # Entra al modulo del rol solicitante
        f.Click_Mixto("xpath", "(//div[contains(.,'Solicitudes')])[8]", t)
        # Entra le da click al botón de crear nueva solicitud
        f.Click_NotScroll("//button[@color='primary'][contains(.,'Crear nueva solicitud')]", t)
        # le da click al seleccionable de tipo de adquisicion
        f.Click_NotScroll("(//div[contains(.,'Tipo de adquisición *')])[7]", t)
        # # Selecciona un tipo de adquisicion aleatoria
        f.Click_NotScroll("(//span[contains(@class,'mat-option-text')])[{}]".format(typeadquiran),t )
        # le da click al seleccionable de categoria
        f.Click_NotScroll("(//div[contains(.,'Categoría *')])[7]",t)
        # Selecciona una categoria aleatoria
        f.Click_Mixto("xpath", "(//span[contains(@class,'mat-option-text')])[1]".format(categoryran), t)
        # le da click al seleccionable de empresas
        f.Click_NotScroll("(//div[contains(.,'Empresa *')])[7]", t)
        # Selecciona una empresa aleatoria
        f.Click_Mixto("xpath","(//mat-option[contains(@role,'option')])[{}]".format(companyran), t)
        # Se encuentra campo de nombre de campaña y se envian diligencian nombre de campaña, titulo de solicitud, detalle, fecha de ejecucion, observacion 
        # productos y cantidad
        campaingauto = self.driver.find_element(By.XPATH, "(//input[contains(@type,'text')])[4]")
        campaingauto.click()
        campaingauto.send_keys("CampañapruebaAutomatica", Keys.TAB, str(productos_alea)+" {}".format(name), Keys.TAB,"Detalles automaticoqwer", 
        Keys.TAB, "16", "01", "2023", Keys.TAB, "Observación de  ejecución automatica", Keys.TAB, str(productos_alea) ,Keys.TAB, item)
        sleep(3)
        # Le da click a guardar la solicitud
        f.Click_NotScroll("//button[@type='submit'][contains(.,'Guardar')]", 4)
        # Se le da un refrescar a la pagina
        # self.driver.refresh()
        
        
