import pandas as pd
import tkinter as tk
from tkinter import ttk

class student_list:
    
    def list_page(self):
        def generate_list():
            clear = 0
            df = pd.read_excel("C:/record_save/record.xlsx")
            value = value_e.get()               #requireed value
            req_column = sel_e.get()            #required column name
            if req_column=='Scholar':
                value = int(value)
            

            treeview = ttk.Treeview(frm)
            columns = ['Scholar','Admsn no.','Name','Father Name','DOB','SSSM ID','Admsn class','Cast']
            treeview['columns']=columns

            for column in columns:
                treeview.heading(column,text=column)
                treeview.column(column,width=150)
            for index, row in f.iterrows():
                values = row[columns].values.tolist()
                treeview.insert('',tk.END,text = index,values=values)

            treeview.pack()

            if clear == 1:
                treeview.destroy()
                frm.place_forget()
                
                clear=0
            else:
                frm.place(x=0,y=130)
                clear=1

        def clear_list():
            frm.place_forget()
            
        
        win = tk.Tk()
        win.state('zoomed')

        frm = tk.Canvas(win,width=1000,height=1000)
        frm.place(x=0,y=130)

        sb=ttk.Scrollbar(win,orient=tk.VERTICAL, command=frm.yview)
        sb.pack(side=tk.RIGHT,fill=tk.Y)

        frm.configure(yscrollcommand=sb.set)

        sel_l = tk.Label(win,text="select column name ",font=("Times New Roman",15))
        sel_l.place(x=100,y=40)

        value_l = tk.Label(win,text="enter value ",font=("Times New Roman",15))
        value_l.place(x=850,y=40)

        sel_e = ttk.Combobox(win,font=("Bahnschrift SemiLight SemiConde",15),width=12,state="readonly",values=['Scholar','Name','Gender','DOB','Cast','Class'])
        sel_e.place(x=275,y=40)

        value_e = tk.Entry(win,font=("Bahnschrift SemiLight SemiConde",15))
        value_e.place(x=950,y=40)

        generate_btn = tk.Button(win,text="Generate List",height=1,width=15,font=('Times New Roman',12,"bold"),command=generate_list)
        generate_btn.place(x=900,y=90)

        h=tk.Button(win,text="List",height=1,width=15,font=('Times New Roman',12,"bold"),command=clear_list)
        h.place(x=1000,y=90)
        

s = student_list()
s.list_page()
        

def ddd():
    df = pd.read_csv("C:/Users/MY/Desktop/ds_salaries.csv")
    value='M'                               #requireed value
    f = df[df['company_size']==value]       #required column name

    win = tk.Tk()
    treeview = ttk.Treeview(win,height=1000)
    columns = ['work_year','experience_level','company_size']
    treeview['columns']=columns

    for column in columns:
        treeview.heading(column,text=column)
        treeview.column(column,width=100)
    for index, row in f.iterrows():
        values = row[columns].values.tolist()
        treeview.insert('',tk.END,text = index,values=values)

    treeview.pack()
    #win.mainloop()




