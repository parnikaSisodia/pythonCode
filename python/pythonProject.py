from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as MessageBox
import mysql.connector as mys
from PIL import Image, ImageTk

'''mycon=mys.connect(host="localhost",user='root',passwd='paru',database='prac')
mycur=mycon.cursor()

q2="create table payments(registrationNo varchar(20),\
    month varchar(20),\
    rupee int(11),\
    mode_of_payment varchar(20))"
mycur.execute(q2)
mycon.close()



mycon=mys.connect(host="localhost",user='root',passwd='paru',database='prac')
mycur=mycon.cursor()
q1="create table form (registrationNo int(11),\
    FisrstName varchar(20),\
    MiddleName varchar(20),\
    LastName varchar(20),\
    MobileNo bigint(20),\
    Email_id varchar(100),\
    DOB date,\
    Class varchar(4))"
mycur.execute(q1)
mycon.close()'''


def insert1():
    regno1=inp_regno1.get()
    name1=name1E.get()
    name2=name2E.get()
    name3=name3E.get()
    mobile=mobileE.get()
    mail=mailE.get()
    dob=dobE.get()
    class_=classE.get()

    #linking with mysql
    mycon=mys.connect(host="localhost",user="root",passwd="paru",database="prac")
    mycur=mycon.cursor()

    #str,str,str,str,int,str,str,int assingned according to datatypes assigned in mysql
    s1="insert into form values({},'{}','{}','{}',{},'{}','{}','{}')".format(regno1\
        ,name1,name2,name3,mobile,mail,dob,class_)
    mycur.execute(s1)              
    mycon.commit()
    MessageBox.showinfo("REGISTRATION STATUS","Added successfully !!")
    mycon.close()

# view records for frame 2 'SEE ALL RECORDS'    
def viewing_records():    
    mycon=mys.connect(host="localhost",user="root",passwd="paru",database="prac")
    mycur=mycon.cursor()
    s1="select * from form order by registrationNo"
    mycur.execute(s1)

    #making list of records in table "form"
    i=0
    l=[]
    for reg in mycur:
        l.append(reg)



    #creating table    
    class Table:
        def __init__(self,root):
            for i in range(total_rows):    
                for j in range(total_columns):
                    if j==0:
                        if i==0:        #to make black heading(top most,i.e.i=0) of every column (j)
                            self.e = Entry(root, width=8, fg='black',font=('Arial',12,'bold'))
                        else:           #to make blue coloured contents
                            self.e = Entry(root, width=8, fg='blue',font=('Arial',12,'bold'))
                    elif j==1:
                        if i==0:
                            self.e = Entry(root, width=14, fg='black',font=('Arial',12,'bold'))
                        else:
                            self.e = Entry(root, width=14, fg='blue',font=('Arial',12,'bold'))
                    elif j==2:
                        if i==0:
                            self.e = Entry(root, width=14, fg='black',font=('Arial',12,'bold'))
                        else:
                            self.e = Entry(root, width=14, fg='blue',font=('Arial',12,'bold'))
                    elif j==3:
                        if i==0:
                            self.e = Entry(root, width=14, fg='black',font=('Arial',12,'bold'))
                        else:
                            self.e = Entry(root, width=14, fg='blue',font=('Arial',12,'bold'))
                    elif j==4:
                        if i==0:
                            self.e = Entry(root, width=12, fg='black',font=('Arial',12,'bold'))
                        else:
                            self.e = Entry(root, width=12, fg='blue',font=('Arial',12,'bold'))
                    elif j==5:
                        if i==0:
                            self.e = Entry(root, width=25, fg='black',font=('Arial',12,'bold'))
                        else:
                            self.e = Entry(root, width=25, fg='blue',font=('Arial',12,'bold'))
                    elif j==6:
                        if i==0:
                            self.e = Entry(root, width=12, fg='black',font=('Arial',12,'bold'))
                        else:
                            self.e = Entry(root, width=12, fg='blue',font=('Arial',12,'bold'))
                    else:
                        if i==0:
                            self.e = Entry(root, width=10, fg='black',font=('Arial',12,'bold'))
                        else:
                            self.e = Entry(root, width=10, fg='blue',font=('Arial',12,'bold'))
                    
                        
                    #inserting the list
                    self.e.grid(row=i, column=j)
                    self.e.insert(END, lst2[i][j])
                    
    #defining new varible (lst) else error l defined before the funtion (class Table)    
    lst=l

    # creating i=0(row1) with headings
    lst2=[('REG.NO.','FIRST NAME','MIDDLE NAME','LAST NAME','MOB.NO.','EMAIL-ID','DOB','CLASS')]+lst #contatenation

    # find total number of rows and 
    total_rows = len(lst2)

    #find total columns
    total_columns = len(lst2[0]) 
           
        # create root window 
    root = Tk() 
    t = Table(root)
    root.title("SEE ALL RECORDS")
    root.mainloop()
                
            

