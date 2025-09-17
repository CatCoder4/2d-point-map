from tkinter import *
from functools import partial
from DistanceGui import calculateCords, calculateDist, showCordinates, showDistance



def main():
    window = Tk()
    window.title("x and y value calculator simulate")
    window.geometry("400x400")

    # the cordinate Gui
    Xlabel = Label(window, font=("helvetica, 10"), text="Enter the X of the unknown")
    Ylabel = Label(window, font=("helvetica, 10"), text="Enter the Y of the unknown")
    Xentry = Entry(window, font=("helvetica, 30"), width=4, relief=SUNKEN, bd=3)
    Yentry = Entry(window, font=("helvetica, 30"), width=4, relief=SUNKEN, bd=3)

    # Distance gui
    aeEntry = Entry(window, font=("helvetica, 30"), width=4, relief=SUNKEN, bd=3)
    label1 = Label(window, font=("helvetica, 10"), text="Enter the distance between A and E")
    beEntry = Entry(window, font=("helvetica, 30"), width=4, relief=SUNKEN, bd=3)
    label2 = Label(window, font=("helvetica, 10"), text="Enter the distance between B and E")
    ceEntry = Entry(window, font=("helvetica, 30"), width=4, relief=SUNKEN, bd=3)
    label3 = Label(window, font=("helvetica, 10"), text="Enter the distance between C and E")
    calcDist = partial(calculateDist, aeE=aeEntry, beE=beEntry, ceE=ceEntry)
    submitDist = Button(window, text="submit", font=("helvetica, 25"), relief=SUNKEN, bd=5, command=calcDist)

    cordinateMode = BooleanVar()
    calcCords = partial(calculateCords, xentry=Xentry, yentry=Yentry)
    submitXandy = Button(window, text="submit", font=("helvetica, 25"), relief=SUNKEN, bd=5, command=calcCords)
    showcord = partial(showCordinates, var=cordinateMode, elementList=[Xentry, Xlabel, Yentry , Ylabel, submitXandy])
    DistanceMode = BooleanVar()
    showdist = partial(showDistance, var=DistanceMode, elementList=[aeEntry, label1, beEntry, label2, ceEntry, label3, submitDist])


    # check buttons

    Checkbutton(window, text="Use cordinate mode", variable=cordinateMode, command=showcord).grid(row=0, column=0)
    Checkbutton(window, text="Use distance mode", variable=DistanceMode, command=showdist).grid(row=0, column=1)


    window.mainloop()


main()