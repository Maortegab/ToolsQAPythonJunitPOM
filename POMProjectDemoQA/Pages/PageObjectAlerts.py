from selenium.webdriver.common.by import By
from POMProjectDemoQA.Maps.MapsObjectAlerts import *
from POMProjectDemoQA.Test.ClaseBase import *

def clickAlerts(self):
#def clickAlerts(self):
    #Instancia de clase base
    cb = ClaseBase(self)
    #Instancia de MapsObject
    mapsAlerts = MapsObjectAlerts()


    cb.tiempoEspera(1)
    #cb.click("xpath", mapsWebTables.btnElements)
    self.driver.find_element(by=By.XPATH, value=mapsAlerts.btnAlertsFrame).click()
    self.driver.find_element(by=By.XPATH, value=mapsAlerts.btnAlerts).click()
    # driver.get_screenshot_as_file(f".\\Screenshots\\elements_{inspect.stack()[0][3]}.png")
    cb.tiempoEspera(1)

    self.driver.find_element(by=By.XPATH, value=mapsAlerts.btnSeeAlert).click()
    cb.tiempoEspera(1)
    self.driver.switch_to.alert.accept()
    cb.tiempoEspera(1)

    self.driver.find_element(by=By.XPATH, value=mapsAlerts.btnTimeAlert).click()
    cb.tiempoEspera(5)
    self.driver.switch_to.alert.accept()
    self.driver.find_element(by=By.XPATH, value=mapsAlerts.btnConfAlert).click()
    cb.tiempoEspera(1)
    self.driver.switch_to.alert.accept()
    cb.tiempoEspera(1)
    self.driver.find_element(by=By.XPATH, value=mapsAlerts.btnConfAlert).click()
    self.driver.switch_to.alert.dismiss()
    cb.tiempoEspera(1)
    self.driver.find_element(by=By.XPATH, value=mapsAlerts.btnBoxAlert).click()
    self.driver.switch_to.alert.send_keys("Miguel")
    self.driver.switch_to.alert.accept()
    cb.tiempoEspera(3)

    self.driver.find_element(by=By.XPATH, value=mapsAlerts.btnHome).click()
    cb.tiempoEspera(1)