def see_individual():
    
    sub_hd1=Label(my_frame2,text="Enter the Registration number",bg='light blue',font=("bold",20))
    sub_hd1.place(x=550,y=456)
    
    def see_rec():
        mycon=mys.connect(host="localhost",user="root",passwd="paru",database="prac")
        mycur=mycon.cursor()

        #extracting value from Combobox
        prt=drop1.get()

        #creating a tuple
        inp=(prt,)

        #table join
        s2="select f.registrationNo,FisrstName,month,rupee,mobileNo,\
            mode_of_payment from form f,payments p where \
            f.registrationNo=p.registrationNo and f.registrationNo=%s"
        mycur.execute(s2,inp)
        result=mycur.fetchall()
        l=[]
        for x in result:
            print(x)
            l.append(x)
        class Table:
            def __init__(self,root):
                for i in range(total_rows): 
                    for j in range(total_columns):
                        if j==0:
                            if i==0:
                                self.e = Entry(root, width=8, fg='black',font=('Arial',12,'bold'))
                            else:
                                self.e = Entry(root, width=8, fg='blue',font=('Arial',12,'bold'))
                        elif j==1:
                            if i==0:
                                self.e = Entry(root, width=12, fg='black',font=('Arial',12,'bold'))
                            else:
                                self.e = Entry(root, width=12, fg='blue',font=('Arial',12,'bold'))
                        elif j==2:
                            if i==0:
                                self.e = Entry(root, width=10, fg='black',font=('Arial',12,'bold'))
                            else:
                                self.e = Entry(root, width=10, fg='blue',font=('Arial',12,'bold'))
                        elif j==3:
                            if i==0:
                                self.e = Entry(root, width=10, fg='black',font=('Arial',12,'bold'))
                            else:
                                self.e = Entry(root, width=10, fg='blue',font=('Arial',12,'bold'))
                        elif j==4:
                            if i==0:
                                self.e = Entry(root, width=10, fg='black',font=('Arial',12,'bold'))
                            else:
                                self.e = Entry(root, width=10, fg='blue',font=('Arial',12,'bold'))
                        else:
                            if i==0:
                                self.e = Entry(root, width=20, fg='black',font=('Arial',12,'bold'))
                            else:
                                self.e = Entry(root, width=20, fg='blue',font=('Arial',12,'bold'))
                        self.e.grid(row=i, column=j)
                        self.e.insert(END, lst2[i][j])
   
        # find total number of rows and 
        # columns in list
        lst=l
        lst2=[('REG NO.','FIRST NAME','MONTH','RUPEE','MOB NO.','MODE')]+lst
        total_rows = len(lst2) 
        total_columns = len(lst2[0])
        if total_rows<2:
            MessageBox.showinfo("WARNING","No Record Found !")
        else:
            # create root window 
            root = Tk() 
            t = Table(root)
            root.title("SEE PARTICULAR RECORD")
            root.mainloop()
        
                
    my_button=Button(my_frame2,text="VIEW",command=see_rec,bg="black",\
                     font=20,fg="white",padx=1,pady=1)
    my_button.place(x=1100,y=456)
    
    mycon=mys.connect(host="localhost",user="root",passwd="paru",database="prac")
    mycur=mycon.cursor()
    s1="select distinct(registrationNo) from payments "
    mycur.execute(s1)
    result=mycur.fetchall()
    mycon.close()
    l=[]
    for x in result:
        print(x)
        l.append(x)
    print(l)    
    drop1=ttk.Combobox(my_frame2,values=l,font=('bold',20),width=6)
    drop1.current(0)
    drop1.place(x=950,y=456)



def reg():
    my_nb.select(1)

def make_pay():
    my_nb.select(3)

def view_det():
    my_nb.select(2)

    
