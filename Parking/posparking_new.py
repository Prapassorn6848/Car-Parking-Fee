from tkinter import *
from tkinter import messagebox
import random
import time
import os
from ftplib import FTP
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


root = Tk()
root.geometry("1540x800+0+0")
root.title("Pos Carpaking")
root.configure(background='white')
# create all of the main containers
top_frame = Frame(root, bg='cyan', width=450, height=50, pady=3)
center = Frame(root, bg='gray2', width=50, height=40, padx=3, pady=3)
btm_frame = Frame(root, bg='white', width=450, height=45, pady=3)
btm_frame1 = Frame(root, bg='white', width=450, height=45, pady=3)
btm_frame2 = Frame(root, bg='lavender', width=450, height=60, pady=3)

# layout all of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

top_frame.grid(row=0, sticky="ew")
center.grid(row=1, sticky="nsew")
btm_frame.grid(row=3, sticky="w")
btm_frame1.grid(row=3, sticky="e")
btm_frame2.grid(row=4, sticky="ew")

NamePlate = Label(top_frame,font=('TH Sarabun new',50,'bold'),bg='cyan', fg='black',text = "POS PARKING                               TOTAL")
NamePlate.grid(row=0, column=0, padx=10, pady=5)
center.grid_rowconfigure(0, weight=1)
center.grid_columnconfigure(1, weight=1)
ctr_left = Frame(center, bg='honeydew2', width=770, height=190)
ctr_right = Frame(center, bg='honeydew2', width=1000, height=190)

ctr_left.grid(row=0, column=0, sticky="nswe")
ctr_right.grid(row=0, column=1, sticky="ns")

TimeLabel = Label(ctr_left,font = ('calibri', 70, 'bold'),
            background = 'purple',
            foreground = 'white')
TimeLabel.grid(rowspan=2, columnspan=3, padx=10, pady=5)

NamePark = Label(ctr_left,font=('TH Sarabun new',50,'bold'), fg='BLack',text = "  เลขทะเบียนรถยนต์  ",bg="honeydew2")
NamePark.grid(row=2,column=0) 
eieiframe = Frame(ctr_left, bg='honeydew2', width=770, height=1, pady=3)
eieiframe.grid(row=3, sticky="ew")

################################################ Function Button ##################################################
def Reset():
    txtTotal.configure(state = NORMAL)
    txtTotal2.configure(state = NORMAL)
    txtTotal3.configure(state = NORMAL)
    txtTotal.delete("1.0",END)
    txtTotal2.delete("1.0",END)
    txtTotal3.delete("1.0",END)
    licenseCarList[0].set("")
    txtTotal.configure(state = DISABLED)
    txtTotal2.configure(state = DISABLED)
    txtTotal3.configure(state = DISABLED)
    
