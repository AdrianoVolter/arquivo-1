import os
from tkinter import *
from tkinter import messagebox

app = Tk()

def myClick():
      os.system('docker run -d -p 80:80 docker/getting-started')
      
myButton = Button(app, text='Clique aqui!\nInstalar arquivo', command=myClick ,pady=50,fg='red', bg='blue')
myButton.pack()
app.title('ARQUIVO-1',)

#Caixa de mensagem na tela.
#app.geometry('500x300')
#messagebox.showinfo(title='ARQUIVO-1', message=
#'CONTAINER UP!')

app.mainloop()


