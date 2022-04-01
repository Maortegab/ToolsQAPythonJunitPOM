from selenium import webdriver

import unittest
from POMProjectDemoQA.Pages import PageObjectWebTables
from POMProjectDemoQA.Pages.PageObjectDatePicker import *
from POMProjectDemoQA.Pages.PageObjectWebTables import *
from POMProjectDemoQA.Pages.PageObjectAlerts import *
from POMProjectDemoQA.Test import  ClaseBase




class Run(unittest.TestCase):

    '''@property
    def driver(self):
        return self._driver

    @driver.setter
    def driver(self, driver):
        self._driver = driver'''

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")
        #cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

        #Definimos driver y llamamos la URL
        driver = cls.driver
        driver.get("http://demoqa.com")


    def testWebTable(self):

        clickElements(self)

        #INGRESA AL MENU WEB TABLES
        addData(self,"Miguel","Ortega", "ma@mail.com","20", "1000", "Bogotá")

    def testDatePicker(self):

        clickPicker(self)

        #INGRESA AL MENU WEB TABLES
        addDataDate(self,"01/13/2002","January 13, 2002")


    def testAlert(self):

        clickAlerts(self)
        #clickAlerts(self)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
