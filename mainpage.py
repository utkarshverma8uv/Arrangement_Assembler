from tkinter import *
#add the location of welcome txt file here
hlo=open('C:\\Users\\Aman\\Desktop\\tkinter\\welcome.dat')
#setting-up parent window
m_win=Tk()
m_win.title('Arrangement Assembler')
m_win.configure(background="black")
m_win.resizable(False,False)
#setting-up buttons
asm= Button(m_win, text='Assembler', height= 1, font= ('Georgia',8), bg='white',fg='black', relief= 'groove')
asm.grid(padx=2, pady=2, row=0, column= 0)
db= Button (m_win, text='Database', height= 1, font= ('Georgia',8), bg='white',fg='black', relief= 'groove')
db.grid(padx=2, pady=2, row=0, column= 2)
#displaying the logo
try:
    lg = Canvas(m_win, width = 300, height = 300, bg='black',relief= 'flat' )
    #add the location of logo png  file here
    logo = PhotoImage(file=r'C:\Users\Aman\Desktop\tkinter\logo.png')      
    lg.create_image(22,22, anchor=NW, image=logo)
    lg.grid(row=1, column= 1)
except:
    pass
#displaying welcome message
try:
    wlc = Label(m_win , text = hlo.read() , bg='black', fg= 'lime', font =('Gabriola', 18 ), relief= 'groove')
    wlc.grid(row=2, column= 1)
except:
    pass
end=Label(m_win, bg='black' ).grid(row=3, column= 0)

m_win.mainloop()