#inserting data in Frame3            
#next button
def insert3():
    
    registrationNo=inp_regno.get()
    month=drop_month.get()
    rupee=inp_rupee.get()
    mode_of_payment=drop_mop.get()
    mycon=mys.connect(host="localhost",user="root",passwd="paru",database="prac")
    mycur=mycon.cursor()
    s2="insert into payments values({},'{}',{},'{}')".format(registrationNo,month,rupee,mode_of_payment)
    if registrationNo=='':
        MessageBox.showinfo("Payment","Enter the registration number please !!")
        mycon.close()

                
    elif rupee=='':
        MessageBox.showinfo("Payment","Enter the amount !!")
        mycon.close()

            
    else:
        mycur.execute(s2)
        mycon.commit()
        print(rupee)
            
        MessageBox.showinfo("Payment","Payment Done!!")
        mycon.close()
            
    
        
def update():
    
    def updt():
        regno=regno2.get()
        name1=name1E.get()
        name2=name2E.get()
        name3=name3E.get()
        mobile=mobileE.get()
        mail=mailE.get()
        dob=dobE.get()
        class_=classE.get()
        
        mycon=mys.connect(host="localhost",user="root",passwd="paru",database="prac")
        mycur=mycon.cursor()
        s2='update form set FisrstName=%s,MiddleName=%s,LastName=%s,MobileNo=%s,Email_id=%s,DOB=%s,Class=%s \
            where registrationNo=%s'
        inputs=(name1,name2,name3,mobile,mail,dob,class_,regno)
        
        
        mycur.execute(s2,inputs)
        mycon.commit()
        

        MessageBox.showinfo("Update","Record is updated!!")
        mycon.close()

        
    def nxt():
        regno=regno2.get()
        name1=name1E.get()
        name2=name2E.get()
        name3=name3E.get()
        mobile=mobileE.get()
        mail=mailE.get()
        dob=dobE.get()
        class_=classE.get()
        mycon=mys.connect(host="localhost",user="root",passwd="paru",database="prac")
        mycur=mycon.cursor()
        s1="select registrationNo from form "
        mycur.execute(s1)
        result=mycur.fetchall()
        l=[]
        for x in result:
            print(x)
            l.append(x)
        print(l)

        inp=(regno,)
        s2="select * from form where registrationNo=%s"
        mycur.execute(s2,inp)
        result=mycur.fetchall()
        mycon.commit()                    
        for record in result:
            print(record)
            regno1.set("")
            name1E.delete(0,'end')
            name2E.delete(0,'end')
            name3E.delete(0,'end')
            mobileE.delete(0,'end')
            mailE.delete(0,'end')
            dobE.delete(0,'end')
            classE.set("")
            regno1.insert(0,record[0])
            name1E.insert(0,record[1])
            name2E.insert(0,record[2])
            name3E.insert(0,record[3])
            mobileE.insert(0,record[4])
            mailE.insert(0,record[5])
            dobE.insert(0,record[6])
            classE.insert(0,record[7])
                    
        mycon.close()
    def clear():
        regno1.set("")
        name1E.delete(0,'end')
        name2E.delete(0,'end')
        name3E.delete(0,'end')
        mobileE.delete(0,'end')
        mailE.delete(0,'end')
        dobE.delete(0,'end')
        classE.set("")
        
    root=Tk()
    root.title("UPDATE")
    w=form1.winfo_screenwidth()
    h=form1.winfo_screenheight()
    root.geometry('%dx%d+0+0' % (w,h))

    heading=Label(root,text='UPDATING RECORDS FORM',font=("bold",50))
    heading.place(x=250,y=10)

    hd2=Label(root,text="SELECT REGISTRATION NUMBER",font=('bold',15))
    hd2.place(x=50,y=150)
    #linking with mysql
    mycon=mys.connect(host="localhost",user="root",passwd="paru",database="prac")
    mycur=mycon.cursor()
    s1="select registrationNo from form "
    mycur.execute(s1)
    result=mycur.fetchall()
    mycon.close()
    l=[]
    for x in result:
        l.append(x)    
    regno2=ttk.Combobox(root,values=l,font=('bold',20),width=6)
    regno2.place(x=450,y=150)
        
    reg=Label(root,text="Registration Number",font=("bold",15))
    reg.place(x=50,y=300)
    regno1=ttk.Combobox(root,values=l,font=('bold',20),width=6)
    regno1.place(x=250,y=300)

    class_=Label(root,text="Class",font=("bold",15))
    class_.place(x=500,y=300)
    classE=ttk.Combobox(root,values=['I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII'],font=('bold',15))
    classE.place(x=600,y=300,width=75,height=30)


    name1=Label(root,text="First name",font=("bold",15))
    name1.place(x=50,y=350)
    name1E= Entry(root,font=('bold',15))
    name1E.place(x=250,y=350,width=150,height=30)

    name2=Label(root,text="Middle Name",font=("bold",15))
    name2.place(x=500,y=350)
    name2E= Entry(root,font=('bold',15))
    name2E.place(x=650,y=350,width=150,height=30)

    name3=Label(root,text="Last Name",font=("bold",15))
    name3.place(x=900,y=350)
    name3E= Entry(root,font=('bold',15))
    name3E.place(x=1050,y=350,width=150,height=30)


    mobile=Label(root,text="Mobile no.",font=("bold",15))
    mobile.place(x=50,y=400)
    mobileE= Entry(root,font=('bold',15))
    mobileE.place(x=250,y=400,width=150,height=30)

    mail=Label(root,text="Email id",font=("bold",15))
    mail.place(x=500,y=400)
    mailE= Entry(root,font=('bold',15))
    mailE.place(x=650,y=400,width=300,height=30)


    dob=Label(root,text="Date of Birth",font=("bold",15))# add calendar
    dob.place(x=50,y=450)
    dob_=Label(root,text="(Enter date in this format(yy-mm-dd))",font=('bold',10))
    dob_.place(x=450,y=450)
    dobE= Entry(root,font=('bold',15))
    dobE.place(x=250,y=450,width=150,height=30)

    button13=Button(root,text="Save Record",bg="black",font=("bold",20)\
                    ,fg="white",padx=1,pady=1,command=updt)
    button13.place(x=450,y=500)


            
    
    
    myButton=Button(root,text="NEXT",bg="black",font=("bold",15)\
                    ,fg="white",padx=1,pady=1,command=nxt)
    myButton.place(x=750,y=150)

    
    myButton2=Button(root,text="CLEAR",bg="black",font=("bold",15)\
                    ,fg="white",padx=1,pady=1,command=clear)
    myButton2.place(x=950,y=150)
    


