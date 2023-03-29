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
from datetime import datetime
from Funcionesglobales.funciselenium import Funciones_Globales
from Funcionesglobales.roleapplicant import Applicant

# Variable para poner precio de la cotizacion aleatorio
pricecot = random.randint(100000, 999999)
date = datetime.today().strftime('%d%m%Y')
companyran = random.randint(1, 99)
# Variable para poner IVA aleatorio
iva = random.randint(1, 5)
# Variable para poner metodo de pago aleatorio
t= 2

methodpay = random.randint(1, 4)

class Analyst(unittest.TestCase):
    def __init__(self,driver):
        self.driver=driver

    def managerequestAnaAccept(self):
        # Llamado de funciones globales
        sleep(4)
        f = Funciones_Globales(self.driver)
        # Entra al modulo del rol analista
        f.Click_Mixto("xpath", "(//div[contains(.,'Solicitudes')])[7]", t)
        # Se da click en el botón de gestionar
        f.Click_Mixto("xpath", "(//span[contains(.,'Gestionar')])[1]", t)
        # le da click al seleccionable de Estado
        f.Click_Mixto("xpath", "(//div[contains(.,'Estado')])[17]", t)
        # le da click al seleccionable de Estado  
        f.Click_NotScroll("(//span[@class='mat-option-text'])[1]", t)
        # le da click al campo de cotización 
        f.Click_Mixto("xpath", "(//div[contains(.,'Cotización 1')])[9]", t)
        # Se da click en el icono del clip para cargar archivo
        f.Click_NotScroll("/html/body/div[2]/div[2]/div/mat-dialog-container/app-procesar-solicitud/div/form/mat-dialog-content/div[9]/div[2]/div[1]/mat-form-field/div/div[1]/div[2]/i",3)
        #Se debe enviar la ruta donde se encuentra el archivo
        # En este caso se debe modifcar el nombre del usuario en la ruta
        f.uploadfile("C:\\Users\\aleon\\Desktop\\Comprasauto\\filesupload\\cotizacion1.pdf")
        sleep(2)
        # Diligencia el campo de precio 
        price =self.driver.find_element(By.XPATH,"(//input[@aria-required='true'])[2]")
        # Diligencia el campo de observaciones 
        price.send_keys(pricecot, Keys.TAB, Keys.TAB, Keys.TAB, "Pruebas autos")
        # Se da click en el botón de Enviar
        f.Click_NotScroll("//button[contains(.,'Enviar')]", t)
        # Se da click en el botón de Aceptar
        f.Click_NotScroll("//button[contains(.,'Aceptar')]", t)
        # Se da click en el botón de Continuar
        f.Click_NotScroll("//button[contains(.,'Continuar')]", t)

    def managerequestAnaback(self):
        # Llamado de funciones globales
        f = Funciones_Globales(self.driver)
        sleep(4)
        # Entra al modulo del rol analista
        f.Click_Mixto("xpath", "(//div[contains(.,'Solicitudes')])[7]", 3)
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
        print(date)
        f = Funciones_Globales(self.driver)
        sleep(4)
        # Entra al modulo del rol analista
        f.Click_Mixto("xpath", "(//div[contains(.,'Solicitudes')])[7]",5)
        # Se da click en el botón de orden
        f.xpath_buttons("(//span[contains(.,'Orden')])[1]")
        # Diligencia el campo de NIT proveedor y le da enter
          # Diligencia el campo de precio 
        f.sendkeys("//input[contains(@formcontrolname,'nitProveedor')]", 1,"1234567899")
        # Se da click en el botón de Generar orden
        f.Click_NotScroll("//button[contains(.,'Generar Orden')]", 4)
        # Se da click en el botón de siguiente
        f.Click_Mixto("xpath", "(//button[contains(.,'Siguiente')])[1]", 6)
        # Diligencia el campo de descripción, especificación, Cantidad, tipo de moneda, valor unitario 
        textdetails= self.driver.find_element(By.XPATH, "(//input[@type='text'])[5]")
        textdetails.send_keys("Especificación", Keys.TAB, Keys.TAB, Keys.ARROW_RIGHT, Keys.TAB, pricecot)
        # le da click al seleccionable de Iva
        f.Click_NotScroll("(//div[contains(.,'IVA')])[12]",1)
        # Selecciona la opcion de iva aleatoriamente
        f.Click_NotScroll("(//span[@class='mat-option-text'])[{}]".format(iva), 3)
        # Se da click en el botón de siguiente
        f.Click_Mixto("xpath", "(//button[@type='button'])[8]", 5)
        
         # Diligencia el campo de descripción
        f.Texto_Mixto("xpath", "(//input[@type='text'])[6]", "Observación de Orden de compra automatica.",2)
         # Diligencia el campo de Fecha de entrega
        f.Texto_Mixto("xpath", "//input[@type='date']", date,2)
        # le da click al seleccionable de Método de pago
        f.Click_NotScroll("(//div[contains(.,'Método de pago')])[9]", 1)
         # Selecciona la opcion de Método de pago aleatoriamente
        f.Click_NotScroll("(//span[@class='mat-option-text'])[{}]".format(methodpay), 3)
        # le da click al seleccionable de Condicion de pago
        f.Click_NotScroll("(//div[contains(.,'Condición de pago')])[9]", 1)
        # Selecciona la opcion de Abono, se diligencian campos de Valor de abpono, porcentaje de abono, garantia, poliza 
        # Ciudad de entrega, direccion y observacionbes
        valueabo = self.driver.find_element(By.XPATH, "(//span[contains(@class,'mat-option-text')])[1]")
        ActionChains(self.driver).click(valueabo).send_keys(Keys.TAB,"0", Keys.TAB,"5", Keys.TAB, Keys.ARROW_RIGHT,
        Keys.TAB, Keys.ARROW_RIGHT, Keys.TAB, "Ciudad auto", Keys.TAB,"Direccion auto", Keys.TAB,"Observaciones de condiciones auto").perform() 
        sleep(5)
        # Se da click en el botón de Guardar
        f.Click_Mixto("xpath", "(//button[@type='button'])[10]", 2)
        # Se da click en el botón de Guardar
        f.Click_Mixto("xpath", "//button[contains(.,'Continuar')]", 2)

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
        sleep(4)
        f.Click_Mixto("xpath", "(//div[contains(.,'Solicitudes')])[7]", 1)
        # Se da click al tap de Ordenes de compra
        f.Click_NotScroll("(//div[contains(.,'Órdenes de compra')])[7]",3 )
        # Se da click al icono de fragmentacion
        f.Click_NotScroll("(//i[@class='fi-rr-layout-fluid'])[1]", 1)
        # Se da click al botón de siguiente
        f.Click_Mixto("xpath", "(//button[contains(.,'Siguiente')])[1]", 2)


        quantitysol1 = self.driver.find_element(By.XPATH, "(//input[@type='number'])[4]")
        # # Se toma el valor del campo
        companyran1 = quantitysol1.get_attribute('value')
        companyran =(int(companyran1))
        # Se divide el numero en 2 para asi mismo hacer 2 fragmentaciones
        frag = companyran/2
        print(frag)
        # Se valida si es par
        companyrandiv = companyran % 2
        print(companyrandiv)
        if companyrandiv == 0:
            fragpar=(int(frag))
            # Diligencia el campo de nueva cantidad
            f.Texto_Mixto("xpath", "(//input[@type='number'])[5]", fragpar, 5)
            # Se da click al botón de siguiente
            f.Click_NotScroll("(//button[contains(.,'Siguiente')])[2]", 1)
            # Se da click al botón de Guardar
            f.Click_Mixto("xpath", "//button[contains(.,'Guardar')]", 1)
            # Se da click en el botón de Continuar
            f.Click_Mixto("xpath", "//button[contains(.,'Continuar')]", 1)
            f.Click_Mixto("xpath", "(//td[contains(@role,'gridcell')])[2]", 1)
            f.Click_Mixto("xpath", "(//i[contains(@class,'fi-rr-paper-plane')])[1]", 1)
            # Se da click al icono de fragmentacion
            f.Click_NotScroll("(//i[@class='fi-rr-layout-fluid'])[1]", 1)
            # Se da click al botón de siguiente
            f.Click_Mixto("xpath", "(//button[contains(.,'Siguiente')])[1]", 2)
            # Diligencia el campo de nueva cantidad
            f.Texto_Mixto("xpath", "(//input[@type='number'])[5]", fragpar, 1)
            # Se da click al botón de siguiente
            f.Click_NotScroll("(//button[contains(.,'Siguiente')])[2]", 1)
            # Se da click al botón de Guardar
            f.Click_Mixto("xpath", "//button[contains(.,'Guardar')]", 2)
            # Se da click en el botón de Continuar
            f.Click_Mixto("xpath", "//button[contains(.,'Continuar')]", 1)
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
            # Se da click en el botón de Continuar
            f.Click_Mixto("xpath", "//button[contains(.,'Continuar')]", 20)
            # Se da click al icono de fragmentacion
            f.Click_NotScroll("(//i[@class='fi-rr-layout-fluid'])[1]",4)
            # Se da click en el botón de siguiente
            f.Click_Mixto("xpath", "(//button[contains(.,'Siguiente')])[1]", 2)
            # Diligencia el campo de nueva cantidad
            f.Texto_Mixto("xpath", "(//input[@type='number'])[5]", fragimpar2, 5)
            # Se da click al botón de siguiente
            f.Click_NotScroll("(//button[contains(.,'Siguiente')])[2]",1)
            # Se da click al botón de Guardar
            f.Click_Mixto("xpath", "//button[contains(.,'Guardar')]", 2)
            # Se da click en el botón de Continuar
            f.Click_Mixto("xpath", "//button[contains(.,'Continuar')]", 20)

    def cancelationOC(self):
        # Llamado de funciones globales
        f = Funciones_Globales(self.driver)
        # Se da click al icono del ojo
        sleep(3)
        f.Click_NotScroll("(//i[contains(@class,'fi-rr-eye')])[1]",2)
        # Se da click al tap de Finalizar orden
        f.Click_NotScroll("//mat-step-header[contains(.,'3Finalizar orden')]",1)
        # Diligencia el campo de Observacion
        f.Texto_Mixto("xpath", "(//input[@type='text'])[8]", "Observación cancelación automaticamente", 2)
        # Se da click al botón de Enviar
        f.Click_Mixto("xpath","//button[@color='primary'][contains(.,'Enviar')]", 2)
        # Se da click en el botón de Continuar
        f.Click_Mixto("xpath", "//button[contains(.,'Continuar')]", 10)

    def associate(self):
        # Llamado de funciones globales
        f = Funciones_Globales(self.driver)
        # Le da click al modulo del analista
        f.Click_Mixto("xpath", "(//div[contains(.,'Solicitudes')])[7]", 5)
        # Da click en el botón de gestionar
        f.Click_NotScroll("(//span[contains(.,'Gestionar')])[1]", 3)
         # le da click al seleccionable de Estado
        f.Click_Mixto("xpath", "(//div[contains(.,'Estado')])[17]", 3)
        # le da click al seleccionable de Estado  
        f.Click_NotScroll("(//span[@class='mat-option-text'])[1]", 2)
        #Le da click en el botón de Crear solicitud asociada
        f.Click_NotScroll("//button[contains(.,'Crear solicitud asociada')]", 3)
        f.gettext("(//div[@class='col-4'])[12]")
        # Llenar campo de descripcion
        description = self.driver.find_element(By.XPATH, "(//input[contains(@type,'text')])[2]")
        description.click()
        description.send_keys("Producto Asociado 1", Keys.TAB, "7", Keys.TAB, Keys.TAB , "Observaciones solicitud asociada auto")
         # Se da click en el icono del clip para cargar archivo
        f.Click_Mixto("xpath", "/html/body/div[2]/div[2]/div/mat-dialog-container/app-associated-request/div/form/mat-dialog-content/div[14]/div[2]/div[1]/mat-form-field/div/div[1]/div[2]/i",4)
        #Se debe enviar la ruta donde se encuentra el archivo
        # En este caso se debe modifcar el nombre del usuario en la ruta
        f.uploadfile("C:\\Users\\aleon\\Desktop\\Comprasauto\\filesupload\\cotizacion1.pdf")
        sleep(2)
        # Diligencia el campo de precio 
        f.Texto_Mixto("xpath", "(//input[@aria-required='true'])[2]", pricecot ,2)
        # Diligencia el campo de observaciones 
        f.Texto_Mixto("xpath", "(//input[@type='text'])[7]", "Observación cotizaciones automaticas." ,3)
        # Se da click en el botón de Enviar
        f.Click_NotScroll("//button[contains(.,'Enviar')]", 2)
        # Se da click en el botón de Aceptar
        f.Click_NotScroll("//button[contains(.,'Aceptar')]", 6)



        

            


        

        



        


        