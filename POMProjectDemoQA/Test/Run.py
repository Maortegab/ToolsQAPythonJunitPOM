from selenium import webdriver
import time
import unittest
#from POMProjectDemoQA.Maps.MapsObjectWebTables import MapsObjectWebTables
from selenium.webdriver.common import by

from POMProjectDemoQA.Pages import PageObjectWebTables
from  POMProjectDemoQA.Pages.PageObjectWebTables import  *

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

    #def test_login_valid(self):
        #driver = self.driver
        #driver.get("http://demoqa.com")

    def testWebTable(self):

        # crea objeto pageObject
        #POwebTables = PageObjectWebTables(driver)

        #INGRESA AL MENU WEB TABLES
        PageObjectWebTables.clickElements(self)
        #POwebTables.addData("Miguel","Ortega", "ma@mail.com","20", "1000", "Bogotá")


    '''def tearDownClass(self):
        self.driver.close()
        #cls.driver.quit()
        print("Test completed")'''