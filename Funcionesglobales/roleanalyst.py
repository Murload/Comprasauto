import unittest
from os import remove
from selenium import webdriver
from time import sleep
import random  
from pyunitreport import HTMLTestRunner
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from Funcionesglobales.funciselenium import Funciones_Globales
from Funcionesglobales.roleapplicant import Applicant

# Variable para poner precio de la cotizacion aleatorio
pricecot = random.randint(100000, 999999)

companyran = random.randint(1, 99)
# Variable para poner IVA aleatorio
iva = random.randint(1, 5)
# Variable para poner metodo de pago aleatorio

methodpay = random.randint(1, 4)

class Analyst(unittest.TestCase):
    def __init__(self,driver):
        self.driver=driver

    def managerequestAnaAccept(self):
        # Llamado de funciones globales
        f = Funciones_Globales(self.driver)
        # Entra al modulo del rol analista
        f.Click_Mixto("xpath", "(//div[@class='mat-list-item-content'][contains(.,'Solicitudes')])[1]", 5)
        # Se da click en el botón de gestionar
        f.Click_Mixto("xpath", "(//span[contains(.,'Gestionar')])[1]", 1)
        # le da click al seleccionable de Estado
        f.Click_Mixto("xpath", "(//div[contains(.,'Estado')])[17]", 3)
        # le da click al seleccionable de Estado  
        f.Click_NotScroll("(//span[@class='mat-option-text'])[1]", 1)
        # le da click al campo de cotización 
        f.Click_Mixto("xpath", "(//div[contains(.,'Cotización 1')])[9]", 2)
        # Se da click en el icono del clip para cargar archivo
        f.Click_NotScroll("/html/body/div[2]/div[2]/div/mat-dialog-container/app-procesar-solicitud/div/form/mat-dialog-content/div[9]/div[2]/div[1]/mat-form-field/div/div[1]/div[2]/i",3)
        #Se debe enviar la ruta donde se encuentra el archivo
        # En este caso se debe modifcar el nombre del usuario en la ruta
        f.uploadfile("C:\\Users\\aleon\\Desktop\\Comprasauto\\filesupload\\cotizacion1.pdf")
        sleep(2)
        # Diligencia el campo de precio 
        f.Texto_Mixto("xpath", "(//input[@aria-required='true'])[2]", pricecot ,1)
        # Diligencia el campo de observaciones 
        f.Texto_Mixto("xpath", "(//input[@type='text'])[5]", "Observación cotizaciones automaticas." ,3)
        # Se da click en el botón de Enviar
        f.Click_NotScroll("//button[contains(.,'Enviar')]", 1)
        # Se da click en el botón de Aceptar
        f.Click_NotScroll("//button[contains(.,'Aceptar')]", 6)

    def managerequestAnaback(self):
        # Llamado de funciones globales
        f = Funciones_Globales(self.driver)
        # Entra al modulo del rol analista
        f.Click_Mixto("xpath", "(//div[@class='mat-list-item-content'][contains(.,'Solicitudes')])[1]", 1)
        # Se da click en el botón de gestionar
        f.Click_Mixto("xpath", "(//span[contains(.,'Gestionar')])[1]", 1)
        # le da click al seleccionable de Estado
        f.Click_Mixto("xpath", "(//div[contains(.,'Estado')])[17]", 3)
        # Selecciona la opcion de Devuelta
        f.Click_NotScroll("(//span[@class='mat-option-text'])[2]", 1)
        # Diligencia el campo de observaciones 
        f.Texto_Mixto("xpath", "(//input[@type='text'])[2]", "Observación devuelta automaticamente", 2)
        # Se da click en el botón de guardar
        f.Click_NotScroll("//button[contains(.,'Guardar')]", 1)
        # Se da click en el botón de Aceptar
        f.Click_NotScroll("//button[contains(.,'Aceptar')]", 4)

    def order(self):
        # Llamado de funciones globales
        f = Funciones_Globales(self.driver)
        sleep(4)
        # Entra al modulo del rol analista
        f.Click_Mixto("xpath", "(//div[@class='mat-list-item-content'][contains(.,'Solicitudes')])[1]", 4)
        # Se da click en el botón de orden
        f.Click_Mixto("xpath", "(//span[contains(.,'Orden')])[1]", 2)
        # Diligencia el campo de NIT proveedor y le da enter
        f.Textkeyenenter("(//input[@aria-invalid='false'])[2]")
        sleep(1)
        # Se da click en el botón de Generar orden
        f.Click_NotScroll("//button[contains(.,'Generar Orden')]", 4)
        # Se da click en el botón de siguiente
        f.Click_Mixto("xpath", "(//button[contains(.,'Siguiente')])[1]", 6)
        # Diligencia el campo de descripción, especificación, Cantidad, tipo de moneda, valor unitario 
        textdetails= self.driver.find_element(By.XPATH, "(//input[contains(@type,'text')])[1]")
        textdetails.send_keys("Producto", Keys.TAB ,"Especificación", Keys.TAB, companyran, Keys.TAB,
        Keys.ARROW_RIGHT, Keys.TAB, pricecot)
        # le da click al seleccionable de Iva
        f.Click_NotScroll("(//div[contains(.,'IVA')])[12]",1)
        # Selecciona la opcion de iva aleatoriamente
        f.Click_NotScroll("(//span[@class='mat-option-text'])[{}]".format(iva), 3)
        # Se da click en el botón de siguiente
        f.Click_Mixto("xpath", "(//button[@type='button'])[8]", 5)
         # Diligencia el campo de descripción
        f.Texto_Mixto("xpath", "(//input[@type='text'])[3]", "Observación de Orden de compra automatica.",2)
         # Diligencia el campo de Descuento
        f.Texto_Mixto("xpath", "(//input[@aria-required='true'])[6]", "0",5)
         # Diligencia el campo de Fecha de entrega
        f.Texto_Mixto("xpath", "//input[@type='date']", "20012023",2)
        # le da click al seleccionable de Método de pago
        f.Click_NotScroll("(//div[contains(.,'Método de pago')])[9]", 1)
         # Selecciona la opcion de Método de pago aleatoriamente
        f.Click_NotScroll("(//span[@class='mat-option-text'])[{}]".format(methodpay), 3)
        # le da click al seleccionable de Condicion de pago
        f.Click_NotScroll("(//div[contains(.,'Condición de pago')])[9]", 1)
        # Selecciona la opcion de Abono, se diligencian campos de Valor de abpono, porcentaje de abono, garantia, poliza 
        # Ciudad de entrega, direccion y observacionbes
        valueabo = self.driver.find_element(By.XPATH, "(//span[contains(@class,'mat-option-text')])[1]")
        ActionChains(self.driver).click(valueabo).send_keys(Keys.TAB,"1000000", Keys.TAB,"5", Keys.TAB, Keys.ARROW_RIGHT,
        Keys.TAB, Keys.ARROW_RIGHT, Keys.TAB, "Ciudad auto", Keys.TAB,"Direccion auto", Keys.TAB,"Observaciones de condiciones auto").perform() 
        sleep(5)
        # Se da click en el botón de Guardar
        f.Click_Mixto("xpath", "(//button[@type='button'])[10]", 10)
        
    def sendorder(self):
        # Llamado de funciones globales
        f = Funciones_Globales(self.driver)
        sleep(6)
        # Se da click en el tap de Órdenes de compra
        f.Click_NotScroll("(//div[contains(.,'Órdenes de compra')])[7]", 1)
        # Se da click en el icono de Enviar
        f.Click_NotScroll("/html/body/app-root/app-mios/app-side-bar/div/mat-sidenav-container/mat-sidenav-content/div/app-solicitudes-list/div/mat-tab-group/div/mat-tab-body[2]/div/app-orden-compra-list/div[3]/table/tbody/tr[1]/td[1]/div/button[3]", 2)
        # Se da click en el botón de Aceptar
        f.Click_NotScroll("//button[contains(.,'Aceptar')]", 1)
        sleep(20)

    def fragorder(self):
        # Llamado de funciones globales
        f = Funciones_Globales(self.driver)
        # Se realiza que una variable random para el numero de productos se modulo para ver si es par o impar el numero
        companyrandiv = companyran % 2
        # Se divide el numero en 2 para asi mismo hacer 2 fragmentaciones
        frag = companyran/2
        # Se da click al modulo de analista
        f.Click_Mixto("xpath", "(//div[@class='mat-list-item-content'][contains(.,'Solicitudes')])[1]", 1)
        # Se da click al tap de Ordenes de compra
        f.Click_NotScroll("(//div[contains(.,'Órdenes de compra')])[7]",3 )
        # Se da click al icono de fragmentacion
        f.Click_NotScroll("(//i[@class='fi-rr-layout-fluid'])[1]", 3)
        # Se da click al botón de siguiente
        f.Click_Mixto("xpath", "(//button[contains(.,'Siguiente')])[1]", 2)
        # Se valida si es par
        if companyrandiv == 0:
            fragpar=(int(frag))
            # Diligencia el campo de nueva cantidad
            f.Texto_Mixto("xpath", "(//input[@type='number'])[5]", fragpar, 5)
            # Se da click al botón de siguiente
            f.Click_NotScroll("(//button[contains(.,'Siguiente')])[2]", 1)
            # Se da click al botón de Guardar
            f.Click_Mixto("xpath", "//button[contains(.,'Guardar')]", 21)
            # Se da click al icono de fragmentacion
            f.Click_NotScroll("(//i[@class='fi-rr-layout-fluid'])[1]", 5)
            # Se da click al botón de siguiente
            f.Click_Mixto("xpath", "(//button[contains(.,'Siguiente')])[1]", 2)
            # Diligencia el campo de nueva cantidad
            f.Texto_Mixto("xpath", "(//input[@type='number'])[5]", fragpar, 5)
            # Se da click al botón de siguiente
            f.Click_NotScroll("(//button[contains(.,'Siguiente')])[2]", 1)
            # Se da click al botón de Guardar
            f.Click_Mixto("xpath", "//button[contains(.,'Guardar')]", 14)
        else:
        # Se valida si es impar
            fragimpar1 = (int(frag))
            #Se le suma uno mas para que de la totalidad
            fragimpar2 =(int(frag+1))
            # Diligencia el campo de nueva cantidad
            f.Texto_Mixto("xpath", "(//input[@type='number'])[5]", fragimpar1, 5)
            # Se da click al botón de siguiente
            f.Click_NotScroll("(//button[contains(.,'Siguiente')])[2]",1 )
             # Se da click al botón de Guardar
            f.Click_Mixto("xpath", "//button[contains(.,'Guardar')]", 21)
            f.Click_NotScroll("(//i[@class='fi-rr-layout-fluid'])[1]",4)
            f.Click_Mixto("xpath", "(//button[contains(.,'Siguiente')])[1]", 2)
            # Diligencia el campo de nueva cantidad
            f.Texto_Mixto("xpath", "(//input[@type='number'])[5]", fragimpar2, 5)
            # Se da click al botón de siguiente
            f.Click_NotScroll("(//button[contains(.,'Siguiente')])[2]",1)
            # Se da click al botón de Guardar
            f.Click_Mixto("xpath", "//button[contains(.,'Guardar')]", 13)

    def cancelationOC(self):
        # Llamado de funciones globales
        f = Funciones_Globales(self.driver)
        # Se da click al icono del ojo
        f.Click_NotScroll("(//i[contains(@class,'fi-rr-eye')])[1]",2)
        # Se da click al tap de Finalizar orden
        f.Click_NotScroll("//mat-step-header[contains(.,'3Finalizar orden')]",1)
        # Diligencia el campo de Observacion
        f.Texto_Mixto("xpath", "(//input[@type='text'])[8]", "Observación cancelación automaticamente", 2)
        # Se da click al botón de Enviar
        f.Click_Mixto("xpath","//button[@color='primary'][contains(.,'Enviar')]", 8)
            


        

        



        


        