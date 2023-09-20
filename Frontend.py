#PYTHON COURSEWORK 02 --UP2121336 --LUKE PALMER
#FRONTEND
##############################################
##############################################
#TASKS 4-5-6

from Backend import *
from tkinter import *
from tkinter import ttk

smartHome1 = SmartHome()
mainWin = Tk()

plug1 = SmartPlug()
plug2 = SmartPlug()
oven1 = SmartOven()
oven2 = SmartOven()
oven3 = SmartOven()

def turnOffAll():
    smartHome1.turnOffAll()
    createWidgets(mainWin)

def turnOnAll():
    smartHome1.turnOnAll()
    createWidgets(mainWin)

def setupHome():
    #SP, SP, C, C, C UP2121336
    smartHome1.addDevice(plug1)
    smartHome1.addDevice(plug2)
    smartHome1.addDevice(oven1)
    smartHome1.addDevice(oven2)
    smartHome1.addDevice(oven3)

def smartHomeApp():
    mainWin.title("SmartHome")
    mainWin.geometry("350x225")
    mainWin.resizable (width=False, height=False)
    mainWin.configure(bg = "#3F497F")
    mainWin.columnconfigure(index=0, weight=1)
    mainWin.columnconfigure(index=1, weight=6)
    mainWin.columnconfigure(index=2, weight=6)
    createWidgets(mainWin)
    mainWin.mainloop()
    
def createWidgets(mainWin):
    setupHome()
    styling = ttk.Style()
    styling.configure("Tk.TTk", background = "#000000")
    styling.configure("Label.TLabel",
        font = ("Arial", 20, "bold"),
        background = ("#3F497F"),
        foreground = ("#F7C04A")
    )
    styling.configure("Label2.TLabel",
        font = ("Arial", 12, "bold"),
        background = ("#3F497F"),
        foreground = ("#F8F5E4")
    )
    styling.configure("Button.TButton",
        font = ("Arial", 10, "bold"),
        # background = ("#539165"),
        foreground = ("#3F497F")
    )
 
    titleLabel = ttk.Label(mainWin, text="SmartHome", style = "Label.TLabel")
    titleLabel.grid(row=0)

    deviceLabel1 = ttk.Label(mainWin, text= f"{plug1}", style = "Label2.TLabel")
    deviceLabel1.grid(row=3, column=0)

    deviceLabel2 = ttk.Label(mainWin, text= f"{plug2}", style = "Label2.TLabel")
    deviceLabel2.grid(row=4, column=0)

    deviceLabel3 = ttk.Label(mainWin, text= f"{oven1}", style = "Label2.TLabel")
    deviceLabel3.grid(row=5, column=0)

    deviceLabel4 = ttk.Label(mainWin, text= f"{oven2}", style = "Label2.TLabel")
    deviceLabel4.grid(row=6, column=0)

    deviceLabel5 = ttk.Label(mainWin, text= oven3 , style = "Label2.TLabel")
    deviceLabel5.grid(row=7, column=0)

    def toggleButton1():
        plug1.toggleSwitch()
        createWidgets(mainWin)
    
    def toggleButton2():
        plug2.toggleSwitch()
        createWidgets(mainWin)

    def toggleButton3():
        oven1.toggleSwitch()
        createWidgets(mainWin)

    def toggleButton4():
        oven2.toggleSwitch()
        createWidgets(mainWin)

    def toggleButton5():
        oven3.toggleSwitch()
        createWidgets(mainWin)

    deviceButton1 = ttk.Button(mainWin, text="Toggle This", command=toggleButton1, style = "Button.TButton")
    deviceButton1.grid(row=3, column=1)

    deviceButton2 = ttk.Button(mainWin, text="Toggle This", command=toggleButton2, style = "Button.TButton")
    deviceButton2.grid(row=4, column=1)

    deviceButton3 = ttk.Button(mainWin, text="Toggle This", command=toggleButton3, style = "Button.TButton")
    deviceButton3.grid(row=5, column=1)

    deviceButton4 = ttk.Button(mainWin, text="Toggle This", command=toggleButton4, style = "Button.TButton")
    deviceButton4.grid(row=6, column=1)

    deviceButton5 = ttk.Button(mainWin, text="Toggle This", command=toggleButton5, style = "Button.TButton")
    deviceButton5.grid(row=7, column=1)
    
    turnOnAllButton = ttk.Button(mainWin, text="Turn On All", command=turnOnAll, style = "Button.TButton")
    turnOnAllButton.grid(row=1, column=0)

    turnOffAllButton = ttk.Button(mainWin, text="Turn Off All", command=turnOffAll, style = "Button.TButton")
    turnOffAllButton.grid(row=2, column=0)

def main():
    setupHome()
    smartHomeApp()
main()

    
