from tkinter import *
from tkinter import messagebox
import random
import time
import os
from ftplib import FTP


root = Tk()
root.geometry("1350x750+0+0")
root.title("Major Cineplex")
root.configure(background='black')

FrameTops = Frame(root, width= 1350, height = 100, bd=10, relief="raised")
FrameTops.pack(side=TOP)
FrameTops.configure(background='firebrick4')
TitleHead = Label(FrameTops,font=('TH Sarabun new',50,'bold'), fg='bisque',text = "        Engineer Cineplex        ", bg="red4", bd=10)
TitleHead.grid(row=0,column=0) 

FrameBottom = Frame(root, width= 1350, height = 120, bd=6, relief="sunken")
FrameBottom.pack(side=BOTTOM)
FrameBottom.configure(background='gray80')
fInfo1 = Frame(FrameBottom,width= 300,height = 120, bd=3, relief="flat")
fInfo1.pack(side=LEFT)
fInfo2 = Frame(FrameBottom,width= 300,height = 120, bd=3, relief="flat")
fInfo2.pack(side=LEFT)
fInfo3 = Frame(FrameBottom,width= 300,height = 120, bd=3, relief="flat")
fInfo3.pack(side=LEFT)
fInfo4 = Frame(FrameBottom,width= 445,height = 120, bd=5, relief="sunken")
fInfo4.pack(side=LEFT)


FrameLeft = Frame(root, width= 900, height = 476, bd=6, relief="sunken")
FrameLeft.pack(side=LEFT)
fTicket = Frame(FrameLeft,width= 445,height = 476, bd=5, relief="flat")
fTicket.pack(side=LEFT)
fSnack = Frame(FrameLeft,width= 445,height = 476, bd=5, relief="flat")
fSnack.pack(side=RIGHT)

FrameRight = Frame(root, width= 440, height = 460, bd=6, relief="sunken")
FrameRight.pack(side=RIGHT)

ftotal = Frame(FrameRight, width= 440, height = 80, bd=2, relief="sunken", bg="black")
ftotal.pack(side=TOP)
fReceipt = Frame(FrameRight, width= 400, height = 360, relief="flat",bg="black")
fReceipt.pack(side=BOTTOM)

#============================================================ function Command Btn ============================================================
def qExit():
    qExit = messagebox.askyesno("Quit", "Do you want to quit?")
    if qExit > 0:
        root.destroy()
        return

def Reset():
    txtTotal.configure(state = NORMAL)
    txtReceipt.configure(state = NORMAL)
    FrameTicketReset()
    FrameSnackReset()
    FrameCostReset()
    txtReceipt.delete("1.0",END)
    txtTotal.delete("1.0",END)
    txtTotal.configure(state = DISABLED)
    txtReceipt.configure(state = DISABLED)

def FrameTicketReset():
    for x in VarTicketList:    
        x.set("0")

    for x in EntryTicketList:    
        x.set("0")
        
    txtNormal.configure(state = DISABLED)
    txtHoneymoon.configure(state = DISABLED)
    txtPair.configure(state = DISABLED)

def FrameSnackReset():
    for x in VarSnackList:    
        x.set("0")

    for x in EntrySnackList:    
        x.set("0")

    txtPopcorn1.configure(state = DISABLED)
    txtPopcorn2.configure(state = DISABLED)
    txtPopcorn3.configure(state = DISABLED)
    txtPopcorn4.configure(state = DISABLED)
    txtSoftdrink1.configure(state = DISABLED)
    txtSoftdrink2.configure(state = DISABLED)
    txtSoftdrink3.configure(state = DISABLED)
    txtSoftdrink4.configure(state = DISABLED)
    txtSoftdrink5.configure(state = DISABLED)
    txtSet1.configure(state = DISABLED)
    txtSet2.configure(state = DISABLED)
    txtSet3.configure(state = DISABLED)
    txtAppe1.configure(state = DISABLED)
    txtAppe2.configure(state = DISABLED)
    
def FrameCostReset():

    CostofTicket.set("")          #price of Ticket
    CostofSnack.set("")           #price of Snack
    PaidTax.set("")               #Tax
    Subtotal.set("")              #Sum Ticket and Snack
    Cash.set("")                  #money from customer
    LicensePlate.set("")          #number of Car
    TotalCost.set("")             #Sum all
    
    Change.set("")                #money give customer


