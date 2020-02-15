from tkinter import *
import tkinter.filedialog
import tkinter as tk
import sqlite3
from PIL import ImageTk, Image
import time
import sqlite3
from tkinter import ttk
import datetime

global rdir
rdir="/media/dev/Development/DHS Info/Image Processing/pypro/Criminal_Identification-Python_Fingerprint_Matching-SIFT-DHS_Informatics/"
            
currentDT = datetime.datetime.now()

LARGE_FONT= ("Verdana", 12)
global admunm,usrnm
admunm=None
usrnm="None"

##Database initiailization // Connecting
conn = sqlite3.connect('db-sqlite3/teda.db')
with conn:
    cursor=conn.cursor()
#status=StringVar()
#status=""
global status
status=""

class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Criminal Detection")
        self.geometry('500x700')
        #global container
        container = tk.Frame(self)

        #StatusBar(self,"test",)
        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        #lbl_status=StringVar()
        #Label(self,textvariable= self.lbl_status).grid(row=4,column=0,columnspan=2,sticky='W')


        self.frames = {}

        for F in (RootPage, AdminLogin, UserLogin, CrRegister,AdmHmPg,UsrHmPg):

            frame = F(container,self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(RootPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
"""
   def MenAdmHmPg():

        menubar=tk.Menu(container)
        filemenu=Menu(menubar,tearoff=0)
        filemenu.add_command(label="New",command=self.quit)
        filemenu.add_command(label="New",command=self.quit)
        filemenu.add_command(label="New",command=self.quit)
        filemenu.add_command(label="New",command=self.quit)

        #filemenu.add_seperator()
        filemenu.add_command(label="New",command=self.quit)
"""
### Root Page

class RootPage(tk.Frame):
    def printq():
        print ("Hello")

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        self.lbl_status = StringVar(parent)
        self.lbl_status.set("waiting input...")
        Label(self,textvariable= self.lbl_status).grid(row=4,column=0,columnspan=2,sticky='W')


        label_0 = Label(self, text="Criminal Detection",width=20,font=("bold", 20))
        label_0.place(x=100,y=53)

        label_1 = Label(self, text="Login as",width=20,font=("default", 14))
        label_1.place(x=100,y=130)

        #Setting it up
        #admimg = ImageTk.PhotoImage(Image.open("admin.png"))

        #Displaying it
        #imglabel = Label(self, image=admimg)
        #imglabel.place(x=123,y=160)  
        
        Button(self, text='Admin',width=24,bg='brown',fg='white',command=lambda:controller.show_frame(AdminLogin)).place(x=123,y=160)

        #Setting it up
        #usrimg = ImageTk.PhotoImage(Image.open("user.png"))

        #Displaying it
        #imglabel1 = Label(self, image=usrimg)
        #imglabel1.place(x=123,y=280)  

        label_2 = Label(self, text="Or",width=14,font=("default", 9))
        label_2.place(x=175,y=195)

        Button(self, text='User',width=24,bg='brown',fg='white',command=lambda:controller.show_frame(UserLogin)).place(x=123,y=220)
        
""" 
       def messageWindow():
            # create child window
            win = Toplevel()
            # display message
            message = "This is the child window"
            Label(win, text=message).pack()
            # quit child window and return to root window
            # the button is optional here, simply use the corner x of the child window
            Button(win, text='OK', command=win.destroy).pack()
            
        Button(self, text='Test Window',width=24,bg='brown',fg='white',command=messageWindow).place(x=123,y=220)
"""
##Status Bar -Dev
"""
def StatusBar1(status):

    status1 = Label(text=status, bd=1, relief=SUNKEN, anchor=W)
    status1.pack(side=BOTTOM, fill=X)
    #time.sleep(1)

    """

###Admin Login

class AdminLogin(tk.Frame):


    def __init__(self, parent, controller):

        tk.Frame.__init__(self,parent)



        #aunm=StringVar()
        #apwd=StringVar()
        unm=StringVar()
        pwd=StringVar()
        
        def AdmLogCheck():

            unm1=unm.get()
            pwd1=pwd.get()

            row=cursor.execute("SELECT `unm`,`pwd` FROM admin WHERE unm=? and pwd=?",(unm1,pwd1))
            row=cursor.fetchall()
            le=len(row)
            if(le>0):
                #print ("Login Success!")
                cp = Label(self, text="Succesfully Logged in! Redirecting soon..!!",fg='Green',width=40,font=("bold", 10))
                cp.place(x=100,y=100)
                #time.sleep(2)

                """cp = Label(self, text="Succesfully Logged in! Redirecting soon..!!",fg='Green',width=40,font=("bold", 10))
                cp.place(x=100,y=100)
                
                """
                admunm="admin"
                controller.show_frame(AdmHmPg)
            else:
                wp = Label(self, text="Wrong Username or Password!",fg='red',width=40,font=("bold", 10))
                wp.place(x=100,y=100)
                #print("Wrong Cred")

            """cunm="a"
            cpwd="t"

            if(cunm==unm1 and cpwd==pwd1):
                status="Admin Login Success"
                print (status)
                time.sleep(0.5)
                status="Redirecting Now"
                print (status)
                time.sleep(0.5)
                status="Welcome Admin"
                print (status)
                #print("Login Success")
                #StatusBar1("Login Sucess.. Redirecting now")
                #self.variable.set("Login Success")            
            else:
                print("Wrong Cred")"""



        


        label_0 = Label(self, text="Admin Login",width=20,font=("bold", 20))
        label_0.place(x=100,y=53)

        label_1 = Label(self, text="Username :",width=20,font=("bold", 10))
        label_1.place(x=80,y=130)

        unm = Entry(self)
        unm.place(x=240,y=130)

        plbl= Label(self, text="Password :",width=20,font=("bold", 10))
        plbl.place(x=80,y=180)

        pwd = Entry(self,show="*")
        pwd.place(x=240,y=180)

        Button(self, text='Login',width=13,bg='green',fg='white',command=AdmLogCheck).place(x=123,y=230)
        Button(self, text='Cancel',width=13,bg='brown',fg='white',command=lambda:controller.show_frame(RootPage)).place(x=273,y=230)

##Menu
"""
class MenuBar(Tkinter.Menu):
    def __init__(self, parent):
        Tkinter.Menu.__init__(self, parent)

        fileMenu = Tkinter.Menu(self, tearoff=False)
        self.add_cascade(label="File",underline=0, menu=fileMenu)
        fileMenu.add_command(label="Exit", underline=1, command=self.quit)

    def quit(self):
        sys.exit(0)"""

class StatusBar(tk.Frame):   
    def __init__(self, parent,controller):
        tk.Frame.__init__(self, parent)
        self.variable=StringVar()
        #tk.StringVar()        
        self.label=tk.Label(self, bd=1, relief=SUNKEN, anchor=tk.W,
                           textvariable=self.variable,
                           font=('arial',10,'normal'))
        self.variable.set(status)
        #self.variable.set("Test")
        self.label.pack(side=BOTTOM,fill=X)        
        self.pack()
        """status1 = Label(text=status, bd=1, relief=SUNKEN, anchor=W)
        status1.pack(side=BOTTOM, fill=X)
"""

        #Button(self, text='Login',width=24,bg='brown',fg='white',command=lambda:controller.show_frame(Login)).place(x=123,y=160)

        """Button(self, text='Login',width=24,bg='brown',fg='white',command=lambda:controller.show_frame(Login)).place(x=123,y=160)

        label_2 = Label(self, text="Search by FP",width=20,font=("default", 14))
        label_2.place(x=100,y=190)

        Button(self, text='Input FP',width=24,bg='brown',fg='white',command=Register).place(x=123,y=220)


        label_3 = Label(self, text="Search by Face",width=20,font=("default", 14))
        label_3.place(x=100,y=250)

        Button(self, text='Input Face',width=24,bg='brown',fg='white',command=Register).place(x=123,y=280)
"""

"""

class LoginFrame(tk.Frame):
    def __init__(self, parent, controller):
        #super().__init__(master)

        self.label_username = Label(self, text="Username")
        self.label_password = Label(self, text="Password")

        self.entry_username = Entry(self)
        self.entry_password = Entry(self, show="*")

        self.label_username.grid(row=0, sticky=E)
        self.label_password.grid(row=1, sticky=E)
        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)

        self.checkbox = Checkbutton(self, text="Keep me logged in")
        self.checkbox.grid(columnspan=2)

        self.logbtn = Button(self, text="Login", command=self._login_btn_clicked)
        self.logbtn.grid(columnspan=2)

        self.pack()

    def _login_btn_clicked(self):
        # print("Clicked")
        username = self.entry_username.get()
        password = self.entry_password.get()

        # print(username, password)

        if username == "john" and password == "password":
            tk.showinfo("Login info", "Welcome John")
        else:
            tk.showerror("Login error", "Incorrect username")
"""


###Admin Home Page

class AdmHmPg(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        #c=SeaofBTCapp.MenAdmHmPg()
        """
        container = tk.Frame(self)

        StatusBar(self,"test",)
        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        menubar = Menu(self)
        fileMenu = Menu(self)
        recentMenu = Menu(self)

        menubar.add_cascade(label="File", menu=fileMenu)
        fileMenu.add_cascade(label="Open Recent", menu=recentMenu)
        for name in ("file1.txt", "file2.txt", "file3.txt"):
            recentMenu.add_command(label=name)"""
        def AdmAdUsr():
            win = Toplevel()
            win.geometry('500x500')

            unm=StringVar()
            pwd=StringVar()
            Email=StringVar()
            name=StringVar()
            
            def database():

                unm1=unm.get()
                pwd1=pwd.get()
                em1=Email.get()
                nm1=name.get()   
                #cursor.execute('CREATE TABLE IF NOT EXISTS criminal (`ID` INTEGER PRIMARY KEY AUTOINCREMENT,`name` TEXT,`mobile` NUMERIC,`email` TEXT,`crtype` TEXT,`address` TEXT,`dirurl` TEXT)')
                cursor.execute('INSERT INTO user (unm,pwd,name,email) VALUES(?,?,?,?)',(unm1,pwd1,em1,nm1))
                conn.commit()

   
   
             
            label_0 = Label(win, text="Add User",width=20,font=("bold", 20))
            label_0.place(x=90,y=53)


            label_1 = Label(win, text="Username",width=20,font=("bold", 10))
            label_1.place(x=80,y=130)

            entry_1 = Entry(win,textvar=unm)
            entry_1.place(x=240,y=130)

            label_1 = Label(win, text="Password",width=20,font=("bold", 10))
            label_1.place(x=80,y=180)

            mobe = Entry(win,textvar=pwd,show="*")
            mobe.place(x=240,y=180)

            label_2 = Label(win, text="Name",width=20,font=("bold", 10))
            label_2.place(x=80,y=230)

            entry_2 = Entry(win,textvar=name)
            entry_2.place(x=240,y=230)


            addr = Label(win, text="Email",width=20,font=("bold", 10))
            addr.place(x=68,y=280)

            addre = Entry(win,textvar=Email)
            addre.place(x=240,y=280)


            Button(win, text='Add User',width=20,bg='brown',fg='white',command=database).place(x=180,y=340)
            Button(win, text='Cancel',width=20,bg='red',fg='white',command=win.destroy).place(x=180,y=370)


        def AdmVwUsr():
            win=Toplevel()
            win.geometry('500x500')
            
            label_0 = Label(win, text="Registered Users",width=20,font=("bold", 20))
            label_0.place(x=100,y=53)

            Button(win, text='Exit',width=8,bg='black',fg='white',command=win.destroy).place(x=390,y=53)

            row=cursor.execute("SELECT `unm`,`name` FROM user")
            row=cursor.fetchall()
            
            px1=40
            px2=165
            px3=220
            py=130
            for i in row:

                unm = Label(win, text="Username: "+i[0],width=15,font=("normal", 9))
                unm.place(x=px1,y=py)
                nm = Label(win, text="Name: " +i[1],width=15,font=("normal", 9))
                nm.place(x=px2,y=py)
                
                py=py+40

            """scrollbar = Scrollbar(win)

            scrollbar.pack( side = RIGHT, fill = Y )

            mylist = Listbox(win, yscrollcommand = scrollbar.set )

            for i in row:
               mylist.insert(END, "Username : "+i[0]+"Name : "+i[1])

            mylist.pack( side = LEFT, fill = BOTH )
            scrollbar.config( command = mylist.yview )"""

        def AdmAdCr():
            win=Toplevel()
            win.geometry('500x700')

            name=StringVar()
            mobile=StringVar()
            Email=StringVar()
            addrs=StringVar()
            gvar = StringVar()
            s=StringVar()
            crtype=StringVar()

            #var1= IntVar()



            def database():
                
                row=cursor.execute("SELECT id FROM criminal")
                row=cursor.fetchall()
                global rid
                rid=len(row)
                rid=rid+1

                name1=name.get()
                mbl=mobile.get()
                addr=addrs.get()
                crt=crtype.get()
                email=Email.get()
                gender=gvar.get()
                state=s.get()
                #cursor.execute('CREATE TABLE IF NOT EXISTS criminal (`ID` INTEGER PRIMARY KEY AUTOINCREMENT,`name` TEXT,`mobile` NUMERIC,`email` TEXT,`crtype` TEXT,`address` TEXT,`dirurl` TEXT)')
                cursor.execute('INSERT INTO criminal (id,name,gender,email,mobile,address,remark,state) VALUES(?,?,?,?,?,?,?,?)',(rid,name1,gender,email,mbl,addr,crt,state))
                conn.commit()
                cp = Label(win, text="Succesfully Added! Close this Window..!!",fg='Green',width=40,font=("bold", 10))
                cp.place(x=100,y=100)
                

                for i in range(len(crfps)):
                    fp=str.replace(crfps[i],rdir,'')
                    cursor.execute('INSERT INTO crfploc (crid,fploc) VALUES(?,?)',(rid,fp))
                    conn.commit()

       
       
                 
            label_0 = Label(win, text="Add Criminals",width=20,font=("bold", 20))
            label_0.place(x=90,y=53)


            label_1 = Label(win, text="Name",width=20,font=("bold", 10))
            label_1.place(x=80,y=130)

            entry_1 = Entry(win,textvar=name)
            entry_1.place(x=240,y=130)

            mob = Label(win, text="Mobile",width=20,font=("bold", 10))
            mob.place(x=80,y=180)

            mobe = Entry(win,textvar=mobile)
            mobe.place(x=240,y=180)

            label_2 = Label(win, text="Email",width=20,font=("bold", 10))
            label_2.place(x=80,y=230)

            entry_2 = Entry(win,textvar=Email)
            entry_2.place(x=240,y=230)


            addr = Label(win, text="Address",width=20,font=("bold", 10))
            addr.place(x=68,y=280)

            addre = Entry(win,textvar=addrs)
            addre.place(x=240,y=280)

            label_3 = Label(win, text="Gender",width=20,font=("bold", 10))
            label_3.place(x=70,y=330)

            Radiobutton(win, text="Male",padx = 5, variable=gvar, value="m").place(x=235,y=330)
            Radiobutton(win, text="Female",padx = 20, variable=gvar, value="f").place(x=290,y=330)


            crty = Label(win, text="Remark",width=20,font=("bold", 10))
            crty.place(x=70,y=380)

            crt =Entry(win,textvar=crtype)
            crt.place(x=240,y=380)



            label_4 = Label(win, text="State",width=20,font=("bold", 10))
            label_4.place(x=70,y=430)

            list1 = ['Karnataka','Andhrapradesh','Tamilnadu','Kerala','Maharashtra','Delhi','Bihar','West Bengal'];

            droplist=OptionMenu(win,s, *list1)
            droplist.config(width=15)
            s.set('select your state') 
            droplist.place(x=240,y=430)

            def crpf():
                global crfps
                crfps = tkinter.filedialog.askopenfilenames(initialdir = "/media/dev/BetaMind/linx bak/devv/DHSInfo/Image Processing/pypro/fir4/database/",title = "Select file",filetypes = (("TIFF files","*.tif"),("all files","*.*")))
           

            Button(win, text='Add FP',width=20,bg='green',fg='white',command=crpf).place(x=180,y=480)

            """label_4 = Label(win, text="Programming",width=20,font=("bold", 10))
            label_4.place(x=85,y=330)
            var2= IntVar()
            Checkbutton(win, text="java", variable=var1).place(x=235,y=330)

            Checkbutton(win, text="python", variable=var2).place(x=290,y=330)
    """
            Button(win, text='Submit',width=20,bg='brown',fg='white',command=database).place(x=180,y=510)


            ############END OF ADD CRIMINAL###################

        def AdmVwCr():
            win=Toplevel()
            win.geometry('500x500')


 
            
            label_0 = Label(win, text="Registered Criminals",width=20,font=("bold", 20))
            label_0.place(x=100,y=53)

            Button(win, text='Exit',width=8,bg='black',fg='white',command=win.destroy).place(x=390,y=53)

            row=cursor.execute("SELECT `name`,`crtype` FROM criminal")
            row=cursor.fetchall()

            scrollbar = Scrollbar(win)

            scrollbar.pack( side = RIGHT, fill = Y )

            mylist = Listbox(win, yscrollcommand = scrollbar.set )

            for i in row:
               mylist.insert(END, "Name : "+i[0]+"Crime : "+i[1])

            mylist.pack( side = LEFT, fill = BOTH )
            scrollbar.config( command = mylist.yview )



        def AdmChPwd():
            win=Toplevel()
            win.geometry('500x500')

            crpwd=StringVar()
            nwpwd=StringVar()
            cnwpwd=StringVar()
            nwpwd1=StringVar()

            def updAdmPwd():
                crpwd1=crpwd.get()
                nwpwd1=nwpwd.get()
                print(nwpwd1)
                #cursor.execute('CREATE TABLE IF NOT EXISTS criminal (`ID` INTEGER PRIMARY KEY AUTOINCREMENT,`name` TEXT,`mobile` NUMERIC,`email` TEXT,`crtype` TEXT,`address` TEXT,`dirurl` TEXT)')
                cursor.execute('UPDATE admin set pwd=? where unm="admin"',(nwpwd1,))
                conn.commit()
                cp = Label(win, text="Succesfully Changed Password!",fg='Green',width=40,font=("bold", 10))
                cp.place(x=100,y=90)
                cp = Label(win, text="Please Close this Window.",fg='red',width=40,font=("bold", 10))
                cp.place(x=100,y=110)
                
                Button(win, text='Exit',width=24,bg='brown',fg='white',command=win.destroy).place(x=180,y=320)
                #time.wait(1)
                #win.destroy()

            
            def vrPwd():
                n=1
                cpwd=crpwd.get()
                row=cursor.execute("SELECT `pwd` FROM admin where id=1")
                row=cursor.fetchall()
                print(row[0][0])
                if(cpwd==row[0][0]):
                    icrpwd.config(state="disable")
                    Button(win, text='Verified',width=24,bg='green',fg='white',state="disable").place(x=123,y=180)
                    #vrbtn.config(text="Verified")
                    mob = Label(win, text="New Password",width=20,font=("bold", 10))
                    mob.place(x=80,y=250)

                    mobe = Entry(win,textvar=nwpwd)
                    mobe.place(x=240,y=250)

                    Button(win, text='Submit',width=24,bg='brown',fg='white',command=updAdmPwd).place(x=180,y=320)

                
            label_0 = Label(win, text="Change Password",width=20,font=("bold", 20))
            label_0.place(x=100,y=53)

            Button(win, text='Exit',width=8,bg='black',fg='white',command=win.destroy).place(x=390,y=53)
            """
            row=cursor.execute("SELECT `pwd` FROM admin where id=1")
            row=cursor.fetchall()
            print(row[0][0])
            """
            label_1 = Label(win, text="Current Password",width=20,font=("bold", 10))
            label_1.place(x=80,y=130)

            icrpwd = Entry(win,textvar=crpwd)
            icrpwd.place(x=240,y=130)

            vrbtn=Button(win, text='Verify',width=24,bg='brown',fg='white',command=vrPwd).place(x=123,y=180)


            


            

            # display message
            """message = "This is the child window"
            Label(win, text=message).pack()
            # quit child window and return to root window
            # the button is optional here, simply use the corner x of the child window
            Button(win, text='OK', command=win.destroy).pack()"""


        #Main Admin Section
        
        label_0 = Label(self, text="Hello, Admin!",width=20,font=("bold", 20))
        label_0.place(x=100,y=53)

        Button(self, text='Signout',width=8,bg='black',fg='white',command=lambda:controller.show_frame(RootPage)).place(x=390,y=53)

        ttk.Separator(self).place(x=0, y=120, relwidth=1)
        label_1 = Label(self, text="User Section",width=20,font=("default", 14))
        label_1.place(x=100,y=130)
        
        
        Button(self, text='Add User',width=24,bg='brown',fg='white',command=AdmAdUsr).place(x=123,y=160)

        """label_2 = Label(self, text="Or",width=14,font=("default", 9))
        label_2.place(x=175,y=195)"""

        Button(self, text='View Users',width=24,bg='brown',fg='white',command=AdmVwUsr).place(x=123,y=190)

        ttk.Separator(self).place(x=0, y=240, relwidth=1)

        #Criminal Section

        label_2 = Label(self, text="Criminal Section",width=20,font=("default",14))
        label_2.place(x=100,y=260)
        
        
        Button(self, text='Add Criminal',width=24,bg='brown',fg='white',command=AdmAdCr).place(x=123,y=290)
        Button(self, text='View Criminal',width=24,bg='brown',fg='white',command=AdmVwCr).place(x=123,y=320)

        ttk.Separator(self).place(x=0, y=360, relwidth=1)

        #User  Settings

        label_2 = Label(self, text="User Settings",width=20,font=("default",14))
        label_2.place(x=100,y=380)
        
        
        Button(self, text='Change Password',width=24,bg='brown',fg='white',command=AdmChPwd).place(x=123,y=410)
        ttk.Separator(self).place(x=0, y=490, relwidth=1)


    


###User Login

class UserLogin(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self,parent)
        #aunm=StringVar()
        #apwd=StringVar()
        unm=StringVar()
        pwd=StringVar()
        
        def UsrLogCheck():

            unm1=unm.get()
            pwd1=pwd.get()

            row=cursor.execute("SELECT `unm`,`pwd` FROM user WHERE unm=? and pwd=?",(unm1,pwd1))
            row=cursor.fetchall()
            le=len(row)
            if(le>0):
                #print ("Login Success!")
                cp = Label(self, text="Succesfully Logged in! Redirecting soon..!!",fg='Green',width=40,font=("bold", 10))
                cp.place(x=100,y=100)
                #time.sleep(2)

                """cp = Label(self, text="Succesfully Logged in! Redirecting soon..!!",fg='Green',width=40,font=("bold", 10))
                cp.place(x=100,y=100)
                
                """
                """ 
                qlst=row[0]
                qlst1=self.tk.splitlist(qlst)
                #usrnm=qlst1[0]
                qlst2=qlst.split(',')
                usrnm=qlst2[0]"""
                """
                for i in row:
                    print(i[0])"""
                #global usrnm
                usrnm=(row[0][0])
                logu=("Log : User - "+usrnm+" Logged in at "+str(currentDT)+"\n")
                print(logu)
                f=open("log.txt","a")
                f.write(logu)
                f=open("ses_usr.txt","w+")
                f.write(usrnm)
                f.close()
                controller.show_frame(UsrHmPg)
            else:
                wp = Label(self, text="Wrong Username or Password!",fg='red',width=40,font=("bold", 10))
                wp.place(x=100,y=100)
                #print("Wrong Cred")

            """cunm="a"
            cpwd="t"

            if(cunm==unm1 and cpwd==pwd1):
                status="Admin Login Success"
                print (status)
                time.sleep(0.5)
                status="Redirecting Now"
                print (status)
                time.sleep(0.5)
                status="Welcome Admin"
                print (status)
                #print("Login Success")
                #StatusBar1("Login Sucess.. Redirecting now")
                #self.variable.set("Login Success")            
            else:
                print("Wrong Cred")"""



        


        label_0 = Label(self, text="User Login",width=20,font=("bold", 20))
        label_0.place(x=100,y=53)

        label_1 = Label(self, text="Username :",width=20,font=("bold", 10))
        label_1.place(x=80,y=130)

        unm = Entry(self)
        unm.place(x=240,y=130)

        plbl= Label(self, text="Password :",width=20,font=("bold", 10))
        plbl.place(x=80,y=180)

        pwd = Entry(self,show="*")
        pwd.place(x=240,y=180)

        Button(self, text='Login',width=13,bg='green',fg='white',command=UsrLogCheck).place(x=123,y=230)
        Button(self, text='Cancel',width=13,bg='brown',fg='white',command=lambda:controller.show_frame(RootPage)).place(x=273,y=230)


###User Home Page

class UsrHmPg(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)


        def Process():
            import cv2
            import os
            import sys
            import numpy
            import matplotlib.pyplot as plt
            from enhance import image_enhance
            from skimage.morphology import skeletonize, thin
            os.chdir(rdir)

            def removedot(invertThin):
                temp0 = numpy.array(invertThin[:])
                temp0 = numpy.array(temp0)
                temp1 = temp0/255
                temp2 = numpy.array(temp1)
                temp3 = numpy.array(temp2)
                
                enhanced_img = numpy.array(temp0)
                filter0 = numpy.zeros((10,10))
                W,H = temp0.shape[:2]
                filtersize = 6
                
                for i in range(W - filtersize):
                    for j in range(H - filtersize):
                        filter0 = temp1[i:i + filtersize,j:j + filtersize]

                        flag = 0
                        if sum(filter0[:,0]) == 0:
                            flag +=1
                        if sum(filter0[:,filtersize - 1]) == 0:
                            flag +=1
                        if sum(filter0[0,:]) == 0:
                            flag +=1
                        if sum(filter0[filtersize - 1,:]) == 0:
                            flag +=1
                        if flag > 3:
                            temp2[i:i + filtersize, j:j + filtersize] = numpy.zeros((filtersize, filtersize))

                return temp2


            def get_descriptors(img):
                clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
                img = clahe.apply(img)
                img = image_enhance.image_enhance(img)
                img = numpy.array(img, dtype=numpy.uint8)
                # Threshold
                ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU);
                # Normalize to 0 and 1 range
                img[img == 255] = 1
                
                #Thinning
                skeleton = skeletonize(img)
                skeleton = numpy.array(skeleton, dtype=numpy.uint8)
                skeleton = removedot(skeleton)
                # Harris corners
                harris_corners = cv2.cornerHarris(img, 3, 3, 0.04)
                harris_normalized = cv2.normalize(harris_corners, 0, 255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32FC1)
                threshold_harris = 125;
                # Extract keypoints
                keypoints = []
                for x in range(0, harris_normalized.shape[0]):
                    for y in range(0, harris_normalized.shape[1]):
                        if harris_normalized[x][y] > threshold_harris:
                            keypoints.append(cv2.KeyPoint(y, x, 1))
                # Define descriptor
                orb = cv2.ORB_create()
                # Compute descriptors
                _, des = orb.compute(img, keypoints)
                return (keypoints, des);


            def main():
                #image_name = sys.argv[1]
                global img1
                global img2
                """
                with open('/media/dev/BetaMind/linx bak/devv/DHSInfo/Image Processing/pypro/pyfirec/fpknown/fp_names.txt', 'r') as myfile:
                    data=myfile.read().replace('\n', ',')
                #print data
                #print data[1]
                    tags=data.split(',')
                #print tags
                #c=len(tags)
                #print c"""
                fpd=cursor.execute("SELECT fploc FROM crfploc")
                fpd=cursor.fetchall()
                #fpdle=len(fpd)
                global cnt
                cnt=1
                wipro=Toplevel()
                wipro.geometry('500x700')

                label_0 = Label(wipro, text="Processing",width=20,font=("bold", 20))
                label_0.place(x=90,y=53)


                label_1 = Label(wipro, text="Total FP in DB : ",width=20,font=("bold", 10))
                label_1.place(x=80,y=130)



                mob = Label(wipro, text="Progress : ",width=20,font=("bold", 10))
                mob.place(x=80,y=180)



                """
                addr = Label(win, text="Address",width=20,font=("bold", 10))
                addr.place(x=68,y=280)

                addre = Label(win,text=""+str(gcrdet[0][3]))
                addre.place(x=240,y=280)

                label_3 = Label(win, text="Gender",width=20,font=("bold", 10))
                label_3.place(x=70,y=330)

                gen = Label(win,text=""+str(gcrdet[0][4]))
                gen.place(x=235,y=330)
                """

                try:
                    for i in range(len(fpd)):
                        
                        global mfpd
                        mfpd=(fpd[i][0])
                        #exit()
                        #print tags[i]
                        entry_1 = Label(wipro,text=""+str(len(fpd)))
                        entry_1.place(x=240,y=130)

                        mobe = Label(wipro,text=""+str(cnt))
                        mobe.place(x=240,y=180)

                        img1 = cv2.imread(fpd[i][0], cv2.IMREAD_GRAYSCALE)
                        kp1, des1 = get_descriptors(img1)
                        #image_name = sys.argv[2]
                        img2 = cv2.imread(fp2, cv2.IMREAD_GRAYSCALE)
                        kp2, des2 = get_descriptors(img2)
                    
                        # Matching between descriptors
                        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
                        matches = sorted(bf.match(des1, des2), key= lambda match:match.distance)
                        # Plot keypoints
                        img4 = cv2.drawKeypoints(img1, kp1, outImage=None)
                        img5 = cv2.drawKeypoints(img2, kp2, outImage=None)
                        #f, axarr = plt.subplots(1,2)
                        #axarr[0].imshow(img4)
                        #axarr[1].imshow(img5)
                        """
                        def pltkp():
                            # Plot keypoints
                            img4 = cv2.drawKeypoints(img1, kp1, outImage=None)
                            img5 = cv2.drawKeypoints(img2, kp2, outImage=None)
                            f, axarr = plt.subplots(1,2)
                            axarr[0].imshow(img4)
                            axarr[1].imshow(img5)
                            plt.show()
                        def pltmtch():
                            # Plot matches
                            
                            img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches, flags=2, outImg=None)
                            plt.imshow(img3)
                            plt.show()
                            """

                        # Plot matches

                        img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches, flags=2, outImg=None)
                        #plt.imshow(img3)
                        #plt.show()
                        
                        ###############################################################


                        # Calculate score
                        score = 0;
                        for match in matches:
                            score += match.distance

                        score_threshold = 10
                        cnt=cnt+1
                        if score/len(matches) < score_threshold:
                            print("Fingerprint matches.")
                            print ("Match found with following Fingerprint : ")
                            print('Score : {:.2f}'.format(score))
                            def showmatch():
                                win=Toplevel()
                                win.geometry('500x700')
                                win.title('Fingerprint Matched!')

                                getcrid=cursor.execute("SELECT crid from crfploc where fploc=?",(mfpd,))
                                getcrid=cursor.fetchall()
                                gcrid=getcrid[0][0]
                                #print(gcrid)
                                #exit()
                                gcrdet=cursor.execute("SELECT name,mobile,email,address,gender,remark,state from criminal where id=?",(gcrid,))
                                gcrdet=cursor.fetchall()
                                     
                                label_0 = Label(win, text="FP Matched Criminal",width=20,font=("bold", 20))
                                label_0.place(x=90,y=53)


                                label_1 = Label(win, text="Name",width=20,font=("bold", 10))
                                label_1.place(x=80,y=130)

                                entry_1 = Label(win,text=""+str(gcrdet[0][0]))
                                entry_1.place(x=240,y=130)

                                mob = Label(win, text="Mobile",width=20,font=("bold", 10))
                                mob.place(x=80,y=180)

                                mobe = Label(win,text=""+str(gcrdet[0][1]))
                                mobe.place(x=240,y=180)

                                label_2 = Label(win, text="Email",width=20,font=("bold", 10))
                                label_2.place(x=80,y=230)

                                entry_2 = Label(win,text=""+str(gcrdet[0][2]))
                                entry_2.place(x=240,y=230)


                                addr = Label(win, text="Address",width=20,font=("bold", 10))
                                addr.place(x=68,y=280)

                                addre = Label(win,text=""+str(gcrdet[0][3]))
                                addre.place(x=240,y=280)

                                label_3 = Label(win, text="Gender",width=20,font=("bold", 10))
                                label_3.place(x=70,y=330)

                                gen = Label(win,text=""+str(gcrdet[0][4]))
                                gen.place(x=235,y=330)


                                crty = Label(win, text="Remark",width=20,font=("bold", 10))
                                crty.place(x=70,y=380)

                                crt = Label(win,text=""+str(gcrdet[0][5]))
                                crt.place(x=240,y=380)



                                label_4 = Label(win, text="State",width=20,font=("bold", 10))
                                label_4.place(x=70,y=430)

                                state = Label(win,text=""+str(gcrdet[0][6]))
                                state.place(x=240,y=430)

                                def advinf():
                                    #f, axarr = plt.subplots(1,2)
                                    #axarr[0].imshow(img4)
                                    #axarr[1].imshow(img5)
                                    #plt.show()
                                    plt.imshow(img3)
                                    plt.show()

                                Button(win, text='Advanced Info',width=20,bg='green',fg='white',command=advinf).place(x=180,y=480)

                                """label_4 = Label(win, text="Programming",width=20,font=("bold", 10))
                                label_4.place(x=85,y=330)
                                var2= IntVar()
                                Checkbutton(win, text="java", variable=var1).place(x=235,y=330)

                                Checkbutton(win, text="python", variable=var2).place(x=290,y=330)
                        """
                                Button(win, text='Exit',width=20,bg='brown',fg='white',command=win.destroy).place(x=180,y=510)


                            showmatch()
                            raise StopIteration
                            """
                            win=Toplevel()
                            win.geometry('500x500')
                            win.title('Fingerprint Matched!')"""
                            break
                            #print (img1)
                        else:

                            print("Fingerprint does not match.")
                            print('Score : {:.2f}'.format(score))
                            #print("Score : "+score)
                    print("Verification completed")
                    raise StopIteration

                except StopIteration:
                    pass
                #execfile()
            main()

                
    
        def UsrInpFp():
            #print("Hello")
            global fp2
            fp2 = tkinter.filedialog.askopenfilename(initialdir = "database/",title = "Select file",filetypes = (("TIFF files","*.tif"),("all files","*.*")))
            Process()
        #Main Admin Section
        if (usrnm=="None"):
            label_0 = Label(self, text="Hello, Unknown!",width=20,font=("bold", 20))
            label_0.place(x=100,y=53)
        else:
            label_0 = Label(self, text="Hello, !"+usrnm,width=20,font=("bold", 20))
            label_0.place(x=100,y=53)

        Button(self, text='Signout',width=8,bg='black',fg='white',command=lambda:controller.show_frame(RootPage)).place(x=390,y=53)

        ttk.Separator(self).place(x=0, y=120, relwidth=1)
        label_1 = Label(self, text="FP Match",width=20,font=("default", 14))
        label_1.place(x=100,y=130)
        
        
        Button(self, text='Input FP',width=24,bg='brown',fg='white',command=UsrInpFp).place(x=123,y=160)

        """label_2 = Label(self, text="Or",width=14,font=("default", 9))
        label_2.place(x=175,y=195)"""

        
        ttk.Separator(self).place(x=0, y=240, relwidth=1)

        #Criminal Section

        label_2 = Label(self, text="Profile Settings",width=20,font=("default",14))
        label_2.place(x=100,y=260)
        
        
        Button(self, text='Change Password',width=24,bg='brown',fg='white',command=lambda:AdmAdCr).place(x=123,y=290)
        
        ttk.Separator(self).place(x=0, y=360, relwidth=1)

        #User  Settings
"""
        label_2 = Label(self, text="User Settings",width=20,font=("default",14))
        label_2.place(x=100,y=380)
        
        
        Button(self, text='Change Password',width=24,bg='brown',fg='white',command=lambda:controller.show_frame(AdminLogin)).place(x=123,y=410)
        ttk.Separator(self).place(x=0, y=490, relwidth=1)
"""

    

###Criminal Registration

class CrRegister(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        """button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
        """




        name=StringVar()
        mobile=StringVar()
        Email=StringVar()
        addrs=StringVar()
        gvar = StringVar()
        s=StringVar()
        crtype=StringVar()
        #var1= IntVar()



        def database():
            name1=name.get()
            mbl=mobile.get()
            addr=addrs.get()
            crt=crtype.get()
            email=Email.get()
            gender=gvar.get()
            state=s.get()
            #prog=var1.get()
            conn = sqlite3.connect('test.db')
            with conn:
                cursor=conn.cursor()
            #cursor.execute('CREATE TABLE IF NOT EXISTS criminal (`ID` INTEGER PRIMARY KEY AUTOINCREMENT,`name` TEXT,`mobile` NUMERIC,`email` TEXT,`crtype` TEXT,`address` TEXT,`dirurl` TEXT)')
            cursor.execute('INSERT INTO criminal (name,gender,email,mobile,address,crtype,state) VALUES(?,?,?,?,?,?,?)',(name1,gender,email,mbl,addr,crt,state))
            conn.commit()

   
   
             
        label_0 = Label(self, text="Registration form",width=20,font=("bold", 20))
        label_0.place(x=90,y=53)


        label_1 = Label(self, text="Name",width=20,font=("bold", 10))
        label_1.place(x=80,y=130)

        entry_1 = Entry(self,textvar=name)
        entry_1.place(x=240,y=130)

        mob = Label(self, text="Mobile",width=20,font=("bold", 10))
        mob.place(x=80,y=180)

        mobe = Entry(self,textvar=mobile)
        mobe.place(x=240,y=180)

        label_2 = Label(self, text="Email",width=20,font=("bold", 10))
        label_2.place(x=80,y=230)

        entry_2 = Entry(self,textvar=Email)
        entry_2.place(x=240,y=230)


        addr = Label(self, text="Address",width=20,font=("bold", 10))
        addr.place(x=68,y=280)

        addre = Entry(self,textvar=addrs)
        addre.place(x=240,y=280)

        label_3 = Label(self, text="Gender",width=20,font=("bold", 10))
        label_3.place(x=70,y=330)

        Radiobutton(self, text="Male",padx = 5, variable=gvar, value="m").place(x=235,y=330)
        Radiobutton(self, text="Female",padx = 20, variable=gvar, value="f").place(x=290,y=330)


        crty = Label(self, text="Crime Type",width=20,font=("bold", 10))
        crty.place(x=70,y=380)

        crt = ['Arson','Blackmail','Bruglary','Embezzlement','Extortion','Fraud'];

        droplist=OptionMenu(self,crtype, *crt)
        droplist.config(width=15)
        crtype.set('select Crime Type') 
        droplist.place(x=240,y=380)



        label_4 = Label(self, text="State",width=20,font=("bold", 10))
        label_4.place(x=70,y=430)

        list1 = ['Karnataka','Andhrapradesh','Tamilnadu','Kerala','Maharashtra','Delhi'];

        droplist=OptionMenu(self,s, *list1)
        droplist.config(width=15)
        s.set('select your state') 
        droplist.place(x=240,y=430)

        """label_4 = Label(self, text="Programming",width=20,font=("bold", 10))
        label_4.place(x=85,y=330)
        var2= IntVar()
        Checkbutton(self, text="java", variable=var1).place(x=235,y=330)

        Checkbutton(self, text="python", variable=var2).place(x=290,y=330)
"""
        Button(self, text='Submit',width=20,bg='brown',fg='white',command=database).place(x=180,y=480)
        Button(self, text='Back to Home',width=20,bg='red',fg='white',command=lambda: controller.show_frame(StartPage)).place(x=180,y=510)

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()
        


app = SeaofBTCapp()
app.mainloop()