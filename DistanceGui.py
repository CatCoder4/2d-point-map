from tkinter import *
from functools import partial
import distanceCalc
import DistanceSimiluate

def showCordinates(var, elementList):
    if var.get() is True:
        for index, item in enumerate(elementList):
            if index == 4:
                item.grid(row=3, column=0)        
            elif index < 2:
                item.grid(row=1, column=index)
            else:
                item.grid(row=2, column=index - 2)        
    else:
        for i in elementList:
            i.grid_forget()

def calculateCords(xentry, yentry):
    A = (0, 0)
    B = (0, 3)
    C = (5, 0)
    E = (int(xentry.get()), int(yentry.get()))

    if xentry.get() == '' or yentry.get() == '':
        print("Empty X or Y cordinate please type a number in them")
    else:
        E, ae, be, ce = distanceCalc.cordCalc(A, B, C, E)
        DistanceSimiluate.Simulate(600, 500, B, C, E, ae, be, ce)

def showDistance(var, elementList):
    if var.get() is True:
        for index, item in enumerate(elementList):
            if index == 6:
                item.grid(row=4, column=0)        
            elif index == 0 or index == 1:
                item.grid(row=1, column=index)
            elif index == 2 or index == 3:
                item.grid(row=2, column=index-2)
            else:
                item.grid(row=3, column=index - 4)  
    else:
        for i in elementList:
            i.grid_forget()

def calculateDist(aeE, beE, ceE):
    B = (0, 3)
    C = (5, 0)
    ae = float(aeE.get())
    be = float(beE.get())
    ce = float(ceE.get())
    
    if ae.get() == '' or be.get() == '' or ce.get() == '':
        print("you must type something into the inputs")
    else:
        E = distanceCalc.distCalc(B, C, ae, be, ce)
        DistanceSimiluate.Simulate(600, 500, B, C, E, ae, be, ce)