def chkbutton_value(chkValue, txtLabel, Entry):
    if chkValue.get() == 1:
        txtLabel.configure(state = NORMAL)
    elif chkValue.get() == 0:
        txtLabel.configure(state = DISABLED)
        Entry.set("0")
        
###################################################################### Variable for Value #################################################
Ticket0 = 0
Ticket1 = 0
Ticket2 = 0
ValueTicket = [Ticket0, Ticket1, Ticket2]
    
Snack0 = 0
Snack1 = 0
Snack2 = 0
Snack3 = 0
Snack4 = 0
Snack5 = 0
Snack6 = 0
Snack7 = 0
Snack8 = 0
Snack9 = 0
Snack10 = 0
Snack12 = 0
Snack11 = 0
Snack13 = 0
ValueSnack = [Snack0, Snack1, Snack2, Snack3, Snack4, Snack5, Snack6, Snack7, Snack8, Snack9, Snack10, Snack11, Snack12, Snack13]

def CostofItem():
    ################################################### CHECK INPUT MENU IF NOT NUMBER ##################################################   
    txtTotal.configure(state = NORMAL)
    for n in range(3) :
         if(EntryTicketList[n].get() != ""):
            try:
                ValueTicket[n] = float(EntryTicketList[n].get())
            except ValueError: 
                AskforSend = messagebox.showwarning("Value Error!!","Please input number again.")
                EntryTicketList[n].set("")
    
    for m in range(14) :
        if(EntrySnackList[m].get() != ""):
            try:
                ValueSnack[m] = float(EntrySnackList[m].get())
            except ValueError: 
                AskforSend = messagebox.showwarning("Value Error!!","Please input number again.")
                EntrySnackList[m].set("")
                   
    TotalTicketCost = 0
    TotalSnackCost = 0
       
    for i in range(3) :
        TotalTicketCost += ValueTicket[i] * float(TicketPriceList[i])
    
    for i in range(14) :
        TotalSnackCost += ValueSnack[i] * float(SnackPriceList[i])
                                                             
    TicketPrice = str('%.2f'%(TotalTicketCost) + '  baht')       #Calculate price of Ticket
    SnackPrice = str('%.2f'%(TotalSnackCost)  + '  baht')        #Calculate price of Snack
    CostofTicket.set(TicketPrice)
    CostofSnack.set(SnackPrice)

    CostPlus = TotalTicketCost + TotalSnackCost                  #Calculate Subtotal
    SubTotalofItems = str('%.2f'%(CostPlus) + '  baht')
    Subtotal.set(SubTotalofItems)

    Tax = str('%.2f'%(CostPlus*0.15)+ '  baht')                   #Calculate Paid Tax  (Subtotal * 0.15)
    PaidTax.set(Tax)
    
    TTax = CostPlus * 0.15
    TC = str('%.2f'%(CostPlus + TTax) + '  baht')
    TotalCost.set(TC)                                           #Calculate Total (Subtotal + Tax)
    
    txtTotal.delete("1.0",END)
    txtTotal.insert(END, TotalCost.get())
    
    txtTotal.configure(state = DISABLED)
    
    
