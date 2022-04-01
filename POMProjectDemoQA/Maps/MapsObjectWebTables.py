class MapsObjectWebTables():

    #def __init__(self,driver):
        #self.driver = driver
    def __init__(self):

        #creamos MapsObject
        self.btnElements = "//*[name()='path' and contains(@d,'M16 132h41')]"
        self.btnWebTable = "//span[normalize-space()='Web Tables']"
        self.btnAdd = "//button[@id='addNewRecordButton']"

        self.txFirstName = "//input[@id='firstName']"
        self.txtLastName = "//input[@id='lastName']"
        self.txtEmail = "//input[@id='userEmail']"
        self.txtAge = "(//input[@id='age'])[1]"
        self.txtSalary = "(//input[@id='salary'])[1]"
        self.txtDepartment = "(//input[@id='department'])[1]"

        self.btnSubmit = "(//button[normalize-space()='Submit'])[1]"

        self.btnDelete = "(//*[name()='path'])[57]"
        self.btnHome = "(//img[@src='/images/Toolsqa.jpg'])[1]"








