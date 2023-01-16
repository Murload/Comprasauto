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


class Analyst(unittest.TestCase):
    def __init__(self,driver):
        self.driver=driver


    def managerequestAna(self):
        f = Funciones_Globales(self.driver)
        f.Click_Mixto("xpath", "(//div[@class='mat-list-item-content'][contains(.,'Solicitudes')])[1]", 1)
        f.Click_Mixto("xpath", "//span[@class='mat-button-wrapper'][contains(.,'Gestionar')]", 1)
        