def Enter():
    txtTotal.configure(state = NORMAL)
    txtReceipt.configure(state = NORMAL)
    txtTotal.delete("1.0",END)
    txtReceipt.delete("1.0",END)
    
    Changemoney = 0
    InvalidCash = False
        
    TotalTicketCost = 0
    TotalSnackCost = 0
           
    for i in range(3) :
        TotalTicketCost += ValueTicket[i] * float(TicketPriceList[i])
    
    for i in range(14) :
        TotalSnackCost += ValueSnack[i] * float(SnackPriceList[i])
    
    LP = LicensePlate.get()
    CostPlus = TotalTicketCost + TotalSnackCost 
    TTax = CostPlus * 0.15
    
    try:
        Changemoney = float(Cash.get()) - float(CostPlus + TTax)      #Calculate Change
    except:
        InvalidCash = True 
    else :
        InvalidCash = False
    
    if(LP == "" and Cash.get() == ""):
        txtTotal.insert(END, TotalCost.get())
        txtReceipt.delete("1.0",END)
        txtReceipt.insert(END,'Please Input Cash and License Plate !!!\n')
        txtReceipt.tag_add("no both", "1.0", "1.40")
        txtReceipt.tag_config("no both", background="red", foreground="white")
        print('No Input Cash and License Plate')
    
    elif Cash.get() == "" :
        txtTotal.insert(END, TotalCost.get())
        txtReceipt.delete("1.0",END)
        txtReceipt.insert("1.0",'Please Input Cash !!!\n')
        txtReceipt.tag_add("no cash", "1.0", "1.21")
        txtReceipt.tag_config("no cash", background="red", foreground="white")
        print('No Input Cash')
    
    elif InvalidCash :
        txtTotal.insert(END, TotalCost.get())
        txtReceipt.delete("1.0",END)
        txtReceipt.insert("1.0",'Please Input Number !!!\n')
        txtReceipt.tag_add("no int", "1.0", "1.23")
        txtReceipt.tag_config("no int", background="red", foreground="white")
        print('No Input License Plate is Integer')
        
    elif float(Cash.get()) < float(CostPlus + TTax) :
        txtTotal.insert(END, TotalCost.get())
        txtReceipt.delete("1.0",END)
        txtReceipt.insert(END,'Not enough money!!!\n')
        txtReceipt.tag_add("no money", "1.0", "1.40")
        txtReceipt.tag_config("no money", background="red", foreground="white")
        print('No Money')
        
    else :
    
        txtReceipt.insert(END,'Receipt No :\t'+ ReceiptRef.get()  + '\t\t\t\t' + DateofOrder.get() + "\n\n")
        txtReceipt.insert(END,'\tItems\t\t\t\t'+ 'Cost of Items \n')
        
        for i in range(3) :
            if ValueTicket[i] > 0 :
                txtReceipt.insert(END, '\t'+ TicketList[i] + '('+ str('%.2f'%TicketPriceList[i]) + ')\t\t\t\t\t'+ EntryTicketList[i].get() + '\n')  
         
        for i in range(14) :
            if ValueSnack[i] > 0 :
                txtReceipt.insert(END, '\t' + SnackList[i] + '('+ str('%.2f'%SnackPriceList[i]) + ')\t\t\t\t\t' + EntrySnackList[i].get() + '\n')        
    
        txtReceipt.insert(END,'\nCost of Ticket : \t\t'+ CostofTicket.get() + '\n')
        txtReceipt.insert(END,'Cost of Snack : \t\t'+ CostofSnack.get() + '\n')
        txtReceipt.insert(END,'Paid Tax : \t\t'+ PaidTax.get() + '\n\n')
        txtReceipt.insert(END,'Balance : \t\t'+ TotalCost.get() )
                              
        Ch = str('%.2f'%(Changemoney)+ '  baht')
        Change.set(Ch)
        if LP == '-':
            txtTotal.insert(END, Change.get())
            txtReceipt.insert(END,'\nChange : \t\t'+ Change.get() + '\n')       #Set receipt
        else:
            try:
                login = open("Login.txt")
            except IOError:
                print("Can not find file or read data")      
            else:
                for server in login:
                    FTPServer, Username, Password, firstF ,secondF = server.split(';')
                    try:
                        ftp = FTP(FTPServer)
                        ftp.login(user = Username, passwd = Password)
                    except:
                        print("Can not Login!\n")
                        print("Please try again")
                        break
                    
                    def downloadFile(filename):
                        try:
                            localfile = open(filename, 'wb')
                            ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
                        except:
                            print("Can not download file!")
                        localfile.close()
                    
                    def uploadFile(filename):
                        try:
                            ftp.storbinary('STOR ' + filename, open(filename, 'rb'))
                        except:
                            print("Can not upload file!")
                    
                    ftp.cwd(firstF)
                    ftp.cwd(secondF)
                    
                    filenameInput = 'Bill.txt'
                    downloadFile(filenameInput)
                    stateCar = 2
                                  
                    if LP == "":
                        txtTotal.insert(END, TotalCost.get())
                        AskforSend = messagebox.showwarning("Warning!",'If not use parking,\nPlease input "-" in License Plate Box')
                        print('No Input License Plate')
                    else:
                        TCc , bt =TotalCost.get().split()
                        Costed = 0.0
                        status = 1
                        
                        try:
                            billRE = open("Bill.txt",'r',encoding = "utf-8")
                        except IOError:
                            print("Can not find file or read data")
                        else:
                            for line in billRE:
                                LPP,Cost,state = line.split(";")
                                if LP == LPP and state != 2:
                                    stateCar = 1
                                if LP == LPP and state == 2:
                                    stateCar = 2
                            billRE.close()
                            if stateCar == 2 :
                                txtTotal.insert(END, TotalCost.get())
                                AskforSend = messagebox.askyesno("License Plate not found", "License Plate not found\nDo you want to Continue?")
                                if AskforSend:
                                    txtTotal.delete("1.0",END)
                                    txtTotal.insert(END, Change.get())
                                    txtReceipt.insert(END,'\nChange : \t\t'+ Change.get() + '\n')       #Set receipt
                                else:
                                    AFS = messagebox.showinfo("Input License Plate!","Please input License Plate again.")
                                    LicensePlate.set("")
                            elif stateCar == 1 :
                                txtTotal.insert(END, TotalCost.get())
                                AskforSend = messagebox.askyesno("Found License Plate", "Found License Plate\nDo you want to Continue?")
                                if AskforSend:
                                    txtTotal.delete("1.0",END)
                                    txtTotal.insert(END, Change.get())
                                    txtReceipt.insert("1.0",'Status :       Found License Plate \n')
                                    txtReceipt.tag_add("CORRECT", "1.14", "1.43")
                                    txtReceipt.tag_config("CORRECT", background="green", foreground="white")
                                    txtReceipt.insert(END,'\nChange : \t\t'+ Change.get() + '\n')       #Set receipt
                                    try:
                                        billR = open("Bill.txt",'r',encoding = "utf-8")
                                    except IOError:
                                        print("Can not find file or read data")
                                    else:
                                        for line in billR:
                                            LPP,Cost,state = line.split(";")
                                            if LP == LPP:
                                                Costed = Cost
                                        billR.close()
                                        TC = float(TCc) + float(Costed)
                                    try:
                                        billFile = open("Bill.txt", "a", encoding = "utf-8")
                                    except IOError:
                                        print("Can not find file or read data")
                                    else:
                                        print("Written content in the file successfully")
                                        billFile.write(str(LP) + ";" + str(TC) + ";" + str(status) + "\n")
                                    billFile.close()
                                    sendFile = "Bill.txt"
                                    uploadFile(sendFile)              
                    ftp.close()
                login.close()
        
    txtTotal.configure(state = DISABLED)
    txtReceipt.configure(state = DISABLED)
    #*******************************************************************************************************************************

