from selenium import webdriver

import unittest
from POMProjectDemoQA.Pages import PageObjectWebTables


@property
def driver(self):
    return self._driver
@driver.setter
def driver(self, driver):
    self._driver = driver

class Run(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        #Definimos driver y llamamos la URL
        driver = cls.driver
        driver.get("http://demoqa.com")

    def testWebTable(self):
        #INGRESA AL MENU WEB TABLES
        PageObjectWebTables.clickElements(self)
        #POwebTables.addData("Miguel","Ortega", "ma@mail.com","20", "1000", "Bogotá")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