def AskforSenddata():
    DateofOrder = StringVar()
    DateofOrder.set(time.strftime("%d/%m/%Y"))
    checkforSend = 0
    AskforSend = messagebox.askyesno("Send Data", "It's "+str(time.strftime('%H'))+":"+str(time.strftime('%M'))+" now.\nDo you want to Send Email?")
    if AskforSend:
        msg = MIMEMultipart()
        msg['From'] = "ratchapol.at@ku.th"
        msg['To'] = "nitiwat.ko@ku.th"
        msg['Subject'] = "ข้อมูลการชำระประจำวันที่ " + str(DateofOrder.get())
        email_message = "ข้อมูลการชำระประจำวันที่ " + str(DateofOrder.get())
        body = email_message
        msg.attach(MIMEText(body, 'plain'))
        filename = "history.txt"
        attachment = open(filename, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(part)
        text = msg.as_string()
        try:
            input = open("account.txt")
            for line in input:
                ac, pas, re = line.split(';')
            input.close()
            try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                try:
                    server.login(ac, pas)
                    server.sendmail(ac, re, text)
                    print("Successfully")
                except:
                    print("Incorrect")
                finally:
                    print("Quit Server")
                    server.quit()
            except:
                print("server not found")
        except:
            print("file not found")
    
        try:
            history = open('history.txt','w',encoding="utf-8")
        except:
            print("Can't open or find file!!")
        else:
            history.write('ทะเบียนรถ - เข้า - ออก - ค่าจอดรถ\n')
        history.close()
    

####################################List##########################################

licenseCarList0 = StringVar()
licenseCarList1 = StringVar()
licenseCarList2 = StringVar()
licenseCarList = [licenseCarList0, licenseCarList1, licenseCarList2]

def CalPrice(Hi,Mi,Ho,Mo,Cost):
    if Hi == Ho:
        timepark = Mo-Mi
    elif Ho>Hi:
        hour = Ho-Hi
        hour = (hour*60)+Mo 
        timepark = hour - Mi
    else:
        Ho = Ho + 24
        hour = Ho-Hi
        hour = (hour*60)+Mo 
        timepark = hour - Mi
        
        
    if Cost > 1000:
        total = 0
    elif Cost >= 100:
        timepark = timepark-60
        if timepark<0:
            timepark = 0
        minpark = timepark%60
        if minpark<=30:
            timepark = timepark//60
            total = timepark*30
        else:
            timepark+=60
            timepark = timepark//60
            total = timepark*30
    else:
        minpark = timepark%60
        if minpark<=30:
            timepark = timepark//60
            total = timepark*30
        else:
            timepark+=60
            timepark = timepark//60
            total = timepark*30
    return total
    
def CarIn() :
    txtTotal.configure(state = NORMAL)
    txtTotal2.configure(state = NORMAL)
    txtTotal3.configure(state = NORMAL)
    DateofOrder = StringVar()
    time_string = StringVar()
    DateofOrder.set(time.strftime("%d/%m/%Y"))
    time_string.set(time.strftime('%H:%M:%S'))
    NumPlate = str(txtlicenseCar.get())
    
    checkRepeat = 1
    
    if NumPlate != "" :
        txtTotal.delete("1.0",END)
        txtTotal2.delete("1.0",END)
        txtTotal3.delete("1.0",END)
        txtTotal.insert(END,'เลขทะเบียน  '+NumPlate +'\n')
        txtTotal2.insert(END,'เวลาเข้าลานจอดรถยนต์   ' + time_string.get()+"\n")
        txtTotal2.insert(END,'วันที่เข้าลานจอดรถยนต์   ' + DateofOrder.get()+"\n")
        txtTotal3.insert(END,'          ยินดีต้อนรับค่ะ\n') 
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
                downloadFile('Bill.txt')
                
                #***************** Check Repeat Car IN ****************************************************
                
                try:
                    bil = open("Bill.txt",'r',encoding = "utf-8")
                except IOError:
                    print("Can not find file or read data")
                else:
                    for line in bil:
                        LPP,Cost,state = line.split(";")
                        if NumPlate == LPP and int(state) < 2 :
                            checkRepeat = 0
                        if NumPlate == LPP and int(state) == 2 :
                            checkRepeat = 1
                    bil.close()
                    
                #***********************************************************************************
                
                if checkRepeat == 1 :
                    Bill = open('Bill.txt','a',encoding="utf-8")
                    Bill.write(NumPlate + ';0.0;0\n')
                    Bill.close()
                    uploadFile('Bill.txt')
                    
                else :
                    txtTotal.delete("1.0",END)
                    txtTotal2.delete("1.0",END)
                    txtTotal3.delete("1.0",END)
                    txtTotal2.insert(END,'มีรถยนต์คันนี้อยู่แล้ว  \n') 
                    txtTotal2.insert(END,'โปรดตรวจสอบอีกครั้ง  \n') 
                ftp.close()
            login.close()
        try:
            InCar = open('InCar.txt','a',encoding="utf-8")
        except:
            print("Can't open or find file!!")
        else:
            InCar.write(NumPlate + ';' + time.strftime('%H') + ';' + time.strftime('%M') + '\n')
            InCar.close()
    txtTotal.configure(state = DISABLED)
    txtTotal2.configure(state = DISABLED)
    txtTotal3.configure(state = DISABLED)
    
def CarOut():
    txtTotal.configure(state = NORMAL)
    txtTotal2.configure(state = NORMAL)
    txtTotal3.configure(state = NORMAL)
    DateofOrder = StringVar()
    time_string = StringVar()
    DateofOrder.set(time.strftime("%d/%m/%Y"))
    time_string.set(time.strftime('%H:%M:%S'))
    NumPlate = str(txtlicenseCar.get())
    Hour = 0
    Min = 0
    Costed = 0.0
    
    checkCarIn = 0
    if NumPlate != "" :
        
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
                
                def uploadFile(file):
                    try:
                        ftp.storbinary('STOR ' + file, open(file, 'rb'))
                    except:
                        print("Can not upload file")
                
                def downloadFile(filename):
                    try:
                        localfile = open(filename, 'wb')
                        ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
                    except:
                        print("Can not download file!")
                    localfile.close()
                ftp.cwd(firstF)
                ftp.cwd(secondF)
                downloadFile('Bill.txt')
                
                #***************** Check Car IN ****************************************************
                
                try:
                    bil = open("Bill.txt",'r',encoding = "utf-8")
                except IOError:
                    print("Can not find file or read data")
                else:
                    for line in bil:
                        LPP,Cost,state = line.split(";")
                        if NumPlate == LPP and int(state) < 2 :
                            checkCarIn = 1
                        if (NumPlate == LPP and int(state) == 2) :
                            checkCarIn = 0
                    bil.close()
                    
                #***********************************************************************************
                if checkCarIn == 1 :
                    try:
                        billR = open("Bill.txt",'r',encoding = "utf-8")
                    except IOError:
                        print("Can not find file or read data")
                    else:
                        for line in billR:
                            LPP,Cost,state = line.split(";")
                            if NumPlate == LPP:
                                Costed = float(Cost)
                        billR.close()
                    try:
                        billFile = open("Bill.txt", "a", encoding = "utf-8")
                    except IOError:
                        print("Can not find file or read data")
                    else:
                        print("Written content in the file successfully")
                        billFile.write(str(NumPlate) + ";" + str(Costed) + ";2\n")
                    billFile.close()
                    sendFile = "Bill.txt"
                    uploadFile(sendFile)
                ftp.close()
            login.close()
            
        if checkCarIn == 1:   
            try:
                inCar = open('InCar.txt','r',encoding="utf-8")
            except:
                print("Can't open or find file!!")
            else:
                for line in inCar:
                    LP , Hr , Mn = line.split(';')
                    if LP == NumPlate:
                      Hour = int(Hr)
                      Min = int(Mn)
                inCar.close()
            prc = CalPrice(Hour,Min,int(time.strftime('%H')),int(time.strftime('%M')),Costed)
            try:
                OutCar = open('OutCar.txt','a',encoding="utf-8")
            except:
                print("Can't open or find file!!")
            else:
                OutCar.write(NumPlate + ';' +str(Hour)+';'+str(Min)+';'+ time.strftime('%H') + ';' + time.strftime('%M') + ';' + str(prc) + '\n')
            OutCar.close()
            
            
            try:
                history = open('history.txt','a',encoding="utf-8")
            except:
                print("Can't open or find file!!")
            else:
                history.write(NumPlate + ' ' +str('%02d'%Hour)+' : '+str('%02d'%Min)+' - '+ time.strftime('%H') + ' : ' + time.strftime('%M') + ' ราคา ' + str(prc) + '\n')
            history.close()
            
            
            
            if Hour == int(time.strftime('%H')):
                timepark = int(time.strftime('%M'))-Min
            elif int(time.strftime('%H')) >Hour:
                hour = int(time.strftime('%H'))-Hour
                hour = (hour*60)+int(time.strftime('%M')) 
                timepark = hour - Min
            else:
                Ho = int(time.strftime('%H')) + 24
                hour = Ho-Hour
                hour = (hour*60)+int(time.strftime('%M'))
                timepark = hour - Min
            
            txtTotal.delete("1.0",END)
            txtTotal2.delete("1.0",END)
            txtTotal3.delete("1.0",END)
    
            txtTotal.insert(END,'เลขทะเบียน  ' +NumPlate + '\n') 
            txtTotal2.insert(END,'เวลาที่เข้าจอด  ' + str('%02d'%Hour)+ ':'+ str('%02d'%Min) +" น.\n") 
            txtTotal2.insert(END,'เวลาที่ออกจอด  ' + time.strftime('%H')+':'+ time.strftime('%M') + " น.\n")
            timeTotalH = timepark//60
            timeTotalN = timepark%60
            txtTotal2.insert(END,'เวลาที่จอด  ' + str(timeTotalH) + ' ชั่วโมง ' + str(timeTotalN)+" นาที.\n")
            txtTotal3.insert(END,'ค่าจอดรถยนต์  ' +str(prc) + ' บาท \n') 
        else:
            txtTotal.delete("1.0",END)
            txtTotal2.delete("1.0",END)
            txtTotal3.delete("1.0",END)
            txtTotal2.insert(END,'ไม่พบรถยนต์คันนี้  \n') 
            txtTotal2.insert(END,'โปรดตรวจสอบอีกครั้ง  \n') 
    txtTotal.configure(state = DISABLED)
    txtTotal2.configure(state = DISABLED)
    txtTotal3.configure(state = DISABLED)
        
    
def SentTotal() :
    txtTotal.configure(state = NORMAL)
    txtTotal2.configure(state = NORMAL)
    txtTotal3.configure(state = NORMAL)
    AskforSenddata()
    txtTotal.configure(state = DISABLED)
    txtTotal2.configure(state = DISABLED)
    txtTotal3.configure(state = DISABLED)
    
    
def clock():
    hour =time.strftime("%H")
    minute=time.strftime("%M")
    second = time.strftime("%S")
    TimeLabel.config(text=hour + ":" + minute + ":" + second+" น.")
    TimeLabel.after(1000,clock)
clock()



txtTotal = Text(ctr_right, font=('TH Sarabun New',55,'bold'), width= 18, height=1, bg="lavender" , state = DISABLED)
txtTotal.grid(row=3,column=0,padx=20, pady=20)

txtTotal2 = Text(ctr_right, font=('TH Sarabun New',36,'bold'), width= 27, height=3, bg="lightpink" , state = DISABLED)
txtTotal2.grid(row=4,column=0)

txtTotal3 = Text(ctr_right, font=('TH Sarabun New',55,'bold'), width= 18, height=1, bg="darkolivegreen1" , state = DISABLED)
txtTotal3.grid(row=6,column=0,padx=20, pady=20)



txtlicenseCar = Entry(ctr_left, font=('TH Sarabun New',60,'bold'), bd=3, width=10, justify='center' ,textvariable = licenseCarList[0])
txtlicenseCar.grid(row=3, column=0, padx=10, pady=5)




####################################Button##########################################

btnOut = Button(ctr_left, fg="black", font=('TH Sarabun New',26,'bold'),width=20, height = 1, bg = 'green3', text="เข้า",command=CarIn).grid(row =8 ,column = 0,padx=10, pady=5)
btnEnter = Button(ctr_left, fg="black", font=('TH Sarabun New',26,'bold'),width=20, height = 1, bg = 'red3', text="ออก",command=CarOut).grid(row = 9,column = 0,padx=10, pady=5)
btnSentTotal = Button(btm_frame, fg="black", font=('TH Sarabun New',26,'bold'),width=12, height = 1, bg = 'skyblue', text="ส่งยอดประจำวัน",command = SentTotal).grid(row = 10,column = 0,padx=10, pady=5,sticky='E')

btnReset = Button(btm_frame1, fg="white", font=('TH Sarabun New',26,'bold'),width=12, height = 1,  bg = 'gray30', text="รีเซ็ต",command = Reset).grid(row = 10,column = 0,padx=10, pady=5, sticky='E')


root.mainloop()

