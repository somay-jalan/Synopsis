'''print(''          PASSWORD GENERATOR AND MANAGER \n'
MENU-\n
Generate a password---1\n
Save a password---2\n
Show a pre-saved password---3\n
Check if a password is strong---4\n
Delete an existing password---5
Change a password associated to a name---6'')'''

host='localhost'
user='somay'
import time
def strongpassword(passwrd):
    mainnum=0
    uppernum=0
    lowernum=0
    digitnum=0
    spcharnum=0
    if len(passwrd)>=8:
        mainnum+=1
    for j in range(0,4):
        tempnum=0
        if j==0:
            for i in passwrd:
                if i.isupper()==1:
                    tempnum+=1                   
            if tempnum>0:
                mainnum+=1
            else:
                uppernum+=1
        elif j==1:
            for i in passwrd:
                if i.islower()==1:
                    tempnum+=1 
            if tempnum>0:
                mainnum+=1
            else:
                lowernum+=1
        elif j==2:
            for i in passwrd:
                if i.isdigit()==1:
                    tempnum+=1 
            if tempnum>0:
                mainnum+=1
            else:
                digitnum+=1
        elif j==3:
            for i in passwrd:
                if i.isdigit()==0 and i.isalpha()==0:
                    tempnum+=1 
            if tempnum>0:
                mainnum+=1
            else:
                spcharnum+=1
        else:
            pass
    if mainnum==5:
        val='It is a strong password.\n'
    else:
        val='It is not a strong password.\n'
    return val        
def passwordgenerator(passwrdlen):
    import random
    passwrd=''
    initialval='False'
    passwrdlen=int(passwrdlen)
    if passwrdlen>3:
        while initialval=='False':
            passwrdtemp=''
            for i in range(0,passwrdlen):
                passwrdtemp+=chr(random.randint(33,126))
            mainnum=0
            for j in range(0,4):
                tempnum=0
                if j==0:
                    for i in passwrdtemp:
                        if i.isupper()==1:
                            tempnum+=1                   
                    if tempnum>0:
                        mainnum+=1
                elif j==1:
                    for i in passwrdtemp:
                        if i.islower()==1:
                            tempnum+=1 
                    if tempnum>0:
                        mainnum+=1
                elif j==2:
                    for i in passwrdtemp:
                        if i.isdigit()==1:
                            tempnum+=1 
                    if tempnum>0:
                        mainnum+=1
                elif j==3:
                    for i in passwrdtemp:
                        if i.isdigit()==0 and i.isalpha()==0:
                            tempnum+=1 
                    if tempnum>0:
                        mainnum+=1
                else:
                    pass    
            if mainnum==4:
                initialval='True'
                passwrd=passwrdtemp
    else:
        for i in range(0,passwrdlen):
            passwrd+=chr(random.randint(33,126))
    return passwrd

def savepassword(passwrd,passwrdname):  
    import mysql.connector
    mydb=mysql.connector.connect(host=host,user=user,passwd=sqlpass)
    mycursor=mydb.cursor()
    mycursor.execute('show databases')
    list1=[]
    for i in mycursor:
        list1+=[i[0]]
    if ('synopsis' in list1):
        pass
    else:
        mycursor.execute('create database synopsis')
    mycursor.execute('use synopsis')
    mycursor.execute('show tables')
    list2=[]
    for i in mycursor:
        list2+=[i[0]]
    if ('passdata' in list2):
        pass
    else:
            mycursor.execute('create table passdata ( passwordname varchar(1000), password varchar(10000))')  
    mycursor.execute('select * from passdata')
    list3=[]
    for i in mycursor:
        list3+=[i[0]]
    val=''    
    if (passwrdname in list3):
        val='This name already exits choose another name'
    else:
        listpasswrd=[]
        listpasswrdname=[]
        for i in passwrdname:
            listpasswrdname+=[str(ord(i))]
        randstr1=''
        for i in listpasswrdname:
            randstr1+=i
        for i in passwrd:
            listpasswrd+=[str(ord(i)+100)]    
        randstr2=''
        for i in listpasswrd:
            randstr2+=i
        randpass=int(randstr1)*int(randstr2)
        mycursor.execute('insert into passdata values("'+passwrdname+'",'+str(randpass)+')')
        mydb.commit()
        val='Password saved successfully!'
    return val

