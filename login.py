from customtkinter import *
from tkinter import messagebox
from PIL import Image
from PIL import ImageGrab

set_appearance_mode("light")

root = CTk()
root.state('zoomed')
root.config(background="white")


def remove():
    frm.destroy()

# promote class option on home screen

frm = CTkFrame(root,width=1375 ,height=1000 ,fg_color="white")
frm.place(x=0,y=0)

heading = CTkLabel(frm,text = "Educational Details",fg_color="white",font=("Britannic Bold",45), text_color="#add8e6")
heading.place(x=475,y=40)

f_qual_l = CTkLabel(frm,text="Maximum Marks",font=("Times New Roman",22),fg_color="white")
f_qual_l.place(x=270,y=180)

f_occu_l = CTkLabel(frm,text="Obtained Marks",font=("Times New Roman",22),fg_color="white")
f_occu_l.place(x=770,y=180)

m_qual_l = CTkLabel(frm,text="Percentage",font=("Times New Roman",22),fg_color="white")
m_qual_l.place(x=270,y=320)

annual_inc_l = CTkLabel(frm,text="Promot To Class",font=("Times New Roman",22),fg_color="white")
annual_inc_l.place(x=550,y=440)

m_occu_l = CTkLabel(frm,text="Pass OR Fail",font=("Times New Roman",22),fg_color="white")
m_occu_l.place(x=770,y=320)



f_qual_e = CTkEntry(frm, font=("Times New Roman",22), width=300)
f_qual_e.place(x=270,y=210)

f_occu_e = CTkEntry(frm, font=("Times New Roman",22), width=300)
f_occu_e.place(x=770, y=210)

m_qual_e = CTkEntry(frm, font=("Times New Roman",22), width=300)
m_qual_e.place(x=270,y=350)

m_occu_e = CTkComboBox(frm,state="readonly", font=("Times New Roman",22),values = ['Pass','Fail'])
m_occu_e.place(x=770, y=350)

m_qual_e = CTkComboBox(frm,state="readonly", font=("Times New Roman",22),values = ['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th'],width=300)
m_qual_e.place(x=550,y=470)


home_btn3 = CTkButton(frm, text="<<HomePage",font=("Bahnschrift SemiBold",22),height=50,fg_color="#474747")
home_btn3.place(x=400,y=600)
        
save_btn = CTkButton(frm, text="SAVE",font=("Bahnschrift SemiBold",22),height=50,fg_color="#3c7534")
save_btn.place(x=800,y=600)



root.mainloop()
