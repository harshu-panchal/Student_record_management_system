import pandas as pd
from tkinter import ttk
from customtkinter import *

def ddd():
    def bold_heading(style_name):
        bold_font = CTkFont(weight='bold')
        style = ttk.Style()
        style.configure(style_name, font=bold_font)
        
    df = pd.read_csv("C:/Users/MY/Desktop/ds_salaries.csv")
    win =CTk()

    frm=CTkFrame(win)
    frm.grid(row=0,column=0,sticky='nsew')

    win.grid_rowconfigure(0,weight=1)
    win.grid_columnconfigure(0,weight=1)

    
    treeview = ttk.Treeview(frm,height=1000)

    
    
    columns = ['company_size','experience_level']
    treeview['columns']=columns

    bold_heading('Treeview.Heading')


    for column in columns:
        treeview.heading(column,text=column)
        treeview.column(column,width=145)
    for index, row in df.iterrows():
        values = row[columns].values.tolist()
        treeview.insert('',END,text = index,values=values)

    treeview.pack()

    
    
    win.mainloop()
ddd()
    


