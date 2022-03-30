import inspect
import time

from selenium.webdriver.common.by import By
from POMProjectDemoQA.Maps.MapsObjectWebTables import MapsObjectWebTables
from POMProjectDemoQA.Test.ClaseBase import ClaseBase


class PageObjectWebTables():
    def __init__(self,driver):
        self.driver = driver



    def clickElements(self):
        #cb = ClaseBase(self)
        mapsWebTables = MapsObjectWebTables()
        #cb.tiempoEspera(2)
        print("alguna otra mierda")
        #cb.clickObjeto("XPATH", mapsWebTables.btnElements)
        #cb.clickObjeto(By.XPATH, mapsWebTables.btnElements)
        #driver.get_screenshot_as_file(f".\\Screenshots\\elements_{inspect.stack()[0][3]}.png")
        self.driver.find_element(by=By.XPATH, value=mapsWebTables.btnElements).click()
        print("alguna otra mierda adicional")

        '''self.driver.find_element(by=By.XPATH, value=MapsWebTables.btnWebTable).click()
        self.driver.find_element(by=By.XPATH, value=MapsWebTables.btnAdd).click()
        base.tiempoEspera(self,2)

    def addData(self,fName, lName, email, Age, salary, departament):
        MapsWebTables = MapsObjectWebTables()
        self.driver.find_element(by=By.XPATH, value=MapsWebTables.txFirstName).send_keys(fName)
        self.driver.find_element(by=By.XPATH, value=MapsWebTables.txtLastName).send_keys(lName)
        self.driver.find_element(by=By.XPATH, value=MapsWebTables.txtEmail).send_keys(email)
        self.driver.find_element(by=By.XPATH, value=MapsWebTables.txtAge).send_keys(Age)
        self.driver.find_element(by=By.XPATH, value=MapsWebTables.txtSalary).send_keys(salary)
        self.driver.find_element(by=By.XPATH, value=MapsWebTables.txtDepartment).send_keys(departament)

        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value=MapsWebTables.btnSubmit).click()
        time.sleep(1)
        #BORRANDO PRIMER REGISTRO
        self.driver.find_element(by=By.XPATH, value=MapsWebTables.btnDelete).click()
        time.sleep(1)
        #IR A PAGINA INICIAL
        self.driver.find_element(by=By.XPATH, value=MapsWebTables.btnHome).click()
        time.sleep(1)'''