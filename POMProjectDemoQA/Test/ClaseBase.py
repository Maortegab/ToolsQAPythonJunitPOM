import time
from selenium import webdriver

class ClaseBase():

    def __init__ (self,driver):
        self.driver: webdriver.Chrome = driver

    def tiempoEspera(self, tiempo):
        # self.driver.implicitly_wait(tiempo)
        time.sleep(tiempo)

    def click(self, by, objeto):
        #self.listaPasos.append("Se procede a dar click en: " + objeto)
        #self.screenShotApp()
        self.driver.find_element(by, objeto).click()

        #self.driver.find_element()
        #self.tiempoEspera(1)


    '''def clickObjeto(self):
        self.listaPasos.append("Se procede a dar click en: " + objeto)
        self.screenShotApp()
        #self.driver.find_element(by, objeto).click()
        self.tiempoEspera(1)'''