def checkpassword(passwrdname):
    import mysql.connector
    mydb=mysql.connector.connect(host=host,user=user,passwd=sqlpass)
    mycursor=mydb.cursor()
    mycursor.execute('show databases')
    list1=[]
    for i in mycursor:
        list1+=[i[0]]
    if ('synopsis' in list1):
        pass
    else:
        mycursor.execute('create database synopsis')
    mycursor.execute('use synopsis')
    mycursor.execute('show tables')
    list2=[]
    for i in mycursor:
        list2+=[i[0]]
    if ('passdata' in list2):
        pass
    else:
            mycursor.execute('create table passdata ( passwordname varchar(1000), password varchar(10000))')
    mycursor.execute('select * from passdata')        
    list3=[]
    passwrd=''
    for i in mycursor:
        list3+=[i[0]]   
    if (passwrdname in list3):
        listpasswrdname=[]
        for i in passwrdname:
            listpasswrdname+=[str(ord(i))]
        randstr1=''
        randpass=''
        for i in listpasswrdname:
            randstr1+=i
        mycursor.execute('select * from passdata where passwordname="'+passwrdname+'"')
        for i in mycursor:
              randpass=str(i[1])      
        randstr2=str(int(randpass)//int(randstr1))
        list1=[]
        for i in randstr2:
            list1+=[i]        
        for j in range(0,len(list1),3):
            tempstr=''
            for i in range(j,j+3):
                tempstr+=list1[i]   
            passwrd+=chr(int(tempstr)-100)
    else:
        passwrd='No password is associated to this name.'
    return passwrd    

def deletepassword(passwrdname):
    import mysql.connector
    mydb=mysql.connector.connect(host=host,user=user,passwd=sqlpass)
    mycursor=mydb.cursor()
    mycursor.execute('show databases')
    list1=[]
    for i in mycursor:
        list1+=[i[0]]
    if ('synopsis' in list1):
        pass
    else:
        mycursor.execute('create database synopsis')
    mycursor.execute('use synopsis')
    mycursor.execute('show tables')
    list2=[]
    for i in mycursor:
        list2+=[i[0]]
    if ('passdata' in list2):
        pass
    else:
            mycursor.execute('create table passdata ( passwordname varchar(1000), password varchar(10000))')
    mycursor.execute('select * from passdata')        
    list3=[]
    val=''
    for i in mycursor:
        list3+=[i[0]]   
    if (passwrdname in list3):
        mycursor.execute('delete from passdata where passwordname="'+passwrdname+'"')
        mydb.commit()
        val='Password deleted succesfully'
    else:
        val='No password associated to name found'
    return val    
def changepassword(passwrdname,passwrd):
    import mysql.connector
    mydb=mysql.connector.connect(host=host,user=user,passwd=sqlpass)
    mycursor=mydb.cursor()
    mycursor.execute('show databases')
    list1=[]
    for i in mycursor:
        list1+=[i[0]]
    if ('synopsis' in list1):
        pass
    else:
        mycursor.execute('create database synopsis')
    mycursor.execute('use synopsis')
    mycursor.execute('show tables')
    list2=[]
    for i in mycursor:
        list2+=[i[0]]
    if ('passdata' in list2):
        pass
    else:
            mycursor.execute('create table passdata ( passwordname varchar(1000), password varchar(10000))')
    mycursor.execute('select * from passdata')        
    list3=[]
    for i in mycursor:
        list3+=[i[0]]
    val=''    
    if (passwrdname in list3):
        listpasswrd=[]
        listpasswrdname=[]
        for i in passwrdname:
            listpasswrdname+=[str(ord(i))]
        randstr1=''
        for i in listpasswrdname:
            randstr1+=i
        for i in passwrd:
            listpasswrd+=[str(ord(i)+100)]    
        randstr2=''
        for i in listpasswrd:
            randstr2+=i
        randpass=int(randstr1)*int(randstr2)
        mycursor.execute('update passdata set password="'+str(randpass)+'" where passwordname="'+passwrdname+'"')
        mydb.commit()
        val='Password changed successfully!'
    else:
        val='No password associated to name found'
    return val    
        
#-------TKINTER ttk------



from tkinter import *
from tkinter import messagebox
def uselessmain():
    time.sleep(0.1)
    maintk()
def uselessgenerator():
    time.sleep(0.01)
    genpasswrdscreen()
def uselesssecondscreen():
    time.sleep(0.01)
    secondscreen()
def uselesssavepasswrdscreen(passwordinsert=''):
    time.sleep(0.01)
    savepasswrdscreen(passwordinsert1=passwordinsert)
def uselesscheckpasswrdscreen():
    time.sleep(0.01)
    checkpasswrdscreen()
def uselesschangepasswordscreen():
    time.sleep(0.01)
    changepasswordscreen()
def uselessdeletepasswordscreen():
    time.sleep(0.01)
    deletepasswordscreen()
def uselessstrongpasswordscreen():
    time.sleep(0.01)
    strongpasswordscreen()
def strongpasswordscreen():    
    def btn_clicked():
        print("Button Clicked")
    def b1_clicked():
        password=entry0.get()
        val=strongpassword(password)
        entry1.delete(0,last=len(entry1.get()))
        entry1.insert(0,val)
    def b2_clicked():
        password=entry0.get()
        window.destroy()
        uselesssavepasswrdscreen(password)     
    def b3_clicked():
        window.destroy()
        uselesssecondscreen()
    window = Tk()
    window.title('Strong password')
    window.geometry("1000x750")
    window.configure(bg = "#ffffff")
    canvas = Canvas(
        window,
        bg = "#ffffff",
        height = 750,
        width = 1000,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"backgroundstrongpasswordscreen.png")
    background = canvas.create_image(
        500.0, 375.0,
        image=background_img)

    img0 = PhotoImage(file = f"img3.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = window.destroy,
        relief = "flat")

    b0.place(
        x = 21, y = 684,
        width = 136,
        height = 37)

    img1 = PhotoImage(file = f"img5.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = b1_clicked,
        relief = "flat")

    b1.place(
        x = 402, y = 522,
        width = 150,
        height = 41)

    img2 = PhotoImage(file = f"img8.png")
    b2 = Button(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = b2_clicked,
        relief = "flat")

    b2.place(
        x = 663, y = 680,
        width = 314,
        height = 41)

    img3 = PhotoImage(file = f"img4.png")
    b3 = Button(
        image = img3,
        borderwidth = 0,
        highlightthickness = 0,
        command = b3_clicked,
        relief = "flat")

    b3.place(
        x = 317, y = 684,
        width = 136,
        height = 37)

    entry0_img = PhotoImage(file = f"img_textBox0.png")
    entry0_bg = canvas.create_image(
        228.0, 483.0,
        image = entry0_img)

    entry0 = Entry(
        bd = 0,
        bg = "#c4c4c4",
        highlightthickness = 0)

    entry0.place(
        x = 83.0, y = 467,
        width = 290.0,
        height = 30)

    entry1_img = PhotoImage(file = f"img_textBox0.png")
    entry1_bg = canvas.create_image(
        717.0, 483.0,
        image = entry1_img)

    entry1 = Entry(
        bd = 0,
        bg = "#c4c4c4",
        highlightthickness = 0)

    entry1.place(
        x = 572.0, y = 467,
        width = 290.0,
        height = 30)

    window.resizable(False, False)
    window.mainloop()

    
def deletepasswordscreen():
    def btn_clicked():
        print("Button Clicked")
    def b2_clicked():
        window.destroy()
        uselesssecondscreen()
    def b0_clicked():
        try:
            passwordname=entry0.get()
            val=deletepassword(passwordname)
            entry0.delete(0,last=len(entry0.get()))
            entry0.insert(0,val)
        except ValueError:
            pass
        except:
            entry0.delete(0,last=len(entry0.get()))            
            is_ok = messagebox.askokcancel(title='syopsis', message=f"WRONG MYSQL PASSWORD")
            if is_ok:
                window.destroy()
                uselessmain()
    window = Tk()
    window.title('Delete password')
    window.geometry("800x600")
    window.configure(bg = "#ffffff")
    canvas = Canvas(
        window,
        bg = "#ffffff",
        height = 600,
        width = 800,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"backgrounddeletepasswordscreen.png")
    background = canvas.create_image(
        400.0, 300.0,
        image=background_img)

    img0 = PhotoImage(file = f"img7.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = b0_clicked,
        relief = "flat")

    b0.place(
        x = 345, y = 445,
        width = 150,
        height = 42)

    img1 = PhotoImage(file = f"img3.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = window.destroy,
        relief = "flat")

    b1.place(
        x = 42, y = 543,
        width = 136,
        height = 37)

    img2 = PhotoImage(file = f"img4.png")
    b2 = Button(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = b2_clicked,
        relief = "flat")

    b2.place(
        x = 642, y = 545,
        width = 136,
        height = 37)

    entry0_img = PhotoImage(file = f"img_textBox0.png")
    entry0_bg = canvas.create_image(
        370.0, 409.0,
        image = entry0_img)

    entry0 = Entry(
        bd = 0,
        bg = "#c4c4c4",
        highlightthickness = 0)

    entry0.place(
        x = 241.0, y = 393,
        width = 258.0,
        height = 30)

    window.resizable(False, False)
    window.mainloop()
def changepasswordscreen():
    def btn_clicked():
        print("Button Clicked")
    def b2_clicked():
        window.destroy()
        uselesssecondscreen()
    def b0_clicked():
        try:    
            password=entry0.get()
            passwordname=entry1.get()
            val=changepassword(passwordname,password)
            entry0.delete(0,last=len(entry0.get()))
            entry1.delete(0,last=len(entry1.get()))
            entry1.insert(0,val)
        except ValueError:
            pass
        except:
            entry0.delete(0,last=len(entry0.get()))
            entry1.delete(0,last=len(entry1.get()))            
            is_ok = messagebox.askokcancel(title='syopsis', message=f"WRONG MYSQL PASSWORD")
            if is_ok:
                window.destroy()
                uselessmain()
        
    window = Tk()
    window.title('Change password')
    window.geometry("800x600")
    window.configure(bg = "#ffffff")
    canvas = Canvas(
        window,
        bg = "#ffffff",
        height = 600,
        width = 800,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"backgroundchangepasswordscreen.png")
    background = canvas.create_image(
        400.0, 300.0,
        image=background_img)

    img0 = PhotoImage(file = f"img6.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = b0_clicked,
        relief = "flat")

    b0.place(
        x = 345, y = 445,
        width = 150,
        height = 42)

    img1 = PhotoImage(file = f"img3.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = window.destroy,
        relief = "flat")

    b1.place(
        x = 42, y = 543,
        width = 136,
        height = 37)

    img2 = PhotoImage(file = f"img4.png")
    b2 = Button(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = b2_clicked,
        relief = "flat")

    b2.place(
        x = 642, y = 545,
        width = 136,
        height = 37)

    entry0_img = PhotoImage(file = f"img_textBox0.png")
    entry0_bg = canvas.create_image(
        592.0, 409.0,
        image = entry0_img)

    entry0 = Entry(
        bd = 0,
        bg = "#c4c4c4",
        highlightthickness = 0)

    entry0.place(
        x = 463.0, y = 393,
        width = 258.0,
        height = 30)

    entry1_img = PhotoImage(file = f"img_textBox0.png")
    entry1_bg = canvas.create_image(
        186.0, 409.0,
        image = entry1_img)

    entry1 = Entry(
        bd = 0,
        bg = "#c4c4c4",
        highlightthickness = 0)

    entry1.place(
        x = 57.0, y = 393,
        width = 258.0,
        height = 30)

    window.resizable(False, False)
    window.mainloop()

def checkpasswrdscreen():
    def btn_clicked():
        print("Button Clicked")
    def b2_clicked():
        window.destroy()
        uselesssecondscreen()
    def b0_clicked():
        try:    
            name=entry1.get()
            password=checkpassword(name)
            entry0.delete(0,last=len(entry0.get()))
            entry0.insert(0,password)
        except ValueError:
            pass
        except:
            entry0.delete(0,last=len(entry0.get()))
            entry1.delete(0,last=len(entry1.get()))            
            is_ok = messagebox.askokcancel(title='syopsis', message=f"WRONG MYSQL PASSWORD")
            if is_ok:
                window.destroy()
                uselessmain()
    window = Tk()
    window.title('Check password')
    window.geometry("800x600")
    window.configure(bg = "#ffffff")
    canvas = Canvas(
        window,
        bg = "#ffffff",
        height = 600,
        width = 800,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"backgroundcheckpasswrdscreen.png")
    background = canvas.create_image(
        400.0, 300.0,
        image=background_img)

    entry0_img = PhotoImage(file = f"img_textBox0.png")
    entry0_bg = canvas.create_image(
        592.0, 409.0,
        image = entry0_img)

    entry0 = Entry(
        bd = 0,
        bg = "#c4c4c4",
        highlightthickness = 0)

    entry0.place(
        x = 463.0, y = 393,
        width = 258.0,
        height = 30)

    entry1_img = PhotoImage(file = f"img_textBox0.png")
    entry1_bg = canvas.create_image(
        186.0, 409.0,
        image = entry1_img)

    entry1 = Entry(
        bd = 0,
        bg = "#c4c4c4",
        highlightthickness = 0)

    entry1.place(
        x = 57.0, y = 393,
        width = 258.0,
        height = 30)

    img0 = PhotoImage(file = f"img5.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = b0_clicked,
        relief = "flat")

    b0.place(
        x = 345, y = 445,
        width = 150,
        height = 42)

    img1 = PhotoImage(file = f"img3.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = window.destroy,
        relief = "flat")

    b1.place(
        x = 42, y = 543,
        width = 136,
        height = 37)

    img2 = PhotoImage(file = f"img4.png")
    b2 = Button(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = b2_clicked,
        relief = "flat")

    b2.place(
        x = 642, y = 545,
        width = 136,
        height = 37)

    window.resizable(False, False)
    window.mainloop()


def savepasswrdscreen(passwordinsert1=''):
    def b2_clicked():
        window.destroy()
        uselesssecondscreen()
    def b0_clicked():
        try:    
            passwordname=entry0.get()
            password=entry1.get()
            val=savepassword(password,passwordname)
            entry0.delete(0,last=len(entry0.get()))
            entry1.delete(0,last=len(entry1.get()))
            entry0.insert(0,val)
        except ValueError:
            pass
        except:
            entry0.delete(0,last=len(entry0.get()))
            entry1.delete(0,last=len(entry1.get()))            
            is_ok = messagebox.askokcancel(title='syopsis', message=f"WRONG MYSQL PASSWORD")
            if is_ok:
                window.destroy()
                uselessmain()
    def btn_clicked():
        print("Button Clicked")
    window = Tk()
    window.geometry("800x600")
    window.title('Save password')    
    window.configure(bg = "#ffffff")
    canvas = Canvas(
        window,
        bg = "#ffffff",
        height = 600,
        width = 800,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"backgroundsavepasswrdscreen.png")
    background = canvas.create_image(
        400.0, 300.0,
        image=background_img)

    entry0_img = PhotoImage(file = f"img_textBox0.png")
    entry0_bg = canvas.create_image(
        207, 409.0,
        image = entry0_img)

    entry0 = Entry(
        bd = 0,
        bg = "#c4c4c4",
        highlightthickness = 0)

    entry0.place(
        x = 59.0, y = 394,
        width = 290.0,
        height = 30)

    entry1_img = PhotoImage(file = f"img_textBox0.png")
    entry1_bg = canvas.create_image(
        592.0, 409.0,
        image = entry1_img)

    entry1 = Entry(
        bd = 0,
        bg = "#c4c4c4",
        highlightthickness = 0)

    entry1.place(
        x = 463.0, y = 393,
        width = 258.0,
        height = 30)
    entry1.insert(0,passwordinsert1)
    img0 = PhotoImage(file = f"img0.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = b0_clicked,
        relief = "flat")

    b0.place(
        x = 345, y = 445,
        width = 150,
        height = 42)

    img1 = PhotoImage(file = f"img3.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = window.destroy,
        relief = "flat")

    b1.place(
        x = 42, y = 543,
        width = 136,
        height = 37)

    img2 = PhotoImage(file = f"img4.png")
    b2 = Button(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = b2_clicked,
        relief = "flat")

    b2.place(
        x = 642, y = 545,
        width = 136,
        height = 37)

    window.resizable(False, False)
    window.mainloop()

    
def genpasswrdscreen():
    window = Tk()
    window.geometry("800x600")
    window.title('Password generator')
    window.configure(bg = "#ffffff")
    canvas = Canvas(
        window,
        bg = "#ffffff",
        height = 600,
        width = 800,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)
    def save_clicked():
        passwordgen=entry1.get()
        window.destroy()
        uselesssavepasswrdscreen(passwordinsert=passwordgen)
    def generate_clicked():
        passwrd=''
        passwordlen=entry0.get()
        passwrd=passwordgenerator(passwordlen)
        entry1.delete(0,last=len(entry1.get()))
        entry1.insert(0,passwrd)
    def menu_clicked():
        window.destroy()
        uselesssecondscreen()
    background_img = PhotoImage(file = f"backgroundgenpasswrdscreen.png")
    background = canvas.create_image(
        400.0, 300.0,
        image=background_img)

    img0 = PhotoImage(file = f"img3.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = window.destroy,
        relief = "flat")

    b0.place(
        x = 24, y = 547,
        width = 136,
        height = 37)

    img1 = PhotoImage(file = f"img1genpasswrdscreen.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command =generate_clicked ,
        relief = "flat")

    b1.place(
        x = 324, y = 451,
        width = 150,
        height = 42)

    img2 = PhotoImage(file = f"img8.png")
    b2 = Button(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = save_clicked,
        relief = "flat")

    b2.place(
        x = 479, y = 547,
        width = 314,
        height = 41)
    
    img3 = PhotoImage(file = f"img4.png")
    b3 = Button(
        image = img3,
        borderwidth = 0,
        highlightthickness = 0,
        command =menu_clicked,
        relief = "flat")

    b3.place(
        x = 234, y = 549,
        width = 136,
        height = 37)

    entry0_img = PhotoImage(file = f"img_textBox0.png")
    entry0_bg = canvas.create_image(
        203.0, 415.0,
        image = entry0_img)

    entry0 = Entry(
        bd = 0,
        bg = "#c4c4c4",
        highlightthickness = 0)

    entry0.place(
        x = 58.0, y = 399,
        width = 290.0,
        height = 30)

    entry1_img = PhotoImage(file = f"img_textBox0.png")
    entry1_bg = canvas.create_image(
        603.0, 415.0,
        image = entry1_img)

    entry1 = Entry(
        bd = 0,
        bg = "#c4c4c4",
        highlightthickness = 0)

    entry1.place(
        x = 458.0, y = 399,
        width = 290.0,
        height = 30)
    window.resizable(False, False)
    window.mainloop()
def secondscreen():
    def b5_clicked():
        window1.destroy()
        uselessgenerator()
    def b6_clicked():
        window1.destroy()
        uselesssavepasswrdscreen()
    def b0_clicked():
        window1.destroy()
        uselesscheckpasswrdscreen()
    def b1_clicked():
        window1.destroy()
        uselesschangepasswordscreen()
    def b2_clicked():
        window1.destroy()
        uselessdeletepasswordscreen()
    def b4_clicked():
        window1.destroy()
        uselessstrongpasswordscreen()
    window1= Tk()
    window1.title('Menu')
    window1.geometry("800x600")
    window1.configure(bg = "#ffffff")
    canvas = Canvas(
        window1,
        bg = "#ffffff",
        height = 600,
        width = 800,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"backgroundsecond.png")
    background = canvas.create_image(
        437.5, 300.0,
        image=background_img)

    img0 = PhotoImage(file = f"img0second.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = b0_clicked,
        relief = "flat")

    b0.place(
        x = 307, y = 464,
        width = 35,
        height = 35)

    img1 = PhotoImage(file = f"img0second.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = b1_clicked,
        relief = "flat")

    b1.place(
        x = 417, y = 399,
        width = 35,
        height = 35)

    img2 = PhotoImage(file = f"img0second.png")
    b2 = Button(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = b2_clicked,
        relief = "flat")

    b2.place(
        x = 725, y = 329,
        width = 35,
        height = 35)

    img3 = PhotoImage(file = f"img3.png")
    b3 = Button(
        image = img3,
        borderwidth = 0,
        highlightthickness = 0,
        command = window1.destroy,
        relief = "flat")

    b3.place(
        x = 328, y = 529,
        width = 136,
        height = 37)

    img4 = PhotoImage(file = f"img0second.png")
    b4 = Button(
        image = img4,
        borderwidth = 0,
        highlightthickness = 0,
        command = b4_clicked,
        relief = "flat")

    b4.place(
        x = 720, y = 464,
        width = 35,
        height = 35)

    img5 = PhotoImage(file = f"img0second.png")
    b5 = Button(
        image = img5,
        borderwidth = 0,
        highlightthickness = 0,
        command = b5_clicked,
        relief = "flat")

    b5.place(
        x = 325, y = 329,
        width = 35,
        height = 35)
    img6 = PhotoImage(file = f"img0second.png")
    b6 = Button(
        image = img6,
        borderwidth = 0,
        highlightthickness = 0,
        command = b6_clicked,
        relief = "flat")

    b6.place(
        x = 719, y = 399,
        width = 35,
        height = 35)

    window1.resizable(False, False)
    window1.mainloop()
sqlpass=''
def maintk():   
    def btn_clicked():
        if entry.get()=='':
            entry.insert(0,'Please enter your sql password')
        else:
            global sqlpass
            sqlpass=entry.get()
            window.destroy()
            uselesssecondscreen()
    window = Tk()
    window.title('Sql password')
    window.geometry("800x600")
    window.configure(bg = "#ffffff")

    canvas = Canvas(
        window,
        bg = "#ffffff",
        height = 600,
        width = 800,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)


    entry = Entry(
        bd = 0,
        bg = "#9c9797",
        highlightthickness = 0)

    entry.place(
        x = 230.0, y = 450,
        width = 365.0,
        height = 35)

    img = PhotoImage(file = f"img0main.png")
    b = Button(
        image = img,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b.place(
        x = 332, y = 509,
        width = 135,
        height = 40)

    background_img = PhotoImage(file = f"backgroundmain.png")
    background = canvas.create_image(
        400.0, 300.0,
        image=background_img)

    window.resizable(False, False)
    window.mainloop()    
maintk()    




























    