def Receipt():
    txtReceipt.configure(state = NORMAL)
    txtTotal.delete("1.0",END)
    txtReceipt.delete("1.0",END)
    x = random.randint(10908,500876)
    randomRef = str(x)
    ReceiptRef.set("BILL"+ randomRef)

    txtReceipt.insert(END,'Receipt No :\t'+ ReceiptRef.get()  + '\t\t\t\t' + DateofOrder.get() + "\n\n")
    txtReceipt.insert(END,'\tItems\t\t\t\t'+ 'Cost of Items \n')
    
    for i in range(3) :
        if ValueTicket[i] > 0 :
            txtReceipt.insert(END, '\t'+ TicketList[i] + '('+ str('%.2f'%TicketPriceList[i]) + ')\t\t\t\t\t'+ EntryTicketList[i].get() + '\n')  
     
    for i in range(14) :
        if ValueSnack[i] > 0 :
            txtReceipt.insert(END, '\t' + SnackList[i] + '('+ str('%.2f'%SnackPriceList[i]) + ')\t\t\t\t\t' + EntrySnackList[i].get() + '\n')        

    txtTotal.insert(END, TotalCost.get())
    txtReceipt.insert(END,'\nCost of Ticket : \t\t'+ CostofTicket.get() + '\n')
    txtReceipt.insert(END,'Cost of Snack : \t\t'+ CostofSnack.get() + '\n')
    txtReceipt.insert(END,'Paid Tax : \t\t'+ PaidTax.get() + '\n\n')
    txtReceipt.insert(END,'Balance : \t\t'+ TotalCost.get() )
    txtReceipt.configure(state = DISABLED)
    

#============================================================ Read File Menu ============================================================

Ticket = open(r'Ticket.txt')
TicketList = []
TicketPriceList = []
for line in Ticket :
    menu, price = line.split(":")
    TicketList.append(menu)
    TicketPriceList.append(int(price))
Ticket.close()

SnackMenu = open(r'Snack.txt')
SnackList = []
SnackPriceList = []
for line in SnackMenu :
    menu, price = line.split(":")
    SnackList.append(menu)
    SnackPriceList.append(int(price))
SnackMenu.close() 

#============================================================ Variable Ticket ============================================================
ReceiptRef = StringVar()
DateofOrder = StringVar()
DateofOrder.set(time.strftime("%d/%m/%Y"))

