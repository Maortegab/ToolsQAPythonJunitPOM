from selenium.webdriver.common.by import By
from POMProjectDemoQA.Maps.MapsObjectDatePicker import *
from POMProjectDemoQA.Test.ClaseBase import *

def clickPicker(self):
    #Instancia de clase Base
    cb = ClaseBase(self)
    #Instancia de Maps
    mapsDatePicker = MapsObjectDatePicker()

    cb.tiempoEspera(1)
    self.driver.find_element(by=By.XPATH, value=mapsDatePicker.btnWidgets).click()
    self.driver.find_element(by=By.XPATH, value=mapsDatePicker.btnDatePicker).click()
    cb.tiempoEspera(1)

def addDataDate(self, SDate, dateNTime):
    #Instancia de clase Base
    cb = ClaseBase(self)
    # Instancia de Maps
    mapsDatePicker = MapsObjectDatePicker()
    self.driver.find_element(by=By.XPATH, value=mapsDatePicker.btnSelectDate).click()
    cb.tiempoEspera(1)
    cb.delete(self.driver.find_element(by=By.XPATH, value=mapsDatePicker.btnSelectDate))
    cb.tiempoEspera(1)
    self.driver.find_element(by=By.XPATH, value=mapsDatePicker.btnSelectDate).send_keys(SDate)
    cb.submimt(self.driver.find_element(by=By.XPATH, value=mapsDatePicker.btnSelectDate))
    cb.tiempoEspera(1)

    self.driver.find_element(by=By.XPATH, value=mapsDatePicker.txtDateAndTime).click()
    cb.tiempoEspera(1)
    cb.delete(self.driver.find_element(by=By.XPATH, value=mapsDatePicker.txtDateAndTime))
    cb.tiempoEspera(1)
    self.driver.find_element(by=By.XPATH, value=mapsDatePicker.txtDateAndTime).send_keys(dateNTime)
    self.driver.find_element(by=By.XPATH, value=mapsDatePicker.btnHora).click()
    cb.tiempoEspera(2)
    self.driver.find_element(by=By.XPATH, value=mapsDatePicker.btnHome).click()
    cb.tiempoEspera(1)