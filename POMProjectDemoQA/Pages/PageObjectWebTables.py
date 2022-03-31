from selenium.webdriver.common.by import By
from POMProjectDemoQA.Maps.MapsObjectWebTables import *
from POMProjectDemoQA.Test.ClaseBase import *


'''class PageObjectWebTables():
    def __init__(self,driver):
        self.driver = driver'''

def clickElements(self):
    #Instancia de clase base
    cb = ClaseBase(self)
    #Instancia de MapsObject
    mapsWebTables = MapsObjectWebTables()

    cb.tiempoEspera(1)
    #cb.click("xpath", mapsWebTables.btnElements)
    self.driver.find_element(by=By.XPATH, value=mapsWebTables.btnElements).click()
    # driver.get_screenshot_as_file(f".\\Screenshots\\elements_{inspect.stack()[0][3]}.png")
    cb.tiempoEspera(1)



    self.driver.find_element(by=By.XPATH, value=mapsWebTables.btnWebTable).click()
    self.driver.find_element(by=By.XPATH, value=mapsWebTables.btnAdd).click()
    cb.tiempoEspera(1)

def addData(self,fName, lName, email, Age, salary, departament):
    mapsWebTables = MapsObjectWebTables()
    cb = ClaseBase(self)
    self.driver.find_element(by=By.XPATH, value=mapsWebTables.txFirstName).send_keys(fName)
    self.driver.find_element(by=By.XPATH, value=mapsWebTables.txtLastName).send_keys(lName)
    self.driver.find_element(by=By.XPATH, value=mapsWebTables.txtEmail).send_keys(email)
    self.driver.find_element(by=By.XPATH, value=mapsWebTables.txtAge).send_keys(Age)
    self.driver.find_element(by=By.XPATH, value=mapsWebTables.txtSalary).send_keys(salary)
    self.driver.find_element(by=By.XPATH, value=mapsWebTables.txtDepartment).send_keys(departament)

    cb.tiempoEspera(1)
    self.driver.find_element(by=By.XPATH, value=mapsWebTables.btnSubmit).click()
    cb.tiempoEspera(1)
    #BORRANDO PRIMER REGISTRO
    self.driver.find_element(by=By.XPATH, value=mapsWebTables.btnDelete).click()
    cb.tiempoEspera(1)
    #IR A PAGINA INICIAL
    self.driver.find_element(by=By.XPATH, value=mapsWebTables.btnHome).click()
    cb.tiempoEspera(1)