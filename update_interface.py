from customtkinter import *
from tkinter import messagebox
import pandas as pd
from PIL import Image
from tkinter import ttk
from PIL import ImageGrab
import win32print
import os

set_appearance_mode("light")

root = CTk()
root.state('zoomed')
root.config(background="white")

class generate_list:
    column_select = ''
    value_take = ''
    def credential_popup(self):
        def bold_heading(style_name):
            bold_font = CTkFont(weight='bold')
            style = ttk.Style()
            style.configure(style_name, font=bold_font)
        def generate():
            self.column_select = entr_column.get()
            self.value_take = entr_value.get()

            top = CTkToplevel()
            top.state('zoomed')
            top.config(background='white')

            def print_func():
                x=root.winfo_rootx()
                y=root.winfo_rooty()
                width = root.winfo_width()
                height = root.winfo_height()

                screen = ImageGrab.grab(bbox=(x,y,x+width,y+height))
                screen.save("window_ss.png")
                
                image = Image.open("window_ss.png")
                doc_info = ("Print Job",None,'RAW')
                printer_name = win32print.GetDefaultPrinter()
                win32print.SetDefaultPrinter(printer_name)
                prin = win32print.OpenPrinter(printer_name)
                win32print.StartDocPrinter(prin,1,doc_info)
                win32print.StartPagePrinter(prin)
                win32print.WritePrinter(prin,image.tobytes())
                win32print.EndPagePrinter(prin)
                win32print.EndDocPrinter(prin)
                
                os.remove("window_ss.png")

            def data_list():
                df = pd.read_excel("C:/record_save/record.xlsx")

                if self.column_select=='Scholar':
                    self.value_take = int(self.value_take)                

                f = df[df[self.column_select]==self.value_take]       

                frm=CTkFrame(top,fg_color='white')
                frm.grid(row=0,column=0,sticky='nsew')

                top.grid_rowconfigure(0,weight=1)
                top.grid_columnconfigure(0,weight=1)

                labl1 = CTkLabel(frm,text=f"List of Students having {self.column_select} '{self.value_take}'",font=('Arial',20,'bold'))
                labl1.pack()

                labl1 = CTkLabel(frm,text=f"Total number of students = {len(f)}",font=('Arial',18,'bold'))
                labl1.pack()

                treefont = ('arial',11)

                treeview = ttk.Treeview(frm,height=1000)

                treeview.tag_configure('treefont',font=treefont)

                columns = ['Scholar','Admsn no.','Name','Father Name','DOB','SSSM ID','Admsn class','Cast']
                treeview['columns']=columns

                bold_heading('Treeview.Heading')



                for column in columns:
                    treeview.heading(column,text=column)
                    treeview.column(column,width=145)
                for index, row in f.iterrows():
                    values = row[columns].values.tolist()
                    treeview.insert('',END,text = index,values=values,tags=('treefont'))

                treeview.pack()

                click_print = CTkButton(top,text='Print',command=print_func)
                click_print.place(x=600,y=650)

              
            try:   
                data_list()
            except:
                messagebox.showerror("Error","Something went wrong !")
           
            top.mainloop()

        frm = CTkFrame(root, width=400, height=500,fg_color="#d79be8")
        frm.place(x=470,y=100)

        close_btn = CTkButton(frm, text="X",font=("Bahnschrift SemiBold",22),height=10,width=10,fg_color="red",command=frm.destroy)
        close_btn.place(x=375,y=0)

       
        stud_img = CTkImage(Image.open("images/call-sheet.png"), size=(130, 130))
        s_img = CTkLabel(frm,text="", image=stud_img)
        s_img.place(x=135,y=50)
    
        lab = CTkLabel(frm,text='Choose the column name',font=("Bahnschrift SemiLight SemiConde",17))
        lab.place(x=50,y=225)

        lab = CTkLabel(frm,text='Enter the value',font=("Bahnschrift SemiLight SemiConde",17))
        lab.place(x=50,y=310)

        entr_column = CTkComboBox(frm,font=("Bahnschrift SemiLight SemiConde",17),width=300,state="readonly",values=['Scholar','Name','Gender','DOB','Cast','Class'])
        entr_column.place(x=50,y=250)

        entr_value = CTkEntry(frm, font=("Bahnschrift SemiBold",17),width=300)
        entr_value.place(x=50,y=335)

        generate_btn = CTkButton(frm, text="Generate List",font=("Bahnschrift SemiBold",22),height=50,fg_color="#f27b1f",command=generate)
        generate_btn.place(x=125,y=400)

g = generate_list()
g.credential_popup()
        

root.mainloop()
