from customtkinter import *
from tkinter import messagebox
import pandas as pd
from CTkTable import *

set_appearance_mode("light")

root = CTk()
root.state('zoomed')
root.config(background="white")
def generate_list():
    clear = 0
    df = pd.read_csv("C:/Users/MY/Desktop/ds_salaries.csv")
    value = "M"               #requireed value
    req_column = 'company_size'            #required column name
    if req_column=='Scholar':
        value = int(value)
    f = df[df[req_column]==value]

    table = CTkTable(root,column=2,row=50,header_color = 'pink',height=20)
        
    columns = ['company_size','experience_level']
    for i in range(len(columns)):
        table.insert(0,i,value=columns[i])
    
    for index, row in f.iterrows():
        values = row[columns].values.tolist()
        table.edit_row(1)

    table.pack()

generate_list()


root.mainloop()
