import pandas as pd
import tkinter as tk
from tkinter import ttk

def ddd():
    df = pd.read_csv("C:/Users/MY/Desktop/ds_salaries.csv")
    win = tk.Tk()

    frm = tk.Canvas(win,width=500,height=500)
    frm.place(x=100,y=130)

    sb=ttk.Scrollbar(win,orient=tk.VERTICAL, command=frm.yview)
    sb.pack(side=tk.RIGHT,fill=tk.Y)

    frm.configure(yscrollcommand=sb.set)
    
    treeview = ttk.Treeview(frm,height=1000)
    columns = ['company_size','experience_level']
    treeview['columns']=columns

    for column in columns:
        treeview.heading(column,text=column)
        treeview.column(column,width=100)
    for index, row in df.iterrows():
        values = row[columns].values.tolist()
        treeview.insert('',tk.END,text = index,values=values)

    treeview.place(x=30,y=30)

    frm.bind_all('<MouseWheel>',lambda event:frm.yview_scroll(int(-1*(event.delta/120)),"units"))
    frm.create_window((0,0),window=treeview,anchor=tk.NW)
    frm.update_idletasks()
    frm.configure(scrollregion=frm.bbox("all"))
    
    win.mainloop()
ddd()
    


