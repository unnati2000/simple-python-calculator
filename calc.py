import tkinter as ttk 

calcValue = ""

def addToEq(x):
    global calcValue
    calcValue = calcValue + str(x)
    numericEq.set(calcValue)

def calculateEq():
    global calcValue
    total = str(eval(calcValue))
    numericEq.set(total)

def clearInput():
    global calcValue
    calcValue = ""
    numericEq.set("")


win = ttk.Tk()
win.title('Simple Calculator')
win.geometry('500x500')


numericEq = ttk.StringVar()

dataField = ttk.Entry(win, textvariable=numericEq, font="Serif 15")
dataField.grid(row=0,columnspan=3, ipadx=80, ipady=15)


# div 1
oneButton = ttk.Button(win, text="1", pady=10, padx=20, font = "Serif 15",bg = "black", fg = "white", command=lambda: addToEq(1))
oneButton.grid(row=2, column=0,padx=2, pady=3)

twoButton = ttk.Button(win, text="2", pady=10, padx=20, font = "Serif 15",bg = "black", fg = "white", command=lambda: addToEq(2))
twoButton.grid(row=2, column=1, padx=2, pady=3)

threeButton = ttk.Button(win, text="3", pady=10, padx=20, font = "Serif 15",bg = "black", fg = "white", command=lambda: addToEq(3))
threeButton.grid(row=2, column=2, padx=2, pady=3)

plusButton = ttk.Button(win, text="+", pady=10, padx=20, font = "Serif 15",bg = "black", fg = "white", command=lambda: addToEq("+"))
plusButton.grid(row=2, column=3, padx=2, pady=3)


# div 2
fourButton = ttk.Button(win, text="4", pady=10, padx=20, font = "Serif 15",bg = "black", fg = "white", command=lambda: addToEq(4))
fourButton.grid(row=3, column=0, padx=2, pady=3)


fiveButton = ttk.Button(win, text="5", pady=10, padx=20, font = "Serif 15",bg = "black", fg = "white", command=lambda: addToEq(5))
fiveButton.grid(row=3, column=1, padx=2, pady=3)


sixButton = ttk.Button(win, text="6", pady=10, padx=20, font = "Serif 15",bg = "black", fg = "white", command=lambda: addToEq(6))
sixButton.grid(row=3, column=2, padx=2, pady=3)

minusButton = ttk.Button(win, text="-", pady=10, padx=20, font = "Serif 15",bg = "black", fg = "white", command=lambda: addToEq("-"))
minusButton.grid(row=3, column=3, padx=2, pady=3)



# div 3
sevenButton = ttk.Button(win, text="7", pady=10, padx=20, font = "Serif 15",bg = "black", fg = "white", command=lambda: addToEq(7))
sevenButton.grid(row=4, column=0, padx=2, pady=3)

eightButton = ttk.Button(win, text="8", pady=10, padx=20, font = "Serif 15",bg = "black", fg = "white", command=lambda: addToEq(8))
eightButton.grid(row=4, column=1, padx=2, pady=3)

nineButton = ttk.Button(win, text="9", pady=10, padx=20, font = "Serif 15",bg = "black", fg = "white", command=lambda: addToEq(9))
nineButton.grid(row=4, column=2, padx=2, pady=3)

muxButton = ttk.Button(win, text="x", pady=10, padx=20, font = "Serif 15",bg = "black", fg = "white", command=lambda: addToEq("*"))
muxButton.grid(row=4, column=3, padx=2, pady=3)

#div 4
zeroButton = ttk.Button(win, text="0", pady=10, padx=20, font = "Serif 15",bg = "black", fg = "white", command=lambda: addToEq(0))
zeroButton.grid(row=5, column=0, padx=2, pady=3)

clearButton = ttk.Button(win, text="clr", pady=10, padx=20, font = "Serif 15",bg = "black", fg = "white", command=clearInput)
clearButton.grid(row=5, column=1, padx=2, pady=3)

calculateButton = ttk.Button(win, text="cal", pady=10, padx=20, font = "Serif 15",bg = "black", fg = "white", command=calculateEq)
calculateButton.grid(row=5, column=2, padx=2, pady=3)

divideButton = ttk.Button(win, text="/", pady=10, padx=20, font = "Serif 15",bg = "black", fg = "white", command=lambda: addToEq("/"))
divideButton.grid(row=5, column=3, padx=2, pady=3)

win.mainloop()