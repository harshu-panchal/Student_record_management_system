from customtkinter import *
from PIL import Image

set_appearance_mode("light")

root = CTk()

root.state('zoomed')
root.config(background="white")


class page:
    def dataa(self):


        frm = CTkFrame(root, width=1375, height=1000,fg_color="white")
        frm.place(x=0,y=0)


        logo_img = CTkImage(Image.open("images/logo.png"), size=(80, 80))
        lg_img = CTkLabel(frm,text="", image=logo_img, fg_color="white")
        lg_img.place(x=210,y=5)

        schl_name = CTkLabel(frm, text="LORD KRISHNA ENGLISH ACADEMY", font=("Cooper Black",45),text_color="red",fg_color="white")
        schl_name.place(x=300,y=20)


        labl = CTkLabel(frm,text="Admission no. : ",font=("Times New Roman",22,"bold"),fg_color="white")
        labl.place(x=120,y=100)

        labl = CTkLabel(frm,text="Admission date : ",font=("Times New Roman",22,"bold"),fg_color="white")
        labl.place(x=120,y=150)

        labl = CTkLabel(frm,text="Name : ",font=("Times New Roman",22,"bold"),fg_color="white")
        labl.place(x=120,y=200)

        labl = CTkLabel(frm,text="Father's Name : ",font=("Times New Roman",22,"bold"),fg_color="white")
        labl.place(x=520,y=200)

        labl = CTkLabel(frm,text="Mobile no. : ",font=("Times New Roman",22,"bold"),fg_color="white")
        labl.place(x=950,y=250)

        labl = CTkLabel(frm,text="Mother's Name : ",font=("Times New Roman",22,"bold"),fg_color="white")
        labl.place(x=120,y=250)

        labl = CTkLabel(frm,text="Religion : ",font=("Times New Roman",22,"bold"),fg_color="white")
        labl.place(x=520,y=250)

        labl = CTkLabel(frm,text="Cast : ",font=("Times New Roman",22,"bold"),fg_color="white")
        labl.place(x=120,y=400)

        labl = CTkLabel(frm,text="Address : ",font=("Times New Roman",22,"bold"),fg_color="white")
        labl.place(x=120,y=300)

        labl = CTkLabel(frm,text="SSSM ID : ",font=("Times New Roman",22,"bold"),fg_color="white")
        labl.place(x=950,y=300)

        labl = CTkLabel(frm,text="UID : ",font=("Times New Roman",22,"bold"),fg_color="white")
        labl.place(x=120,y=350)

        labl = CTkLabel(frm,text="Family SSSMID : ",font=("Times New Roman",22,"bold"),fg_color="white")
        labl.place(x=520,y=350)

        labl = CTkLabel(frm,text="DOB : ",font=("Times New Roman",22,"bold"),fg_color="white")
        labl.place(x=950,y=350)

        labl = CTkLabel(frm,text="Previous School : ",font=("Times New Roman",22,"bold"),fg_color="white")
        labl.place(x=120,y=450)

        labl = CTkLabel(frm,text="Previous Class : ",font=("Times New Roman",22,"bold"),fg_color="white")
        labl.place(x=950,y=450)

        labl = CTkLabel(frm,text="Scholar no. : ",font=("Times New Roman",22,"bold"),fg_color="white")
        labl.place(x=520,y=150)

        labl = CTkLabel(frm,text="Admission Class : ",font=("Times New Roman",22,"bold"),fg_color="white")
        labl.place(x=520,y=400)

        labl = CTkLabel(frm,text="Gender : ",font=("Times New Roman",22,"bold"),fg_color="white")
        labl.place(x=950,y=400)

        labl = CTkLabel(frm,text="Father's Qualification : ",font=("Times New Roman",22,"bold"),fg_color="white")
        labl.place(x=120,y=500)

        labl = CTkLabel(frm,text="Father's Occupation : ",font=("Times New Roman",22,"bold"),fg_color="white")
        labl.place(x=520,y=500)

        labl = CTkLabel(frm,text="Family Income : ",font=("Times New Roman",22,"bold"),fg_color="white")
        labl.place(x=950,y=500)

        labl = CTkLabel(frm,text="Mother's Qualification : ",font=("Times New Roman",22,"bold"),fg_color="white")
        labl.place(x=120,y=550)

        labl = CTkLabel(frm,text="Mother's Occupation : ",font=("Times New Roman",22,"bold"),fg_color="white")
        labl.place(x=520,y=550)


        home_btn4 = CTkButton(frm, text="HomePage",font=("Bahnschrift SemiBold",22),height=50,fg_color="#474747")
        home_btn4.place(x=620,y=625)

s=page()
s.dataa()

root.mainloop()
