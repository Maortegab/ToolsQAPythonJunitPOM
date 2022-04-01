class MapsObjectAlerts():

    def __init__(self):

        #creamos MapsObject
        self.btnAlertsFrame = "//div[3]//div[1]//div[2]//*[name()='svg']"
        self.btnAlerts = "//span[normalize-space()='Alerts']"

        self.btnSeeAlert = "(//button[@id='alertButton'])[1]"
        self.btnTimeAlert = "//button[@id='timerAlertButton']"
        self.btnConfAlert = "(//button[@id='confirmButton'])[1]"
        self.btnBoxAlert = "(//button[@id='promtButton'])[1]"

        self.btnHome = "(//img[@src='/images/Toolsqa.jpg'])[1]"