VarTicket0 = IntVar()
VarTicket1 = IntVar()
VarTicket2 = IntVar()

VarTicketList = [VarTicket0, VarTicket1, VarTicket2]

for i in VarTicketList :    
    i.set("0")

EntryTicket0 = StringVar()
EntryTicket1 = StringVar()
EntryTicket2 = StringVar()

EntryTicketList = [EntryTicket0, EntryTicket1, EntryTicket2]

for i in EntryTicketList :    
    i.set("0")

#============================================================ Variable Snack ============================================================

VarSnack0 = IntVar()
VarSnack1 = IntVar()
VarSnack2 = IntVar()
VarSnack3 = IntVar()
VarSnack4 = IntVar()
VarSnack5 = IntVar()
VarSnack6 = IntVar()
VarSnack7 = IntVar()
VarSnack8 = IntVar()
VarSnack9 = IntVar()
VarSnack10 = IntVar()
VarSnack11 = IntVar()
VarSnack12 = IntVar()
VarSnack13 = IntVar()

VarSnackList = [VarSnack0, VarSnack1, VarSnack2, VarSnack3, VarSnack4, VarSnack5, VarSnack6, VarSnack7
                , VarSnack8, VarSnack9, VarSnack10, VarSnack11, VarSnack12, VarSnack13]

for i in VarSnackList :    
    i.set("0")

EntrySnack0 = StringVar()
EntrySnack1 = StringVar()
EntrySnack2 = StringVar()
EntrySnack3 = StringVar()
EntrySnack4 = StringVar()
EntrySnack5 = StringVar()
EntrySnack6 = StringVar()
EntrySnack7 = StringVar()
EntrySnack8 = StringVar()
EntrySnack9 = StringVar()
EntrySnack10 = StringVar()
EntrySnack11 = StringVar()
EntrySnack12 = StringVar()
EntrySnack13 = StringVar()


EntrySnackList = [EntrySnack0, EntrySnack1, EntrySnack2, EntrySnack3, EntrySnack4, EntrySnack5, EntrySnack6, EntrySnack7
                  , EntrySnack8, EntrySnack9, EntrySnack10, EntrySnack11, EntrySnack12, EntrySnack13]

for i in EntrySnackList :    
    i.set("0")

#============================================================ Variable for Calculate ============================================================

CostofTicket = StringVar()
CostofSnack = StringVar()
PaidTax = StringVar()
Subtotal = StringVar()
Cash = StringVar()
LicensePlate = StringVar()
TotalCost = StringVar()
Change = StringVar()

#=========================================================== CheckButton and Text Ticket Infomation =======================================

LabelTicket = Label(fTicket, font=('TH Sarabun new',20,'bold'), text = "Ticket", bd=10).grid(row = 0,sticky=W)

Ticket0 = Checkbutton(fTicket, text = TicketList[0], variable = VarTicketList[0], onvalue = 1, offvalue=0,font=('TH Sarabun New',18,'bold')
                      , command=lambda:chkbutton_value(VarTicketList[0], txtNormal, EntryTicketList[0])).grid(row= 1, sticky=W)

Ticket1 = Checkbutton(fTicket, text = TicketList[1], variable = VarTicketList[1], onvalue = 1, offvalue=0,font=('TH Sarabun New',18,'bold')
                      , command=lambda:chkbutton_value(VarTicketList[1], txtHoneymoon, EntryTicketList[1])).grid(row= 2, sticky=W)

Ticket2 = Checkbutton(fTicket, text = TicketList[2], variable = VarTicketList[2], onvalue = 1, offvalue=0,font=('TH Sarabun New',18,'bold')
                      , command=lambda:chkbutton_value(VarTicketList[2], txtPair, EntryTicketList[2])).grid(row= 3, sticky=W)

#============================================================ Entry Ticket Infomation ============================================================

txtNormal = Entry(fTicket, font=('TH Sarabun New',16,'bold'), bd=3, width=8, justify='center', textvariable = EntryTicketList[0], state = DISABLED)
txtNormal.grid(row=1,column =1)

txtHoneymoon = Entry(fTicket, font=('TH Sarabun New',16,'bold'), bd=3, width=8, justify='center', textvariable = EntryTicketList[1], state = DISABLED)
txtHoneymoon.grid(row=2,column =1)