def delete():

    def dele():
        regno=regno3.get()
        input=(regno,)
        s2="delete from form where registrationNo=%s"
        mycur.execute(s2,input)
        mycon.commit()
        MessageBox.showinfo("DELETE","Record is deleted!!")
        mycon.close()
    
    root=Tk()
    root.title("DELETE")
    root.geometry('800x400')

    hd1=Label(root,text="DELETE RECORD",font=("bold",30))
    hd1.place(x=250,y=10)

    hd2=Label(root,text="Select registration number to be deleted",font=('bold',15))
    hd2.place(x=50,y=100)

    mycon=mys.connect(host="localhost",user="root",passwd="paru",database="prac")
    mycur=mycon.cursor()
    s1="select registrationNo from form "
    mycur.execute(s1)
    result=mycur.fetchall()
    l=[]
    for x in result:
        l.append(x)    
    regno3=ttk.Combobox(root,values=l,font=('bold',20),width=6)
    regno3.place(x=450,y=100)
    
    
    myButton=Button(root,text="Delete",bg="black",font=("bold",15)\
                    ,fg="white",padx=1,pady=1,command=dele)
    myButton.place(x=300,y=200)
    

        
#navigating a tab
def back():
    my_nb.select(0)

   
#NOTEBOOK
form1=Tk() #to open new window
form1.title("DOON INTERNATIONAL SCHOOL,MOHALI")
#form1.geometry("1000x1000")
#w=1366
#h=768
w=form1.winfo_screenwidth()
h=form1.winfo_screenheight()
form1.geometry('%dx%d+0+0' % (w,h)) #to open the form to full screen window
my_nb=ttk.Notebook(form1)   #to make tabs
my_nb.pack(pady=15)

my_frame1=Frame(my_nb,width=1300,height=1000,bg="light blue")  #to create frame
my_frame2=Frame(my_nb,width=1300,height=1000,bg="light blue")
my_frame3=Frame(my_nb,width=1300,height=1000,bg="light blue")
my_frame4=Frame(my_nb,width=1300,height=1000,bg="light blue")



my_nb.add(my_frame4,text="Home")
my_nb.add(my_frame1,text="Registration") #tabs heading
my_nb.add(my_frame2,text="View Details")
my_nb.add(my_frame3,text="Make Payment")







#FRAME 4

