from tkinter import *
from tkinter import ttk
from numpy import *
import math
from os import *

#python Dividends Calc
#Frame and Window 
root = Tk()
#root.iconbitmap(root, default = "TpyICO.ico" )
root.geometry('450x275')
root.title("Stock Divi Calc- By @Nimble.Berto")
root.configure(bg='white', highlightbackground="black")

#Variables
Stock = StringVar()
Div = StringVar()
YearlyDiv = StringVar()
QrtlyDiv = float
DivSchedule = ["January", "April", "July", "October"]
calendar = ["January", "February", "March", "April", "May", "June", "July", "August",
    "September", "October", "November", "December"]
QtyStock = "1"
MultiPayQ = float
MultiPayY = float
MultiPtemp = float
MultiYtemp = float

# ----- Entry Fields and Labels LEFT SIDE----------------
label_1 = Label(root, text="Stock Price: $", fg="black", bg="white").grid(row=0, sticky = E)
label_2 = Label(root, text="Yearly Div %:", fg="black", bg="white").grid(row=1, sticky = E)
label_3 = Label(root, text="Qty of Stock:", fg="black", bg="white").grid(row=2, sticky = E)

entry_1 = Entry(root, width=10, textvariable = Stock)
entry_1.configure(bg="white", fg="black")
entry_1.grid(row=0, column = 1)

entry_2 = Entry(root, width=10, textvariable = Div)
entry_2.configure(bg="white", fg="black")
entry_2.grid(row=1, column = 1)

entry_3 = Entry(root, width=10, textvariable = QtyStock)
entry_3.configure(bg="white", fg="black")
entry_3.grid(row=2, column = 1)
entry_3.insert(0, string= "1")

#-----------------------RIGHT-Side labels------------------
label_StkPrice = Label(root, text = "Enter Data, Click Update!")
label_StkPrice.configure(font='Helvetica 14 bold', fg= "black", bg="white")
label_StkPrice.grid(row=0, column=3)

label_YearYield = Label(root, text = "Yearly Payout: $")
label_YearYield.grid(row=1, column=3)
label_YearYield.configure(font='Helvetica 14 bold', fg="black", bg="white")

label_QrtlyYield = Label(root, text = "Qrtly Payout: $", font= 'Helvetica 14 bold', fg="black", bg="white")
label_QrtlyYield.grid(row=3, column=3)


label_QrtlyCount = Label(root, text = "Next Qrtrly Pay is: ", font= 'Helvetica 14 bold', fg="black", bg="white")
label_QrtlyCount.grid(row=4, column=3)

label_SessionCount = Label(root, text = "Days until payout: ", font= 'Helvetica 16 bold', fg="black", bg="white")
label_SessionCount.grid(row=5, column=3)

#----------------------------------------------------------------

#Calc YEARLY Div Pay, user inputs stockPrice(i.e. 4.52) && YrlyDiv % (i.e. 10.12) = YrlyPayout
def YearlyPay():
        StockTemp = float(Stock.get())
        DivTemp = float(Div.get())
        QrtlyDiv = float()
        try:
            YearlyDiv = StockTemp * (DivTemp / 100)
            QrtlyDiv = YearlyDiv / 4
        except ZeroDivisionError:
            YearlyDiv = Stock/1
    
        label_YearYield.configure(text="Your Yearly Yield: $ %.3f " % YearlyDiv, font='Helvetica 14 bold', fg = "green")
        label_QrtlyYield.configure(text="Your Qrtly Yield: $ %.3f " % QrtlyDiv, font='Helvetica 14 bold', fg = "green")



#Multi Stock Pay Calc

def Multi():
    YearTemp = YearlyDiv.get()
    QtyTemp = int(QtyStock)
    MultiPayY = YearTemp * QtyTemp
    MultiPayQ1 = (YearTemp * QtyTemp)
    #MultiPayQ = MultiPayQ1 / 4
    MultiPayY = float

    label_YearYield.configure(text="Your Yearly Yield: $" + str(MultiPayY), font='Helvetica 14 bold', fg = "green")
    label_QrtlyYield.configure(text="Your xxQrtrly Yield: $" + str(MultiPayQ), font='Helvetica 14 bold', fg = "green")
    
    return;




def action():
    if int(entry_3.get()) < 2:
        YearlyPay()
    else:
        Multi()
 
    return;


#------------BUTTON-------------------------

button_1 = ttk.Button(root, text = "Update", command= action)
button_1.grid(row=4, column=1)



'''
List Estimated time until next Qrtly Payout: import OS date&time and subtract days left until
next payday (4 dates in list) do math for (today's date) closest to next pay day in list. followed
by NextPayDay - Today's calendar day (out of 365) 
'''




root.mainloop()