txtPair = Entry(fTicket, font=('TH Sarabun New',16,'bold'), bd=3, width=8, justify='center', textvariable = EntryTicketList[2], state = DISABLED)
txtPair.grid(row=3,column =1)

#=========================================================== CheckButton and Text Snack Infomation =======================================

LabelSnack = Label(fTicket,font=('TH Sarabun new',20,'bold'), text = "Popcorn", bd=10).grid(row = 4,sticky=W)

Snack0 = Checkbutton(fTicket, text = SnackList[0], variable = VarSnackList[0], onvalue = 1, offvalue=0,font=('TH Sarabun New',18,'bold')
                      , command=lambda:chkbutton_value(VarSnackList[0], txtPopcorn1, EntrySnackList[0])).grid(row= 5, sticky=W)

Snack1 = Checkbutton(fTicket, text = SnackList[1], variable = VarSnackList[1], onvalue = 1, offvalue=0,font=('TH Sarabun New',18,'bold')
                      , command=lambda:chkbutton_value(VarSnackList[1], txtPopcorn2, EntrySnackList[1])).grid(row= 6, sticky=W)

Snack2 = Checkbutton(fTicket, text = SnackList[2], variable = VarSnackList[2], onvalue = 1, offvalue=0,font=('TH Sarabun New',18,'bold')
                      , command=lambda:chkbutton_value(VarSnackList[2], txtPopcorn3, EntrySnackList[2])).grid(row= 7, sticky=W)

Snack3 = Checkbutton(fTicket, text = SnackList[3], variable = VarSnackList[3], onvalue = 1, offvalue=0,font=('TH Sarabun New',18,'bold')
                      , command=lambda:chkbutton_value(VarSnackList[3], txtPopcorn4, EntrySnackList[3])).grid(row= 8, sticky=W)

LabelSnack = Label(fSnack,font=('TH Sarabun new',20,'bold'), text = "Soft Drink", bd=10).grid(row = 0,sticky=W)

Snack4 = Checkbutton(fSnack, text = SnackList[4], variable = VarSnackList[4], onvalue = 1, offvalue=0,font=('TH Sarabun New',18,'bold')
                      , command=lambda:chkbutton_value(VarSnackList[4], txtSoftdrink1, EntrySnackList[4])).grid(row= 1, sticky=W)

Snack5 = Checkbutton(fSnack, text = SnackList[5], variable = VarSnackList[5], onvalue = 1, offvalue=0,font=('TH Sarabun New',18,'bold')
                      , command=lambda:chkbutton_value(VarSnackList[5], txtSoftdrink2, EntrySnackList[5])).grid(row= 2, sticky=W)

Snack6 = Checkbutton(fSnack, text = SnackList[6], variable = VarSnackList[6], onvalue = 1, offvalue=0,font=('TH Sarabun New',18,'bold')
                      , command=lambda:chkbutton_value(VarSnackList[6], txtSoftdrink3, EntrySnackList[6])).grid(row= 3, sticky=W)

Snack7 = Checkbutton(fSnack, text = SnackList[7], variable = VarSnackList[7], onvalue = 1, offvalue=0,font=('TH Sarabun New',18,'bold')
                      , command=lambda:chkbutton_value(VarSnackList[7], txtSoftdrink4, EntrySnackList[7])).grid(row= 4, sticky=W)

Snack8 = Checkbutton(fSnack, text = SnackList[8], variable = VarSnackList[8], onvalue = 1, offvalue=0,font=('TH Sarabun New',18,'bold')
                      , command=lambda:chkbutton_value(VarSnackList[8], txtSoftdrink5, EntrySnackList[8])).grid(row= 5, sticky=W) 

LabelSnack = Label(fTicket,font=('TH Sarabun new',20,'bold'), text = "Set", bd=10).grid(row = 0, column = 2, sticky=W)

Snack9 = Checkbutton(fTicket, text = SnackList[9], variable = VarSnackList[9], onvalue = 1, offvalue=0,font=('TH Sarabun New',18,'bold')
                      , command=lambda:chkbutton_value(VarSnackList[9], txtSet1, EntrySnackList[9])).grid(row= 1, column = 2, sticky=W) 

Snack10 = Checkbutton(fTicket, text = SnackList[10], variable = VarSnackList[10], onvalue = 1, offvalue=0,font=('TH Sarabun New',18,'bold')
                      , command=lambda:chkbutton_value(VarSnackList[10], txtSet2, EntrySnackList[10])).grid(row= 2, column = 2, sticky=W)