heading1=Label(my_frame4,text= "DOON INTERNATIONAL SCHOOL",bg="light blue",fg="black",font=("old english school",50,\
                                                                                            "bold"))
heading1.place(x=150,y=230)

hd2=Label(my_frame4,text="Welcomes you to our Online World",bg='light blue',fg="black",font=('bold',40))
hd2.place(x=250,y=300)


        # adding school's image
image =Image.open('D:\python12\PROJECT\doon_sch1.jpg')
image2=image.resize((w-135,182),Image.ANTIALIAS)   #to set image's size in horizontal form leaving '135' space for logo
image1 = ImageTk.PhotoImage(image2)


l1=Label(my_frame4,image=image1)
l1.image=image1
l1.place(x=135,y=0)  # x=135 because 135 space has to be occupied by the logo


        # adding school's logo
load=Image.open('D:\python12\PROJECT\logo4.jpg')
render=ImageTk.PhotoImage(load)         # used library PIL
img= Label(my_frame4,image=render)
img.image =render
img.place(x=0,y=0)








#FRAME 1

        # adding school's image
image =Image.open("D:\python12\PROJECT\doon_sch1.jpg")
image2=image.resize((w-135,182),Image.ANTIALIAS)   #to set image's size in horizontal form leaving '135' space for logo
image1 = ImageTk.PhotoImage(image2)


l1=Label(my_frame1,image=image1)
l1.image=image1
l1.place(x=135,y=0)  # x=135 because 135 space has to be occupied by the logo


        # adding school's logo
load=Image.open('D:\python12\PROJECT\logo4.jpg')
render=ImageTk.PhotoImage(load)         # used library PIL
img= Label(my_frame1,image=render)
img.image =render
img.place(x=0,y=0)






heading2=Label(my_frame1,text="Enrollment form",bg="light blue",fg="black",font=("bold",50))
heading2.place(x=450,y=187)

regno1=Label(my_frame1,text="Registration Number",font=("bold",15))
regno1.place(x=50,y=300)
inp_regno1=Entry(my_frame1,font=("bold",15))
inp_regno1.place(x=250,y=300,width=150,height=30)

class_=Label(my_frame1,text="Class",font=("bold",15))
class_.place(x=500,y=300)
classE=ttk.Combobox(my_frame1,values=['I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII'],font=('bold',15))
classE.current(11)
classE.place(x=600,y=300,width=75,height=30)


name1=Label(my_frame1,text="First name",font=("bold",15))
name1.place(x=50,y=350)
name1E= Entry(my_frame1,font=('bold',15))
name1E.place(x=250,y=350,width=150,height=30)


name2=Label(my_frame1,text="Middle Name",font=("bold",15))
name2.place(x=500,y=350)
name2E= Entry(my_frame1,font=('bold',15))
name2E.place(x=650,y=350,width=150,height=30)

name3=Label(my_frame1,text="Last Name",font=("bold",15))
name3.place(x=900,y=350)
name3E= Entry(my_frame1,font=('bold',15))
name3E.place(x=1050,y=350,width=150,height=30)


mobile=Label(my_frame1,text="Mobile no.",font=("bold",15))
mobile.place(x=50,y=400)
mobileE= Entry(my_frame1,font=('bold',15))
mobileE.place(x=250,y=400,width=150,height=30)


mail=Label(my_frame1,text="Email id",font=("bold",15))
mail.place(x=500,y=400)
mailE= Entry(my_frame1,font=('bold',15))
mailE.place(x=650,y=400,width=300,height=30)


dob=Label(my_frame1,text="Date of Birth",font=("bold",15))# add calendar
dob.place(x=50,y=450)
dob_=Label(my_frame1,text="(Enter date in this format(yy-mm-dd))",bg="light blue",font=('bold',10))
dob_.place(x=400,y=450)
dobE= Entry(my_frame1,font=('bold',15))
dobE.place(x=250,y=450,width=150,height=30)




# frame 2

        # adding school's image
image =Image.open('D:\python12\PROJECT\doon_sch1.jpg')
image2=image.resize((w-135,182),Image.ANTIALIAS)   #to set image's size in horizontal form leaving '135' space for logo
image1 = ImageTk.PhotoImage(image2)


l1=Label(my_frame2,image=image1)
l1.image=image1
l1.place(x=135,y=0)  # x=135 because 135 space has to be occupied by the logo


        # adding school's logo
