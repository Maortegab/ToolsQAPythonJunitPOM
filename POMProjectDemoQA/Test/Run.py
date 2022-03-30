from selenium import webdriver
import time
import unittest
#from POMProjectDemoQA.Maps.MapsObjectWebTables import MapsObjectWebTables
from  POMProjectDemoQA.Pages.PageObjectWebTables import  PageObjectWebTables

'''@property
def driver(self):
    return self._driver
@driver.setter
def driver(self, driver):
    self._driver = driver'''

class Run(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get("http://demoqa.com")

    #def testWebTable(self):

        #crea un objeto login y llama metodo Enter_username y enter_password
        POwebTables = PageObjectWebTables(driver)
        time.sleep(1)
        #INGRESA AL MENU WEB TABLES
        POwebTables.clickElements()
        #POwebTables.addData("Miguel","Ortega", "ma@mail.com","20", "1000", "Bogotá")


    '''def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")'''