Snack11 = Checkbutton(fTicket, text = SnackList[11], variable = VarSnackList[11], onvalue = 1, offvalue=0,font=('TH Sarabun New',18,'bold')
                      , command=lambda:chkbutton_value(VarSnackList[11], txtSet3, EntrySnackList[11])).grid(row= 3, column = 2, sticky=W)  

LabelSnack = Label(fSnack,font=('TH Sarabun new',20,'bold'), text = "Appetizer", bd=10).grid(row = 0, column = 2, sticky=W)

Snack12 = Checkbutton(fSnack, text = SnackList[12], variable = VarSnackList[12], onvalue = 1, offvalue=0,font=('TH Sarabun New',18,'bold')
                      , command=lambda:chkbutton_value(VarSnackList[12], txtAppe1, EntrySnackList[12])).grid(row= 1, column = 2, sticky=W)

Snack13 = Checkbutton(fSnack, text = SnackList[13], variable = VarSnackList[13], onvalue = 1, offvalue=0,font=('TH Sarabun New',18,'bold')
                      , command=lambda:chkbutton_value(VarSnackList[13], txtAppe2, EntrySnackList[13])).grid(row= 2, column = 2, sticky=W)


#============================================================ Entry Snack Infomation ============================================================
txtPopcorn1 = Entry(fTicket, font=('TH Sarabun New',16,'bold'), bd = 3, width = 8, justify='center', textvariable = EntrySnackList[0], state = DISABLED)
txtPopcorn1.grid(row = 5, column =1)

txtPopcorn2 = Entry(fTicket, font=('TH Sarabun New',16,'bold'), bd = 3, width = 8, justify='center', textvariable = EntrySnackList[1], state = DISABLED)
txtPopcorn2.grid(row = 6, column =1)

txtPopcorn3 = Entry(fTicket, font=('TH Sarabun New',16,'bold'), bd = 3, width = 8, justify='center', textvariable = EntrySnackList[2], state = DISABLED)
txtPopcorn3.grid(row = 7, column =1)

txtPopcorn4 = Entry(fTicket, font=('TH Sarabun New',16,'bold'), bd = 3, width = 8, justify='center', textvariable = EntrySnackList[3], state = DISABLED)
txtPopcorn4.grid(row = 8, column =1)

txtSoftdrink1 = Entry(fSnack, font=('TH Sarabun New',16,'bold'), bd = 3, width = 8, justify='center', textvariable = EntrySnackList[4], state = DISABLED)
txtSoftdrink1.grid(row = 1, column =1)

txtSoftdrink2 = Entry(fSnack, font=('TH Sarabun New',16,'bold'), bd = 3, width = 8, justify='center', textvariable = EntrySnackList[5], state = DISABLED)
txtSoftdrink2.grid(row = 2, column =1)

txtSoftdrink3 = Entry(fSnack, font=('TH Sarabun New',16,'bold'), bd = 3, width = 8, justify='center', textvariable = EntrySnackList[6], state = DISABLED)
txtSoftdrink3.grid(row = 3, column =1)

txtSoftdrink4 = Entry(fSnack, font=('TH Sarabun New',16,'bold'), bd = 3, width = 8, justify='center', textvariable = EntrySnackList[7], state = DISABLED)
txtSoftdrink4.grid(row = 4, column =1)

txtSoftdrink5 = Entry(fSnack, font=('TH Sarabun New',16,'bold'), bd = 3, width = 8, justify='center', textvariable = EntrySnackList[8], state = DISABLED)
txtSoftdrink5.grid(row = 5, column =1) 

txtSet1 = Entry(fTicket, font=('TH Sarabun New',16,'bold'), bd = 3, width = 8, justify='center', textvariable = EntrySnackList[9], state = DISABLED)
txtSet1.grid(row = 1, column = 3) 

txtSet2 = Entry(fTicket, font=('TH Sarabun New',16,'bold'), bd = 3, width = 8, justify='center', textvariable = EntrySnackList[10], state = DISABLED)
txtSet2.grid(row = 2, column = 3) 

txtSet3 = Entry(fTicket, font=('TH Sarabun New',16,'bold'), bd = 3, width = 8, justify='center', textvariable = EntrySnackList[11], state = DISABLED)
txtSet3.grid(row = 3, column = 3) 

txtAppe1 = Entry(fSnack, font=('TH Sarabun New',16,'bold'), bd = 3, width = 8, justify='center', textvariable = EntrySnackList[12], state = DISABLED)
txtAppe1.grid(row = 1, column = 3) 

