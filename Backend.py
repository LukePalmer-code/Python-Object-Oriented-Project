#PYTHON COURSEWORK 02 --UP2121336 --LUKE PALMER
#BACKEND
##############################################
##############################################

#TASK 1
class SmartPlug():
    """
    This is the smartPlug class,the first class to be written. 
    The other classes inherit from this one as it is top of the hierachy
    """

    def __init__(self, switchedOn = False, consumptionRate = 0):
        """
        Here is my constructor for the SmartPlug class, I defined the instance variables in here so that they will default at False and 0 on every object.
        """
        self.switchedOn = switchedOn
        self.consumptionRate = consumptionRate

    def toggleSwitch(self):
        """
        This function will check to see what state the plug is in and will then reverse it
        """
        if self.switchedOn == True:
            self.switchedOn = False
        
        elif self.switchedOn == False:
            self.switchedOn = True

    def setConsumptionRate(self, newRate):
        """
        This function uses newRate to set the consumption rate of the plug, if newRate is 0 it will tell the user
        and if newRate is above 150 will also tell the user and in both scenarios will not set the consumption rate until
        the correct rate is set.
        """
        if newRate < 0:
            print("Consumption rate cannot be negative")
        elif newRate > 150:
            print("Consumption rate cannot be above 150")
        else:
            self.consumptionRate = newRate
                
    def getSwitchState(self):
        """
        Simply returns whatever state switchedOn is in, either True or False
        """
        return self.switchedOn
        
    def getConsumptionRate(self):
        """
        Retuns consumptionRate set by the user or the default of 0
        """
        return self.consumptionRate

    def __str__(self):
        """
        This is how a smartPlug Object is converted into a tring format which will allow the program to print the plugs variables conumptionRate and switchedOn
        instead of outputting a memory location!!
        """
        output = (f"Plug: Consumption rate: {self.consumptionRate}, {self.switchedOn}")
        return output

def testSwitch():
    """
    This is my test function, I commented it out just incase the objects mess with the frontend.
    """
    # plugTest = SmartPlug()  #Switch starts off False 
    # plugTest.toggleSwitch() #Sets the switch to True
    # print(plugTest.getSwitchState())  #True
    # print(plugTest.getConsumptionRate())  #0
    # plugTest.setConsumptionRate(150)
    # print(plugTest.getConsumptionRate())  #150
    # print(plugTest)
    pass

#testSwitch()

#TASK 2

class SmartOven(SmartPlug):
    """
    This is the SmartOven class, it inherits from the SmartPlug class!!
    """
    def __init__(self, switchedOn = False, temperature = 0):
        """
        Here is my smartOven constructor, it is inheriting the switchedOn variable so that I didnt need to rewrite that piece of code!!
        """
        super().__init__(switchedOn)
        self.temperature = temperature
    
    def setOvenTemperature(self, newTemp):
        """
        In retrospect I think this couldve been inhereted from the plug class really and instead of set consumption rate and temperature it couldve been a more general variable
        such as setDeviceRate or something, however im not sure how id have written it so that it could tell between a plug and oven
        """
        if newTemp < 0:
            print("Temperature cannot be negative")
        elif newTemp > 260:
            print("Temperature cannot be above 260")
        else:
            self.temperature = newTemp
    
    # def getSwitchState(self):
    #     return self.switchedOn
    
    def getOvenTemperature(self):
        """
        This gets the oven temperature
        """
        return self.temperature
    
    def __str__(self):
        """
        This allows my oven class to output in a string state
        """
        output = (f"Oven: Temperature: {self.temperature}, {self.switchedOn}")
        return output
    
def testOven():
    """
    This is my oven test function,same thing as my plug, I commented it out just incase the objects mess with the frontend.
    """
#ovenTest = SmartOven()  #Oven starts off False 
#ovenTest.toggleSwitch() #Sets the Oven to True
#print(ovenTest.getSwitchState())  #True
#print(ovenTest.getOvenTemperature())  #0
#ovenTest.setOvenTemperature(130)
#print(ovenTest.getOvenTemperature())  #130
#print(ovenTest)
pass

# testOven()

#TASK 3

class SmartHome(SmartOven, SmartPlug):
    """
    SmartHome class, here it inherits both SmartOven and SmartPlug
    """
    def __init__(self, switchedOn = False, temperature = 0):
        """
        The constructor for my smartHome, the only new variable made is devices which is defined as an empty list for each new smarthouse object
        """
        super().__init__(switchedOn, temperature)
        self.devices = []
    
    def addDevice(self, device):
        """
        This adds a device to the devices list
        """
        self.devices.append(device)

    def getDevices(self): 
        """
        Simply gets all devices stored in the devices list
        """
        return self.devices     

    def getDeviceAt(self, index):
        """
        This gets a device at a certain index in the devices list.
        """
        return self.devices[index]

    def turnOnAll(self):
       """
       This simply goes through all devices in the devices list and changes their switchedOn state to True
       """
       for device in self.devices:
            device.switchedOn = True
        
    def turnOffAll(self):
        """
        This simply goes through all devices in the devices list and changes their switchedOn state to False
        """
        for device in self.devices:
            device.switchedOn = False
        
    def __str__(self):
        """
        Here a smartHome object is converted into a legible string, useful for outputting a smartHome object so it can be read by a person
        """
        output = "The current devices states are:\n"    # The switch is currently: {self.switchedOn}")
        for device in self.devices:
            output += (f"{device}\n")
        return output

def testSmartHome():
    # smartHomeSH1 = SmartHome()
    # plugSH1 = SmartPlug()
    # plugSH2 = SmartPlug()
    # ovenSH1 = SmartOven()
    # plugSH2.toggleSwitch()
    # plugSH2.setConsumptionRate(45)
    # ovenSH1.setOvenTemperature(100)
    # smartHomeSH1.addDevice(plugSH1)
    # smartHomeSH1.addDevice(plugSH2)
    # smartHomeSH1.addDevice(ovenSH1)
    # print(smartHomeSH1)
    # smartHomeSH1.turnOnAll()
    # print(smartHomeSH1)
    pass

# testSmartHome()
