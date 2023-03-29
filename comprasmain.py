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
        
    def test_completes(self):
        # Flujo completo desde la solicitud hasta el ingreso del producto
        print("# Flujo completo desde la solicitud hasta el ingreso del producto")
        f = Funciones_Globales(self.driver)
        login = Login_qasoul(self.driver)
        roleapplicant = Applicant(self.driver)
        roleanalyst = Analyst(self.driver)
        rolecoordinator = Coordinator(self.driver)
        rolecontrol = Control(self.driver)
        login.loginqa()
        login.menucompras()
        # roleapplicant.createnewrequest()
        # rolecontrol.managerequestContNotAvailable()
        # roleanalyst.managerequestAnaAccept()
        # rolecoordinator.manageaccept()
        roleanalyst.order()
        roleanalyst.sendorder()
        rolecontrol.entry_product()
        f.End()

    # def test_complete_fragme(self):
    #     # Flujo completo desde la solicitud hasta el ingreso del producto con orden de compra fragmentada
    #     print(" # Flujo completo desde la solicitud hasta el ingreso del producto con orden de compra fragmentada")
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
    #     roleanalyst.fragorder()
    #     rolecontrol.entry_product_frag()
    #     f.End()

    # def test_cancelation(self):
    #     #Flujo completo desde la solicitud hasta el ingreso del producto con orden de compra fragmentada
    #     print(" # Flujo completo desde la solicitud hasta el ingreso del producto con orden de compra enviada pero se cancela")
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
    #     roleanalyst.cancelationOC()
    #     f.End()

    # def test_available_pro(self):
    #     #Se realiza test para cuando el rol control valide disponibilidad del producto en Almacen 
    #     print("#Se realiza test para cuando el rol control valide disponibilidad del producto en Almacen")
    #     f = Funciones_Globales(self.driver)
    #     login = Login_qasoul(self.driver)
    #     roleapplicant = Applicant(self.driver)
    #     rolecontrol = Control(self.driver)
    #     login.loginqa()
    #     login.menucompras()
    #     roleapplicant.createnewrequest()
    #     rolecontrol.managerequestContdAvailable()
    #     f.End()

    # def test_back_manage(self):
    #     #Se realiza test para cuando el rol de analista devuelva la solicitud.
    #     print("#Se realiza test para cuando el rol de analista devuelva la solicitud.")
    #     f = Funciones_Globales(self.driver)
    #     login = Login_qasoul(self.driver)
    #     roleapplicant = Applicant(self.driver)
    #     roleanalyst = Analyst(self.driver)
    #     rolecontrol = Control(self.driver)
    #     login.loginqa()
    #     login.menucompras()
    #     roleapplicant.createnewrequest()
    #     rolecontrol.managerequestContNotAvailable()
    #     roleanalyst.managerequestAnaback()
    #     f.End()

    # def test_coor_declinee(self):
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

    # def test_analyst_assoc(self):
        # Flujo con una solicitud asociada
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
        roleanalyst.associate()
        rolecoordinator.manageaccept()
        roleanalyst.order()
        roleanalyst.sendorder()
        rolecontrol.entry_product()
        f.End()

        
    def tearDown(self):
        self.driver.implicitly_wait(10)
        self.driver.close()

# if __name__ == "__main__":
#     unittest.main()

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reports', report_name='reportComercial2'))

