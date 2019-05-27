from tkinter import *
def act():
    for i in t_lst:
        k.write(i.get()+'\n')
    k.flush()
    aw.destroy()
#add the address of document where it is saved in your computer, here\\//
k=open('C:\\Users\\Aman\\Desktop\\tkinter\\Absentees.dat','w')
aw=Tk()
aw.title('Assembler')
aw.configure(background="black")
aw.resizable(False,False)

title=Label(aw, text ='ASSEMBLER',bg='black', width=15, font= ('Gabriola',30), fg='lime',relief= 'raised',bd=5)
title.grid(row=0, column= 1,pady=5,padx=5)
inst1=Label(aw, text =('-> Enter 3 character teacher codes in each column.')
           ,bg='black', font= ('Gabriola',15), fg='lime')
inst1.grid(row=2, column= 1)
inst2=Label(aw, text =('-> Then click submit button.')
           ,bg='black', font= ('Gabriola',15), fg='lime')
inst2.grid(row=3, column= 1)

t1= Entry(aw,width=20)
t2= Entry(aw,width=20)
t3= Entry(aw,width=20)
t4= Entry(aw,width=20)
t5= Entry(aw,width=20)
t6= Entry(aw,width=20)
t7= Entry(aw,width=20)
t8= Entry(aw,width=20)
t9= Entry(aw,width=20)
t10= Entry(aw,width=20)
t_lst=[t1,t2,t3,t4,t5,t6,t7,t8,t9,t10]
for i in range (len(t_lst)):
    label = Label(aw, text = ("Teacher",i+1,':'),bg='black', width=15, font= ('Gabriola',15), fg='lime')
    label.grid(row=i+4, column= 0)
    t_lst[i].grid(row=i+4, column= 1,pady=5,padx=5)

sub = Button(aw, text='SUBMIT',bg='black', width=15, font= ('Georgia',10), fg='lime',
              relief='raised',bd=5 ,command= act )
sub.grid(padx=2,row=15, column= 4)

aw.mainloop()
