import os
from tkinter import *
from tkinter import messagebox

#cont = os.system('docker run -d -p 80:80 docker/getting-started')


app = Tk()

def myClick():
      myLabel = Label(app, text='Esta OK!' )
      myLabel.pack()

myButton = Button(app, text='Clique aqui!\nInstalar arquivo', command=myClick ,pady=50,fg='red')
myButton.pack()
app.title('ARQUIVO-1',)
#app.geometry('500x300')
#messagebox.showinfo(title='ARQUIVO-1', message=
#'CONTAINER UP!')

app.mainloop()


