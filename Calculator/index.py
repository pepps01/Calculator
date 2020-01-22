from tkinter import *
from tkinter import messagebox as msg
    
class Calculator():
    def __init__(self,master= None):
        self.__lastname = "Sunny Pepple"
        self.master = master
        self.master.title("Calculator") 
        self.master.geometry("500x500") 
        self.input_text  = StringVar()
        self.digits = [1,2,3,4,5,6,7,8]
        self.create_widgets()
    # use the geometry ration 
    

    def create_widgets(self):
        self.display_screen = Entry(self.master, textvariable =  self.input_text)
        self.display_screen.pack()

        self.button1 = Button(self.master, text= self.digits[0], command = lambda: self.insert_digit(self.digits[0]))
        self.button1.pack()

        self.button2 = Button(self.master, text= self.digits[1], command = lambda: self.insert_digit(self.digits[1]))
        self.button2.pack()

        self.button3 = Button(self.master, text= self.digits[2], command = lambda: self.insert_digit(self.digits[2]))
        self.button3.pack()

        self.button4 = Button(self.master, text= self.digits[3], command = lambda: self.insert_digit(self.digits[3]))
        self.button4.pack()

        self.button5 = Button(self.master, text= self.digits[4], command = lambda: self.insert_digit(self.digits[4]))
        self.button5.pack()

        self.button6 = Button(self.master, text= self.digits[5], command = lambda: self.insert_digit(self.digits[5]))
        self.button6.pack()

        self.button7 = Button(self.master, text= self.digits[6], command = lambda: self.insert_digit(self.digits[6]))
        self.button7.pack()  
        
        self.button7 = Button(self.master, text= self.digits[6], command = lambda: self.insert_digit(self.digits[7]))
        self.button7.pack()  
        
        self.button8 = Button(self.master, text= self.digits[6], command = lambda: self.insert_digit(self.digits[8]))
        self.button8.pack()  
        
        self.button9 = Button(self.master, text= self.digits[6], command = lambda: self.insert_digit(self.digits[9]))
        self.button9.pack() 

        self.label1 = Label(self.master)
        self.label1.pack()

        

    def insert_digit(self, rool):
        self.label1.config(text = rool)

if __name__ == "__main__":
       root = Tk()
       cal =  Calculator(master = root)
       root.mainloop()

    