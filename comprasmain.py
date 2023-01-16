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
from Funcionesglobales.requestt import Request

class Comprasauto(unittest.TestCase):

    def setUp(self):
        # self.driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")
        self.driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver1.exe")
        funciones = Funciones_Globales(self.driver)
        funciones.Navegar("http://qamios.groupcos.com/login", 1)
        
    def test_compras(self):
        f = Funciones_Globales(self.driver)
        login = Login_qasoul(self.driver)
        request = Request(self.driver)
        login.loginqa()
        login.menucompras()
        request.createnewrequest()


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

