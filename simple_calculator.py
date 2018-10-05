#-*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk, Menu, PhotoImage

class Calculator(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        menubar = Menu(self)


        buttons = ['C', '(', ')', '<x','7', '8', '9', '/','4', '5','6','*', '1','2','3', '-', '0', '.','=','+']


        def keypress(event):
            text = result_entry.get()
            label.configure(text="")

            try:
                text=eval(text)
                result.set(text)
            except SyntaxError:
                label.configure(text="Hibás kifejezés")
                #result.set(text)


        result= tk.StringVar()
        result_entry = ttk.Entry(self, text='',textvariable=result,width=40)
        result_entry.bind('<Return>', keypress)
        result_entry.grid(row=0, column=0, columnspan=4, padx=5, pady=10)




        def click(event):
            #print(event.widget.cget("text"))
            t= event.widget.cget("text")
            text = result_entry.get()
            label.configure(text="")
            if t=="<x":
                text=text[:-1]
                result.set(text)
            elif t=="C":
                result.set("")
            elif t=="=":
                try:
                    text=eval(text)
                    result.set(text)
                except SyntaxError:
                    label.configure(text="Hibás kifejezés")
                    #result.set(text)
            else:
                t=text+t
                result.set(t)


        r=1
        c=0

        for button in buttons:
                btn = ttk.Button(self, text=button)
                btn.bind('<Button-1>', click)
                button_bind='<'+button+'>'
                #print(button_bind)
                btn.grid(row=r, column=c, padx=2, pady=2)
                c+=1
                if c==4:
                    c=0
                    r+=1
        frame= tk.Frame(self, relief="sunken")
        frame.grid(row=r+1, column=0,  padx=2, pady=2, columnspan=4)
        label = ttk.Label(frame, text="", foreground="red")
        label.grid(row=0, column=0, padx=2, pady=2)



calc=Calculator()
calc.title("Simple calculator with tkinter")
calc.resizable(False, False)
img = PhotoImage(file='calculator.png')
calc.iconphoto(True, img)
calc.mainloop()