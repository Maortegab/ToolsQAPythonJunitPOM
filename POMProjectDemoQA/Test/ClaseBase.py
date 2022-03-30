import time


class ClaseBase():

    def __init__ (self,driver):
        self.driver = driver

    def tiempoEspera(self, tiempo):
        # self.driver.implicitly_wait(tiempo)
        time.sleep(tiempo)

    def clickObjeto(self, by,objeto):
        #self.listaPasos.append("Se procede a dar click en: " + objeto)
        #self.screenShotApp()
        self.driver.find_element(by, objeto).click()
        self.tiempoEspera(1)


    '''def clickObjeto(self):
        self.listaPasos.append("Se procede a dar click en: " + objeto)
        self.screenShotApp()
        #self.driver.find_element(by, objeto).click()
        self.tiempoEspera(1)'''