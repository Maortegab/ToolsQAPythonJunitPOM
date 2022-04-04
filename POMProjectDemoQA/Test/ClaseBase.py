# Comentario de prueba
# Para visualizacion de cambios
# En GitHub


import keyboard
import time


from selenium import webdriver


class ClaseBase():

    def __init__ (self,driver):
        self.driver: webdriver.Chrome = driver
        #self.driver.implicitly_wait(20)

    def tiempoEspera(self, tiempo):
        # self.driver.implicitly_wait(tiempo)
        time.sleep(tiempo)

    def click(self, objeto):
        #self.listaPasos.append("Se procede a dar click en: " + objeto)
        #self.screenShotApp()
        #self.driver.find_element(by, objeto).click()
        self.driver.find_element(objeto).click()

        #self.driver.find_element()
        #self.tiempoEspera(1)

    def delete(self, objeto):
        keyboard.press_and_release('ctrl + a')
        keyboard.send('delete')

    def submimt(self, objeto):

        keyboard.send('enter')


    '''def clickObjeto(self):
        self.listaPasos.append("Se procede a dar click en: " + objeto)
        self.screenShotApp()
        #self.driver.find_element(by, objeto).click()
        self.tiempoEspera(1)'''

    ##Hola