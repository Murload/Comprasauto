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
        
    # def test_compras1_comp(self):
    #     # Flujo completo desde la solicitud hasta el ingreso del producto
    #     print("# Flujo completo desde la solicitud hasta el ingreso del producto")
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
    #     f.End()

    # def test_compras2_com_fra(self):
    #     # Flujo completo desde la solicitud hasta el ingreso del producto con orden de compra fragmentada
    #     # print(" # Flujo completo desde la solicitud hasta el ingreso del producto con orden de compra fragmentada")
    #     # f = Funciones_Globales(self.driver)
    #     # login = Login_qasoul(self.driver)
    #     # roleapplicant = Applicant(self.driver)
    #     # roleanalyst = Analyst(self.driver)
    #     # rolecoordinator = Coordinator(self.driver)
    #     # rolecontrol = Control(self.driver)
    #     # login.loginqa()
    #     # login.menucompras()
    #     # roleapplicant.createnewrequest()
    #     # rolecontrol.managerequestContNotAvailable()
    #     # roleanalyst.managerequestAnaAccept()
    #     # rolecoordinator.manageaccept()
    #     # roleanalyst.order()
    #     # roleanalyst.fragorder()
    #     # f.End()

    def test_compras3_com_fra_can(self):
        # Flujo completo desde la solicitud hasta el ingreso del producto con orden de compra fragmentada
        print(" # Flujo completo desde la solicitud hasta el ingreso del producto con orden de compra fragmentada")
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
        roleanalyst.sendorder()
        roleanalyst.cancelaOrder()
        f.End()

    # ##### orden de compra cancelada 

    # def test_compra4_available_pro(self):
    #     #Se realiza test para cuando el rol control valide disponibilidad del producto en Almacen 
    #     print("#Se realiza test para cuando el rol control valide disponibilidad del producto en Almacen")
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
    #     f.End()


    # def test_compras5_back_manage(self):
    #     #Se realiza test para cuando el rol de analista devuelva la solicitud.
    #     print("#Se realiza test para cuando el rol de analista devuelva la solicitud.")
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
    #     f.End()


    # def test_compras6_coor_declinee(self):
    #     # Flujo completo desde la solicitud hasta que el coordinador rechaza la solicitud.
    #     print("# Flujo completo desde la solicitud hasta que el coordinador rechaza la solicitud.")
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
    #     f.End()

        
    def tearDown(self):
        self.driver.implicitly_wait(10)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

