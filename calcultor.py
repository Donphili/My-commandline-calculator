from tkinter import Tk
from tkinter import Entry, Button, StringVar




class MyCalcultor():
     def __int__(self, master):
         master.title('Calculator')
         master.geomery("357x420+0+0")
         master.config(bg="black")
         master.resizable(False,False)
         
         self.equation = StringVar()
         self.entry_value = ''
         Entry(width=17, bg='#ccddff', font=('Arial Bold', 28),textvariable=self.equation).place(x=0, y=0)

Button(width=11, height=4, text='(', relief='flat', bg='white', command=lambda:self.show_screen('(')).place(x=0, y=50)
Button(width=11, height=4, text=')', relief='flat', bg='white', command=lambda:self.show_screen(')')).place(x=90, y=50)
Button(width=11, height=4, text='%', relief='flat', bg='white', command=lambda:self.show_screen('%')).place(x=180, y=50)
Button(width=11, height=4, text='1', relief='flat', bg='white', command=lambda:self.show_screen('1')).place(x=0, y=126)
Button(width=11, height=4, text='2', relief='flat', bg='white', command=lambda:self.show_screen('2')).place(x=90, y=125)
Button(width=11, height=4, text='3', relief='flat', bg='white', command=lambda:self.show_screen('3')).place(x=180, y=125)
Button(width=11, height=4, text='4', relief='flat', bg='white', command=lambda:self.show_screen('4')).place(x=0, y=200)
Button(width=11, height=4, text='5', relief='flat', bg='white', command=lambda:self.show_screen('5')).place(x=90, y=200)
Button(width=11, height=4, text='6', relief='flat', bg='white', command=lambda:self.show_screen('6')).place(x=180, y=200)
Button(width=11, height=4, text='7', relief='flat', bg='white', command=lambda:self.show_screen('7')).place(x=0, y=275)
Button(width=11, height=4, text='8', relief='flat', bg='white', command=lambda:self.show_screen('8')).place(x=180, y=275)
Button(width=11, height=4, text='9', relief='flat', bg='white', command=lambda:self.show_screen('9')).place(x=80, y=275)
Button(width=11, height=4, text='.', relief='flat', bg='white', command=lambda:self.show_screen('.')).place(x=180, y=350)
Button(width=11, height=4, text='×', relief='flat', bg='white', command=lambda:self.show_screen('×')).place(x=270, y=275)
Button(width=11, height=4, text='+', relief='flat', bg='white', command=lambda:self.show_screen('+')).place(x=270, y=200)
Button(width=11, height=4, text='-', relief='flat', bg='white', command=lambda:self.show_screen('-')).place(x=270, y=50)
Button(width=11, height=4, text='/', relief='flat', bg='white', command=lambda:self.show_screen('/')).place(x=270, y=127)
Button(width=11, height=4, text='=', relief='flat', bg='lawngreen', command=self.solve_equation).place(x=270, y=350)
Button(width=11, height=4, text='C', relief='flat', bg='red', command=self.clear_screen).place(x=0, y=350)




def  show_screen(self, value):
     self.entry_value+=str(value)
     self.equation.set(self.entry_value)

def  clear_screen(self):#
     self.entry_value= ''
     self.equarion.set(self.entry_value)

def  solve_equation(self):
     result = eval(selt.entry_value)
     self.equation.set(result)

root = Tk()
Calculator=MyCalculator(root)
root.mainloop()
