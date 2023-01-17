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

class Coordinator(unittest.TestCase):
    def __init__(self,driver):
        self.driver=driver

    def manageaccept(self):
        f = Funciones_Globales(self.driver)
        f.Click_Mixto("xpath", "(//div[@class='mat-list-item-content'][contains(.,'Solicitudes')])[3]", 4)
        f.Click_NotScroll("(//i[contains(@class,'fi-rr-check')])[1]")
        sleep(2)
        # f.Click_NotScroll("(//button[contains(@type,'button')])[7]")
        f.Click_NotScroll("//button[contains(.,'Aceptar')]")
        sleep(5)
    
    def managedecline(self):
        f = Funciones_Globales(self.driver)
        f.Click_Mixto("xpath", "(//div[@class='mat-list-item-content'][contains(.,'Solicitudes')])[3]", 4)
        f.Click_NotScroll("(//i[contains(@class,'fi-rr-cross')])[1]")
        sleep(2)
        f.Click_NotScroll("//button[contains(.,'Aceptar')]")
        sleep(5)

    