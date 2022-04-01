class MapsObjectDatePicker():

    def __init__(self):

        # creamos MapsObject
        self.btnWidgets = "(//h5[normalize-space()='Widgets'])[1]"
        self.btnDatePicker = "//div[@class='element-list collapse show']//li[@id='item-2']"

        #Select Date
        self.btnSelectDate = "(//input[@id='datePickerMonthYearInput'])[1]"

        # Ingreso a menu date and time
        self.txtDateAndTime = "(//input[@id='dateAndTimePickerInput'])[1]"
        self.btnHora = "//li[normalize-space()='09:45']"

        self.btnHome = "(//img[@src='/images/Toolsqa.jpg'])[1]"