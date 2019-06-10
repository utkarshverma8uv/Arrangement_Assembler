import mysql.connector as mysql
from tkinter import *
k=open('C:\\Users\\Aman\\Desktop\\tkinter\\Absentees.dat','r')
pas=input('enter your mysql password-')
mycon= mysql.connect(host='localhost',user='root',password= pas ,database='school')
cursor=mycon.cursor()

pd_lst=['1st','2nd','3rd','4th','5th','6th','7th','8th']
dt= k.readline()[0:3]

t_lst=[]
cursor.execute('show tables')
data=list(cursor.fetchall())
for t in data:
    t_lst+=[t[0]]

abt=[]
for l in range(10):
    line=k.readline()
    if len(line)==4:
        abt+=[(line[0:3])]
ch_lst=t_lst
for a in abt:
    ch_lst.remove(a)
print(ch_lst)
        
arw=Tk()
arw.title('Arranger')
arw.configure(background="black")
#arw.resizable(False,False)

head=Label(arw,text ='ARRANGER',bg='black', font= ('Gabriola',40), fg='lime')
head.grid(row=0,column=4)



for i in range(len(abt)):
    cursor.execute("select 1st,2nd,3rd,4th,5th,6th,7th,8th from {} where day='{}'".format(abt[i],dt))
    d=cursor.fetchone()
    
    mainframe=Frame(arw,bg='black',relief='raised',bd=5)
    mainframe.grid(row=i*8+1,column=4)
    tcname=Label(mainframe,text =abt[i],bg='black',height=1, font= ('Gabriola',30), fg='lime')
    tcname.grid(row=i*8+1,column=1)
    
    period=Frame(mainframe,bg='black',relief='groove',bd=5)
    period.grid(row=i*8+2,column=0)
    label=Label(period,text ='PERIODS',bg='black', font= ('Gabriola',20), fg='lime',relief='raised',bd=3)
    label.grid(row=i*8+2,column=0)
    for p in range(8):
        prd=Label(period,text =pd_lst[p],width=7,bg='black', font= ('Gabriola',20), fg='lime',relief='raised',bd=5)
        prd.grid(row=p*8+3,column=0)

    clas=Frame(mainframe,bg='black',relief='groove',bd=5)
    clas.grid(row=i*8+2,column=1)
    label=Label(clas,text ='CLASS',width=7,bg='black', font= ('Gabriola',20), fg='lime',relief='raised',bd=3)
    label.grid(row=i*8+2,column=1)
    for m in range(8):
        if (d[m])==None:
            label=Label(clas,text ='Free',width=7,bg='black', font= ('Gabriola',20), fg='lime',relief='raised',bd=5)
            label.grid(row=m*8+3,column=1)
        else:
            label=Label(clas,text =d[m],width=7,bg='black', font= ('Gabriola',20), fg='lime',relief='raised',bd=5)
            label.grid(row=m*8+3,column=1)

    avail_tch=Frame(mainframe,bg='black',relief='groove',bd=5)
    avail_tch.grid(row=i*8+2,column=2)
    label=Label(avail_tch,text ='AVAILABLE TEACHER',width=40,bg='black', font= ('Gabriola',20), fg='lime',relief='raised',bd=3)
    label.grid(row=i*8+2,column=2,columnspan=3)

    cn=2
    for pd in range(8):
        for c in ch_lst:
            cursor.execute("select {} from {} where day='{}' and {} is Null".format(pd_lst[pd],c,dt,pd_lst[pd]))
            ch_data=cursor.fetchone()
            if ch_data!=None:
                label=Label(avail_tch,text =c,width=7,bg='black', font= ('Gabriola',20), fg='lime',relief='raised',bd=5)
                label.grid(row=i*8+3+pd,column=cn)
                cn+=1
            elif cn<3:
                label=Label(avail_tch,text ='None',width=7,bg='black', font= ('Gabriola',20), fg='lime',relief='raised',bd=5)
                label.grid(row=i*8+3+pd,column=cn)
        cn=2
        
mainloop()