load=Image.open('D:\python12\PROJECT\logo4.jpg')
render=ImageTk.PhotoImage(load)         # used library PIL
img= Label(my_frame2,image=render)
img.image =render
img.place(x=0,y=0)



hd2=Label(my_frame2,text="FEE Receipt Record",bg='light blue',fg="black",font=('bold',50))
hd2.place(x=350,y=187)






# frame 3


        # adding school's image
image =Image.open('D:\python12\PROJECT\doon_sch1.jpg')
image2=image.resize((w-135,182),Image.ANTIALIAS)   #to set image's size in horizontal form leaving '135' space for logo
image1 = ImageTk.PhotoImage(image2)


l1=Label(my_frame3,image=image1)
l1.image=image1
l1.place(x=135,y=0)  # x=135 because 135 space has to be occupied by the logo


        # adding school's logo
load=Image.open('D:\python12\PROJECT\logo4.jpg')
render=ImageTk.PhotoImage(load)         # used library PIL
img= Label(my_frame3,image=render)
img.image =render
img.place(x=0,y=0)
hd2=Label(my_frame3,text="DO PAYMENT",bg='light blue',fg="black",font=('bold',50))
hd2.place(x=450,y=187)

regno=Label(my_frame3,text="Enter the Registration number",font=("bold",15))
regno.place(x=50,y=300)
inp_regno=Entry(my_frame3,font=("bold",15),width=15)
inp_regno.place(x=400,y=300)

month=Label(my_frame3,text='Month',font=("bold",15))
month.place(x=50,y=350)
#drop_down list like Combobox
drop_month=ttk.Combobox(my_frame3,values=["Jan","Feb","Mar","Apr","May","June","July","Aug",'Sept','Oct','Nov','Dec'],\
                        font=("bold",15),width=13) #values in the form of list
drop_month.current(0) #by default display on the dropdown menu
drop_month.place(x=400,y=350)


rupee=Label(my_frame3,text="Amount",font=("bold",15))
rupee.place(x=50,y=400)
inp_rupee=Entry(my_frame3,font=("bold",15),width=15)
inp_rupee.place(x=400,y=400)

mode_of_pay=Label(my_frame3,text="Mode of Payment",font=("bold",15))
mode_of_pay.place(x=50,y=450)
drop_mop=ttk.Combobox(my_frame3,values=['Online','Cash'],font=("bold",15),width=13)
drop_mop.current(0)
drop_mop.place(x=400,y=450)



#buttons

button1=Button(my_frame1,text="Add",bg="black",font=("bold",20),fg="white",command=insert1,padx=10,pady=1)
button1.place(x=500,y=550)

button4=Button(my_frame1,text="Home",bg="black",font=("bold",20),fg="white",padx=10,pady=1,command=back)
button4.place(x=650,y=550)

button2=Button(my_frame2,text="See ALL records",bg="black",font=("bold",20),fg="white",padx=1,pady=1,\
               command=viewing_records)
button2.place(x=200,y=350)

button12=Button(my_frame2,text="Update record",bg="black",font=("bold",20),fg="white",padx=1,pady=1,command=update)
button12.place(x=550,y=350)

button13=Button(my_frame2,text="Delete record",bg="black",font=("bold",20),fg="white",padx=1,pady=1,command=delete)
button13.place(x=900,y=350)

button5=Button(my_frame2,text="See particular records",bg="black",font=("bold",20),fg="white",padx=1,pady=1,\
               command=see_individual)
button5.place(x=200,y=450)


button10=Button(my_frame2,text="Home",bg="black",font=("bold",20),fg="white",padx=10,pady=1,command=back)
button10.place(x=200,y=550)

button11=Button(my_frame3,text="Home",bg="black",font=("bold",20),fg="white",padx=1,pady=1,command=back)
button11.place(x=750,y=550)


button6=Button(my_frame4,text="Registration",bg="black",font=("bold",20),fg="white",padx=25,pady=10,command=reg)
button6.place(x=150,y=400)

button8=Button(my_frame4,text="View Details",bg="black",font=("bold",20),fg="white",padx=25,pady=10,command=view_det)
button8.place(x=550,y=400)

button9=Button(my_frame4,text="Make Payment",bg="black",font=("bold",20),fg="white",padx=25,pady=10,command=make_pay)
button9.place(x=950,y=400)

button7=Button(my_frame3,text="Make Payment",bg="black",font=("bold",20),fg="white",padx=1,pady=1,command=insert3)
button7.place(x=450,y=550)