txtAppe2 = Entry(fSnack, font=('TH Sarabun New',16,'bold'), bd = 3, width = 8, justify='center', textvariable = EntrySnackList[13], state = DISABLED)
txtAppe2.grid(row = 2, column = 3) 

#============================================================ Frame Receipt Information ============================================================

txtTotal = Text(ftotal, font=('TH Sarabun New',50,'bold'), width= 17, height = 0, bg="white", state = DISABLED)
txtTotal.grid()

txtReceipt = Text(fReceipt, font=('TH Sarabun New',16,'bold'), width= 55, height=13, bg="lightcyan2", state = DISABLED)
txtReceipt.grid(row=1,column=0)

#============================================================= Show value Calculate Infomation ===================================================

LabelCostofTicket = Label(fInfo1, font = ('TH Sarabun New',18,'bold'), text="Cost of Tickets", bd=8).grid(row=0, column=0, sticky=W)
txtCostofTicket = Entry(fInfo1, font = ('TH Sarabun New',18,'bold'), bd=2, width = 19, bg = 'light gray', justify='left', textvariable = CostofTicket).grid(row=0, column=1, sticky=W)

LabelCostofSnack = Label(fInfo1, font = ('TH Sarabun New',18,'bold'), text="Cost of Snack", bd=8).grid(row=1, column=0, sticky=W)
txtCostofSnack = Entry(fInfo1, font = ('TH Sarabun New',18,'bold'), bd=2, width = 19, bg = 'light gray', justify='left', textvariable = CostofSnack).grid(row=1, column=1, sticky=W)

LabelPaidTax = Label(fInfo2, font = ('TH Sarabun New',18,'bold'), text="Paid Tax", bd=8).grid(row=0, column=0, sticky=W)
txtPaidTax = Entry(fInfo2, font = ('TH Sarabun New',18,'bold'), bd=2, width = 19, bg = 'light gray', justify='left', textvariable = PaidTax).grid(row=0, column=1, sticky=W)

LabelSubtotal = Label(fInfo2, font = ('TH Sarabun New',18,'bold'), text="Subtotal", bd=8).grid(row=1, column=0, sticky=W)
txtSubtotal = Entry(fInfo2, font = ('TH Sarabun New',18,'bold'), bd=2, width = 19, bg = 'light gray', justify='left', textvariable = Subtotal).grid(row=1, column=1, sticky=W)

LabelCash = Label(fInfo3, font = ('TH Sarabun New',18,'bold'), fg = 'red', text="Cash", bd=8).grid(row=0, column=0, sticky=W)
txtCash = Entry(fInfo3, font = ('TH Sarabun New',18,'bold'), bd=2, width = 20, justify='left', textvariable = Cash).grid(row=0, column=1, sticky=W)

LabelLicensePlate = Label(fInfo3, font = ('TH Sarabun New',18,'bold'), fg = 'red', text="License Plate", bd=8).grid(row=1, column=0, sticky=W)
txtLicensePlate = Entry(fInfo3, font = ('TH Sarabun New',18,'bold'), bd=2, width = 20, justify='left', textvariable = LicensePlate).grid(row=1, column=1, sticky=W)

#============================================================ Button for Function ============================================================
btnEnter = Button(fInfo4, padx = 30, fg="white",font=('TH Sarabun New',26,'bold'),width=4, height = 2, bg = 'red3',
                text="Enter",command = Enter).grid(rowspan = 2,column = 2)

btnTotal = Button(fInfo4,padx=45, fg="white",font=('TH Sarabun New',20,'bold'),width=5, bg = 'forest green',
                text="Total",command = CostofItem).grid(row = 0, column = 0)

btnReceipt = Button(fInfo4,padx=45, fg="white",font=('TH Sarabun New',20,'bold'),width=5, bg = 'dodgerblue3',
                text="Receipt",command = Receipt).grid(row = 0, column = 1)

btnReset = Button(fInfo4,padx=45, fg="white",font=('TH Sarabun New',20,'bold'),width=5, bg = 'gray30',
                text="Reset",command = Reset).grid(row = 1, column = 1)

btnExit = Button(fInfo4, padx = 45, fg="white",font=('TH Sarabun New',20,'bold'),width=5, bg = 'red3',
                text="Exit",command = qExit).grid(row = 1, column = 0)

root.mainloop()