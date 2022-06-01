import os
from tkinter import *
from time import sleep

app = Tk()
def myClick():
      os.system('docker run -d -p 80:80 docker/getting-started')
      sleep(5)
      app.destroy()
      
myButton1 = Button(app, text='INSTALAR PROGRAMA\nClique aqui', command=myClick ,padx=40,pady=40,fg='white', bg='red')
myButton1.pack()

app.title('ARQUIVO-1',)

#app.geometry('500x300')
#messagebox.showinfo(title='ARQUIVO-1', message=
#'CONTAINER UP!')

app.mainloop()


