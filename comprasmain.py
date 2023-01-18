import unittest
from os import remove
from selenium import webdriver
from time import sleep
from pyunitreport import HTMLTestRunner
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from Funcionesglobales.funciselenium import Funciones_Globales
from Funcionesglobales.loginqa import Login_qasoul
from Funcionesglobales.roleapplicant import Applicant
from Funcionesglobales.roleanalyst import Analyst
from Funcionesglobales.rolecoordinator import Coordinator
from Funcionesglobales.rolecontrol import Control


class Comprasauto(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")
        # self.driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver1.exe")
        funciones = Funciones_Globales(self.driver)
        funciones.Navegar("http://qamios.groupcos.com/login", 1)
        
    # def test_compras_complete(self):
    #     # Flujo completo desde la solicitud hasta el ingreso del producto
    #     f = Funciones_Globales(self.driver)
    #     login = Login_qasoul(self.driver)
    #     roleapplicant = Applicant(self.driver)
    #     roleanalyst = Analyst(self.driver)
    #     rolecoordinator = Coordinator(self.driver)
    #     rolecontrol = Control(self.driver)
    #     login.loginqa()
    #     login.menucompras()
    #     roleapplicant.createnewrequest()
    #     rolecontrol.managerequestContNotAvailable()
    #     roleanalyst.managerequestAnaAccept()
    #     rolecoordinator.manageaccept()
    #     roleanalyst.order()
    #     roleanalyst.sendorder()

    def test_compras_complete_frag(self):
        # Flujo completo desde la solicitud hasta el ingreso del producto con orden de compra fragmentada
        f = Funciones_Globales(self.driver)
        login = Login_qasoul(self.driver)
        roleapplicant = Applicant(self.driver)
        roleanalyst = Analyst(self.driver)
        rolecoordinator = Coordinator(self.driver)
        rolecontrol = Control(self.driver)
        login.loginqa()
        login.menucompras()
        roleapplicant.createnewrequest()
        rolecontrol.managerequestContNotAvailable()
        roleanalyst.managerequestAnaAccept()
        rolecoordinator.manageaccept()
        roleanalyst.order()
        roleanalyst.fragorder()

    ##### orden de compra cancelada 

    
    # def test_compra_available(self):
    #     #Se realiza test para cuando el rol control valide disponibilidad del producto en Almacen 
    #     f = Funciones_Globales(self.driver)
    #     login = Login_qasoul(self.driver)
    #     roleapplicant = Applicant(self.driver)
    #     roleanalyst = Analyst(self.driver)
    #     rolecoordinator = Coordinator(self.driver)
    #     rolecontrol = Control(self.driver)
    #     login.loginqa()
    #     login.menucompras()
    #     roleapplicant.createnewrequest()
    #     rolecontrol.managerequestContdAvailable()

    # def test_compras_back(self):
    #     #Se realiza test para cuando el rol de analista devuelva la solicitud.
    #     f = Funciones_Globales(self.driver)
    #     login = Login_qasoul(self.driver)
    #     roleapplicant = Applicant(self.driver)
    #     roleanalyst = Analyst(self.driver)
    #     rolecoordinator = Coordinator(self.driver)
    #     rolecontrol = Control(self.driver)
    #     login.loginqa()
    #     login.menucompras()
    #     roleapplicant.createnewrequest()
    #     rolecontrol.managerequestContNotAvailable()
    #     roleanalyst.managerequestAnaback()

    # def test_compras_coor_decline(self):
    #     # Flujo completo desde la solicitud hasta que el coordinador rechaza la solicitud.
    #     f = Funciones_Globales(self.driver)
    #     login = Login_qasoul(self.driver)
    #     roleapplicant = Applicant(self.driver)
    #     roleanalyst = Analyst(self.driver)
    #     rolecoordinator = Coordinator(self.driver)
    #     rolecontrol = Control(self.driver)
    #     login.loginqa()
    #     login.menucompras()
    #     roleapplicant.createnewrequest()
    #     rolecontrol.managerequestContNotAvailable()
    #     roleanalyst.managerequestAnaAccept()
    #     rolecoordinator.managedecline()
        
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

