from tkinter import filedialog as fd
import tkinter as tk
from tkinter import ttk, messagebox
import os, shutil
import pandas as pd
from openpyxl import Workbook
from customtkinter import *
from PIL import Image,ImageTk,ImageGrab
import win32print
import webbrowser

set_appearance_mode("light")

root = CTk()

root.state('zoomed')
root.config(background="white")
root.geometry("1375x750+20+15")

root.minsize(width=1375, height=750)
root.maxsize(width=1375, height=750)

try:
    root.iconphoto(False,ImageTk.PhotoImage(file='images/teacher.png'))
except:
    None


root.title("School Record Management")

def image_upload():
    global profile
    
    f = fd.askopenfilename(initialdir="/", title="select a file",filetypes=(("jpeg", "*.jpg"), ("png", "*.png")))
    os.chdir('C:\\record_save\\photos')
    shutil.copy(f, 'C:\\record_save\\photos')
    sl = '\\'
    rec = -1
    for i in range(len(f) - 1, 0, -1):
        if (f[i] != "/"):
            rec -= 1
        else:
            break
    st = f[-1:(rec):-1] + sl
    fst = st[-1:-(len(st) + 1):-1]
    f1 = "C:\\record_save\\photos"
    f = f1 + fst
    new_record[27] = f

    profile+=f

    os.chdir(default_dir)



class login:
    def login_page(self):
        def login_():
            userID = entr_user_id.get()
            passwd = entr_psswrd.get()
            if userID == "myschool" and passwd == "123456":
                data = store_data()
                data.create_file()
                home_caller = window()
                home_caller.home_page()
                
                frm.destroy()
            else:
                messagebox.showerror("Error","Username, Password invalid")

        #login page
        #image
        frm = CTkFrame(root, width=1375, height=1000,fg_color="white")
        frm.place(x=0,y=0)
        
        try:
            login_img = CTkImage(Image.open("images/login_img.jpg"), size=(800, 750))
            l_img = CTkLabel(frm,text="", image=login_img)
            l_img.place(x=0,y=0)
        except:
            None

        #labels and entries
        welcome = CTkLabel(frm,text = "Welcome Back!",bg_color="white",font=("Century Schoolbook",35,"bold"),text_color="#836cf5")
        welcome.place(x=800,y=125)

        quote = CTkLabel(frm,text = "Login to continue",bg_color="white",font=("Calibri (Body)",20),text_color="#7f7e82")
        quote.place(x=800,y=175)

        entr_user_id = CTkEntry(frm, font=("Bahnschrift SemiBold",22),fg_color='#f5deb0',text_color="#7f7e82",height=50,width=420)
        entr_user_id.insert(0,"Username")
        entr_user_id.place(x=800,y=245)

        entr_psswrd = CTkEntry(frm, font=("Bahnschrift SemiBold",22),fg_color='#ffc7f4',text_color="#7f7e82",height=50,width=420)
        entr_psswrd.insert(0,"Password")
        entr_psswrd.place(x=800,y=345)

        lgn_btn = CTkButton(frm, text="LOGIN",font=("Bahnschrift SemiBold",22),height=50,fg_color="#e60eba",command=login_)
        lgn_btn.place(x=800,y=445)

        hyper = CTkLabel(frm,text = 'Designed and Developed by Harshvardhan Panchal')
        hyper.place(x=90,y=655)

        def open_link(event):
            webbrowser.open("https://github.com/harshu-panchal")

        hyper_link = CTkLabel(frm,text = 'click here',cursor='hand2',text_color='blue')
        hyper_link.place(x=382,y=655)

        hyper_link.bind("<Button-1>",open_link)


        


class window:
    def home_page(self):
        def add_Data():
            gen = page1()
            gen.general_pg()
            
            frm.destroy()

        root.wm_attributes('-transparentcolor', '#ab23ff')
            


        frm = CTkFrame(root, width=1375, height=1000,fg_color="white")
        frm.place(x=0,y=0)
        
        try:
            backg = Image.open("images/home.jpg")
            rotated = backg.rotate(180)
            home_img = CTkImage(rotated, size=(1400, 730))
            h_img = CTkLabel(frm,text="", image=home_img)
            h_img.place(x=0,y=0)
        except:
            None

        schl_name1 = CTkLabel(frm, text="Welcome TO", font=("Cooper Black",45),text_color="red",fg_color='#f7ca3f')
        schl_name1.place(x=860,y=70)

        schl_name2 = CTkLabel(frm, text="School Dashboard", font=("Cooper Black",35),text_color="red",fg_color="#f7ca3f")
        schl_name2.place(x=860,y=120)

        add_btn = CTkButton(frm,text="Add Student",font=("Bahnschrift SemiBold",22),height=50,width=180,fg_color="#17133b",bg_color='#f7ca3f',text_color="white",command=add_Data)
        add_btn.place(x=850,y=228)

        pr = promot_student()
        promot_btn = CTkButton(frm,text="Promot Student",font=("Bahnschrift SemiBold",22),height=50,width=180,fg_color="#3200bc",bg_color='#f7ca3f',text_color="white",command = pr.promot_entry_page)
        promot_btn.place(x=1070,y=228)

        dl = delete_student()
        del_btn = CTkButton(frm,text="Delete Data",font=("Bahnschrift SemiBold",22),height=50,width=180,fg_color="#e62c2c",bg_color='#f7ca3f',text_color="white",command = dl.delete_entry_page)
        del_btn.place(x=1070,y=320)

        up = update_entry_page()
        up_btn = CTkButton(frm,text="Update Data",font=("Bahnschrift SemiBold",22),height=50,width=180,fg_color="#fe662b",bg_color='#f7ca3f',text_color="white",command=up.credential_page)
        up_btn.place(x=850,y=320)

        sh = show_data()
        show_btn = CTkButton(frm,text="Show Data",font=("Bahnschrift SemiBold",22),height=50,width=180,fg_color="#484848",bg_color='#f7ca3f',text_color="white",command=sh.entry_page)
        show_btn.place(x=850,y=412)

        g = generate_list()
        showlist_btn = CTkButton(frm,text="Show list",font=("Bahnschrift SemiBold",22),height=50,width=180,fg_color="#787878",bg_color='#f7ca3f',text_color="white",command=g.credential_popup)
        showlist_btn.place(x=1070,y=412)

        exit_btn = CTkButton(frm,text="exit",font=("Bahnschrift SemiBold",22),height=50,width=180,fg_color="#36663f",bg_color='#f7ca3f',text_color="white",command=root.destroy)
        exit_btn.place(x=960,y=504)



class page1:
    def general_pg(self):
        def remove():
            frm.destroy()

        def goto_home():
            hm = window()
            hm.home_page()

            remove()

        def dateFormate():
            dd = date_dd_e.get()
            mm = date_mm_e.get()
            yy = date_yy_e.get()
            DAte = dd+'/'+mm+'/'+yy
            return DAte
                
            

        def goto_page2():
            
            mobile = mob_e.get()
            try:
                if len(str(mobile)) != 0 and len(mobile)<10:
                    messagebox.showerror("Error","Invalid mobile number")
                
                elif (len(str(mobile)) == 10 or len(str(mobile))==0) and (isinstance(int(mobile), int)): 
                    pg2 = page2()
                    pg2.student_details()
                
                    record.append(admsn_e.get())
                    record.append(name_e.get())
                    record.append(f_name_e.get())
                    record.append(m_name_e.get())
                    record.append(gender_e.get())
                    record.append(mobile)
                    record.append(cast_e.get())
                    record.append(religion_e.get())
                    record.append(dateFormate())
                    
                    remove()
                elif len(str(mobile)) != 10:
                    messagebox.showerror("Error","Mobile number should contain 10-digits")
            except:
                if len(mobile) == 0:
                    pg2 = page2()
                    pg2.student_details()
                
                    record.append(admsn_e.get())
                    record.append(name_e.get())
                    record.append(f_name_e.get())
                    record.append(m_name_e.get())
                    record.append(gender_e.get())
                    record.append(mobile)
                    record.append(cast_e.get())
                    record.append(religion_e.get())
                    record.append(dateFormate())
                    remove()
                else:
                    messagebox.showerror("Error","Mobile number should contain 10-digits")

                
            

        frm = CTkFrame(root, width=1375, height=1000,fg_color="white")
        frm.place(x=0,y=0)



        heading = CTkLabel(frm,text = "General Information",fg_color="white",font=("Britannic Bold",45), text_color="#add8e6")
        heading.place(x=475,y=40)

        admsn_l = CTkLabel(frm,text="Admission no.",font=("Times New Roman",22),fg_color="white")
        admsn_l.place(x=120,y=150)

        name_l = CTkLabel(frm,text="Full name",font=("Times New Roman",22),fg_color="white")
        name_l.place(x=120,y=255)

        gender_l = CTkLabel(frm,text="Gender",font=("Times New Roman",22),fg_color="white")
        gender_l.place(x=590,y=255)

        date_l = CTkLabel(frm,text="Date of admission",font=("Times New Roman",22),fg_color="white")
        date_l.place(x=1100,y=255)

        f_name_l = CTkLabel(frm,text="Father's name",font=("Times New Roman",22),fg_color="white")
        f_name_l.place(x=290,y=360)

        m_name_l = CTkLabel(frm,text="Mother's name",font=("Times New Roman",22),fg_color="white")
        m_name_l.place(x=740,y=360)

        mob_l = CTkLabel(frm,text="Mobile no.",font=("Times New Roman",22),fg_color="white")
        mob_l.place(x=120,y=465)

        religion_l = CTkLabel(frm,text="Religion",font=("Times New Roman",22),fg_color="white")
        religion_l.place(x=590,y=465)

        cast_l = CTkLabel(frm,text="Cast",font=("Times New Roman",22),fg_color="white")
        cast_l.place(x=1100,y=465)



        admsn_e = CTkEntry(frm,font=("Bahnschrift SemiLight SemiConde",25),width=150)
        admsn_e.place(x=120,y=175)

        name_e = CTkEntry(frm,font=("Bahnschrift SemiLight SemiConde",25),width=325)
        name_e.place(x=120,y=280)

        gender_e = CTkComboBox(frm,state="readonly",font=("Bahnschrift SemiLight SemiConde",25),width=200,values=['male','female'])
        gender_e.place(x=590,y=280)

        date_dd_e = CTkEntry(frm,font=("Bahnschrift SemiLight SemiConde",25),width=50)
        date_dd_e.insert(0,"DD")
        date_dd_e.place(x=1100,y=280)

        date_mm_e = CTkEntry(frm,font=("Bahnschrift SemiLight SemiConde",25),width=50)
        date_mm_e.insert(0,"MM")
        date_mm_e.place(x=1160,y=280)

        date_yy_e = CTkEntry(frm,font=("Bahnschrift SemiLight SemiConde",25),width=80)
        date_yy_e.insert(0," YYYY")
        date_yy_e.place(x=1220,y=280)

        f_name_e = CTkEntry(frm,font=("Bahnschrift SemiLight SemiConde",25),width=325)
        f_name_e.place(x=290,y=385)

        m_name_e = CTkEntry(frm,font=("Bahnschrift SemiLight SemiConde",25),width=325)
        m_name_e.place(x=740,y=385)

        mob_e = CTkEntry(frm,font=("Bahnschrift SemiLight SemiConde",25),width=325)
        mob_e.place(x=120,y=490)

        religion_e = CTkEntry(frm,font=("Bahnschrift SemiLight SemiConde",25),width=325)
        religion_e.place(x=590,y=490)

        cast_e = CTkComboBox(frm,state="readonly",font=("Bahnschrift SemiLight SemiConde",25),width=200,values=['ST','SC','OBC','General'])
        cast_e.place(x=1100,y=490)


        home_btn1 = CTkButton(frm, text="<<HomePage",font=("Bahnschrift SemiBold",22),height=50,fg_color="#474747",command=goto_home)
        home_btn1.place(x=300,y=600)

        img_btn = CTkButton(frm, text="Upload Photo",font=("Bahnschrift SemiBold",22),height=50,fg_color="#f02222",command=image_upload)
        img_btn.place(x=625,y=600)

        next_btn1 = CTkButton(frm, text="NEXT>>",font=("Bahnschrift SemiBold",22),height=50,fg_color="#3c7534",command=goto_page2)
        next_btn1.place(x=900,y=600)



class page2:
    def student_details(self):
        def remove():
            frm.destroy()


            
        def goto_home():
            hm = window()
            hm.home_page()

            remove()

            
        def dateFormate():
            dd = dob_dd_e.get()
            mm = dob_mm_e.get()
            yy = dob_yy_e.get()
            DAte = dd+'/'+mm+'/'+yy
            return DAte
        

        def goto_page3():


            sssm = sss_e.get()
            uid = uid_e.get()
            famID = famID_e.get()

            df = pd.read_excel("C:/record_save/record.xlsx",sheet_name="Sheet1")
            
            try:
                schlr = int(schlr_e.get())
            except:
                schlr=0
                messagebox.showerror("Error","Invalid scholar number")

            try:
                if (len(str(sssm))!=0 and len(str(sssm))<9) and (len(str(uid)) !=0 and len(str(uid)) <12) and (len(str(famID)) !=0 and len(str(famID)) <8):
                    messagebox.showerror("Error","Invalid SSSMID, UID or Family ID number")
                    
                elif (len(str(sssm)) == 9 or len(str(sssm))==0) and (isinstance(int(sssm), int))and (len(str(uid)) == 12 or len(str(uid))==0) and (isinstance(int(uid), int)) and (len(str(famID)) == 8 or len(str(famID))==0) and (isinstance(int(famID), int)):
                    if schlr in df['Scholar'].values:
                        messagebox.showerror("Error","Scholar number already exist")
                    elif len(str(schlr))<3:
                        messagebox.showerror("Error","Invalid Scholar number")
                    elif (schlr not in df['Scholar'].values and len(str(schlr))>=3 ):
                        pg3 = page3()
                        pg3.parent_details()
                        record.append(addr_e.get())
                        record.append(sssm)      
                        record.append(uid)      
                        record.append(famID)
                        record.append(dateFormate())
                        record.append(prev_scl_e.get())
                        record.append(prev_cls_e.get())
                        record.append(schlr)
                        record.append(adm_cls_e.get())
                        remove()

                elif len(str(sssm)) !=9 or len(str(uid)) !=12 or len(str(famID)) !=8 :
                    messagebox.showerror("Error","Invalid SSSMID, UID or Family ID number")

            except:
                if len(sssm)==0 and len(uid)==0 and len(famID)==0:
                    if schlr in df['Scholar'].values:
                        messagebox.showerror("Error","Scholar number already exist")
                    elif len(str(schlr))<3:
                        messagebox.showerror("Error","Invalid Scholar number")
                    elif (schlr not in df['Scholar'].values and len(str(schlr))>=3 ):
                        pg3 = page3()
                        pg3.parent_details()
                        record.append(addr_e.get())
                        record.append(sssm)      
                        record.append(uid)      
                        record.append(famID)
                        record.append(dateFormate())
                        record.append(prev_scl_e.get())
                        record.append(prev_cls_e.get())
                        record.append(schlr)
                        record.append(adm_cls_e.get())
                        remove()
                else:
                    messagebox.showerror("Error","Invalid SSSMID, UID or Family ID number")

                
            
        frm = CTkFrame(root, width=1375, height=1000,fg_color="white")
        frm.place(x=0,y=0)


        
        heading = CTkLabel(frm,text = "Student Details",fg_color="white",font=("Britannic Bold",45), text_color="#eb7134")
        heading.place(x=510,y=40)

        addr_l = CTkLabel(frm,text="Address",font=("Times New Roman",22),fg_color="white")
        addr_l.place(x=120,y=150)

        sss_l = CTkLabel(frm,text="SSSM ID",font=("Times New Roman",22),fg_color="white")
        sss_l.place(x=800,y=150)

        uid_l = CTkLabel(frm,text="UID",font=("Times New Roman",22),fg_color="white")
        uid_l.place(x=290,y=255)

        famID_l = CTkLabel(frm,text="Family ID",font=("Times New Roman",22),fg_color="white")
        famID_l.place(x=740,y=255)

        dob_l = CTkLabel(frm,text="DOB",font=("Times New Roman",22),fg_color="white")
        dob_l.place(x=120,y=360)

        prev_scl_l = CTkLabel(frm,text="Previous School",font=("Times New Roman",22),fg_color="white")
        prev_scl_l.place(x=500,y=360)

        prev_cls_l = CTkLabel(frm,text="Previous Class",font=("Times New Roman",22),fg_color="white")
        prev_cls_l.place(x=120,y=465)

        schlr_l = CTkLabel(frm,text="Scholar no.",font=("Times New Roman",22),fg_color="white")
        schlr_l.place(x=550,y=465)

        adm_cls_l = CTkLabel(frm,text="Admission Class",font=("Times New Roman",22),fg_color="white")
        adm_cls_l.place(x=1060,y=465)



        addr_e = CTkEntry(frm,font=("Bahnschrift SemiLight SemiConde",25),width=600)
        addr_e.place(x=120,y=175)

        sss_e = CTkEntry(frm,font=("Bahnschrift SemiLight SemiConde",25),width=300)
        sss_e.place(x=800,y=175)

        uid_e = CTkEntry(frm,font=("Bahnschrift SemiLight SemiConde",25),width=400)
        uid_e.place(x=290,y=280)

        famID_e = CTkEntry(frm,font=("Bahnschrift SemiLight SemiConde",25),width=400)
        famID_e.place(x=740,y=280)

        dob_dd_e = CTkEntry(frm,font=("Bahnschrift SemiLight SemiConde",25),width=50)
        dob_dd_e.insert(0,"DD")
        dob_dd_e.place(x=120,y=385)

        dob_mm_e = CTkEntry(frm,font=("Bahnschrift SemiLight SemiConde",25),width=50)
        dob_mm_e.insert(0,"MM")
        dob_mm_e.place(x=180,y=385)

        dob_yy_e = CTkEntry(frm,font=("Bahnschrift SemiLight SemiConde",25),width=80)
        dob_yy_e.insert(0," YYYY")
        dob_yy_e.place(x=240,y=385)
                
        prev_scl_e = CTkEntry(frm,font=("Bahnschrift SemiLight SemiConde",25),width=600)
        prev_scl_e.place(x=500,y=385)

        prev_cls_e = CTkComboBox(frm,font=("Bahnschrift SemiLight SemiConde",25),width=200,state="readonly",values=['Nursery','LKG','UKG','1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th'])
        prev_cls_e.place(x=120,y=490)

        schlr_e = CTkEntry(frm,font=("Bahnschrift SemiLight SemiConde",25),width=300)
        schlr_e.place(x=550,y=490)

        adm_cls_e = CTkComboBox(frm,font=("Bahnschrift SemiLight SemiConde",25),width=200,state="readonly",values=['Nursery','LKG','UKG','1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th'])
        adm_cls_e.place(x=1060,y=490)



        home_btn2 = CTkButton(frm, text="<<HomePage",font=("Bahnschrift SemiBold",22),height=50,fg_color="#474747",command=goto_home)
        home_btn2.place(x=400,y=600)

        next_btn2 = CTkButton(frm, text="NEXT>>",font=("Bahnschrift SemiBold",22),height=50,fg_color="#3c7534",command=goto_page3)
        next_btn2.place(x=800,y=600)



class page3:
    def parent_details(self):
        def remove():
            frm.destroy()


        def goto_home():
            hom2 = window()
            hom2.home_page()

            remove()

        def save_data():
            record.append(f_qual_e.get())
            record.append(f_occu_e.get())
            record.append(m_qual_e.get())
            record.append(m_occu_e.get())
            record.append(annual_inc_e.get())

            os.chdir(default_dir)
            
            hom2 = window()
            hom2.home_page()
            remove()

            
            try:
                save =  store_data()
                save.store()
                messagebox.showinfo("Done","Data saved successfully")
            except:
                messagebox.showerror("Error","Something went wrong")
                
            
            
        frm = CTkFrame(root, width=1375, height=1000,fg_color="white")
        frm.place(x=0,y=0)

    
        heading = CTkLabel(frm,text = "Parent's Detail",fg_color="white",font=("Britannic Bold",45), text_color="#5cdb95")
        heading.place(x=525,y=40)

        f_qual_l = CTkLabel(frm,text="Father's Qualification",font=("Times New Roman",22),fg_color="white")
        f_qual_l.place(x=270,y=180)

        f_occu_l = CTkLabel(frm,text="Occupation",font=("Times New Roman",22),fg_color="white")
        f_occu_l.place(x=770,y=180)

        m_qual_l = CTkLabel(frm,text="Mother's Qualification",font=("Times New Roman",22),fg_color="white")
        m_qual_l.place(x=270,y=320)

        m_occu_l = CTkLabel(frm,text="Occupation",font=("Times New Roman",22),fg_color="white")
        m_occu_l.place(x=770,y=320)

        annual_inc_l = CTkLabel(frm,text="Annual Income",font=("Times New Roman",22),fg_color="white")
        annual_inc_l.place(x=550,y=440)


        f_qual_e = CTkComboBox(frm,state="readonly", font=("Times New Roman",22),values = ['primary','middle','secondary','senior secondary','diploma','undergraduate','postgraduate','PhD holder'],width=300)
        f_qual_e.place(x=270,y=210)

        f_occu_e = CTkEntry(frm, font=("Times New Roman",22), width=300)
        f_occu_e.place(x=770, y=210)

        m_qual_e = CTkComboBox(frm,state="readonly", font=("Times New Roman",22),values = ['primary','middle','secondary','senior secondary','diploma','undergraduate','postgraduate','PhD holder'],width=300)
        m_qual_e.place(x=270,y=350)

        m_occu_e = CTkEntry(frm, font=("Times New Roman",22), width=300)
        m_occu_e.place(x=770, y=350)

        annual_inc_e = CTkEntry(frm, font=("Times New Roman",22), width=300)
        annual_inc_e.place(x=550,y=470)


        home_btn3 = CTkButton(frm, text="<<HomePage",font=("Bahnschrift SemiBold",22),height=50,fg_color="#474747",command=goto_home)
        home_btn3.place(x=400,y=600)
        
        save_btn = CTkButton(frm, text="SAVE",font=("Bahnschrift SemiBold",22),height=50,fg_color="#3c7534",command=save_data)
        save_btn.place(x=800,y=600)



class store_data:
    def create_file(self):
        filename = "record.xlsx"
        folder = "C:/record_save"

        os.makedirs(folder,exist_ok=True)

        path1 = "C:/record_save"

        file_path = os.path.join(path1,filename)

        if not os.path.exists(file_path):
            workbook = Workbook()

            sheet = workbook.active

            sheet["A1"]="Scholar"
            sheet["B1"]="Admsn no."
            sheet["C1"]="Name"          
            sheet["D1"]="Father Name"
            sheet["E1"]="Mother Name"
            sheet["F1"]="Mobile"
            sheet["G1"]="Address"
            sheet["H1"]="SSSM ID"
            sheet["I1"]="UID"
            sheet["J1"]="DOB"
            sheet["K1"]="Prev schl"
            sheet["L1"]="Prev class"
            sheet["M1"]="Admsn class"
            sheet["N1"]="Gender"
            sheet["O1"]="Admsn date"
            sheet["P1"]="Religion"
            sheet["Q1"]="Cast"
            sheet["R1"]="Family sssmid"
            sheet["S1"]="Father qual"
            sheet["T1"]="F_Occupation"
            sheet["U1"]="Mother qual"
            sheet["V1"]="M_Occupation"
            sheet["W1"]="Annual income"
            sheet["X1"]="Total marks"
            sheet["Y1"]="Obtained marks"
            sheet["Z1"]="Percentage"
            sheet["AA1"]="Pass/Fail"
            sheet["AB1"]="image"

            workbook.save(file_path)
           


    def store(self):
        global record
        global profile
        new_record = [record[16],record[0],record[1],record[2],record[3],record[5],
                      record[9],record[10],record[11],record[13],record[14],record[15],
                      record[17],record[4],record[8],record[7],record[6],record[12],
                      record[18],record[19],record[20],record[21],record[22],'','','','',
                      profile]
        record=[]
        profile=''
            
        try:
            df = pd.read_excel("C:/record_save/record.xlsx", sheet_name='Sheet')
        except:
            df = pd.read_excel("C:/record_save/record.xlsx", sheet_name='Sheet1')
    
        df_new = pd.DataFrame([new_record],columns=df.columns)

        df_concatenated = pd.concat([df,df_new],ignore_index=True)

        df_concatenated.to_excel( "C:/record_save/record.xlsx",index=False)



#   SHOW DATA __---------------------------------------______________________________

class show_data:
    def entry_page(self):
        global show_record
        def remove():
            frm.destroy()

            
        def show():
            global show_record
            try:
                primary_value1 = int(entr_scholar.get())
            except:
                primary_value1 = 0
            primary_value2 = entr_student_name.get()
            
            df = pd.read_excel("C:/record_save/record.xlsx",sheet_name="Sheet1")

            

            if primary_value1 in df['Scholar'].values:
                filtered_df = df[df['Scholar'] == primary_value1]
                data_row = filtered_df.values.tolist()
                show_list = []
                show_list.append(data_row)
                show_list2 = []
                show_list2 = [item for sublist1 in show_list for sublist2 in sublist1 for item in sublist2]
                show_record.append(show_list2)
                remove()
                show_list=[]
                show_list2=[]
                
                dis = display()
                dis.display_page()
            elif primary_value2 in df['Name'].values:
                filtered_df = df[df['Name'] == primary_value2]
                data_row = filtered_df.values.tolist()
                show_list = []
                show_list.append(data_row)
                show_list2 = []
                show_list2 = [item for sublist1 in show_list for sublist2 in sublist1 for item in sublist2]
                show_record.append(show_list2)
                remove()
                show_list=[]
                show_list2=[]
                
                dis = display()
                dis.display_page()
            else:
                messagebox.showerror("Error","NO such student available in excel sheet")


        frm = CTkFrame(root, width=400, height=500,fg_color="#77a6f7")
        frm.place(x=470,y=100)

        close_btn = CTkButton(frm, text="X",font=("Bahnschrift SemiBold",22),height=10,width=10,fg_color="red",command=frm.destroy)
        close_btn.place(x=375,y=0)

        try:
            stud_img = CTkImage(Image.open("images/student.png"), size=(180, 180))
            s_img = CTkLabel(frm,text="", image=stud_img)
            s_img.place(x=105,y=50)
        except:
            None


        entr_student_name = CTkEntry(frm, font=("Bahnschrift SemiBold",22),text_color="#7f7e82",height=50,width=300)
        entr_student_name.insert(0,"Student Name")
        entr_student_name.place(x=50,y=250)

        entr_scholar = CTkEntry(frm, font=("Bahnschrift SemiBold",22),text_color="#7f7e82",height=50,width=300)
        entr_scholar.insert(0,"Scholar Number")
        entr_scholar.place(x=50,y=320)


        show_btn = CTkButton(frm, text="Show",font=("Bahnschrift SemiBold",22),height=50,fg_color="#00887a",command=show)
        show_btn.place(x=125,y=400)


        

class display:

    def display_page(self):
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

        

        def goto_home():
            hom = window()
            hom.home_page()
            frm.destroy()

            
        global show_record
        frm = CTkFrame(root, width=1375, height=1000,fg_color="white")
        frm.place(x=0,y=0)

        try:
            logo_img = CTkImage(Image.open("images/logo.png"), size=(80, 80))
            lg_img = CTkLabel(frm,text="", image=logo_img, fg_color="white")
            lg_img.place(x=210,y=5)
        except:
            None

        schl_name = CTkLabel(frm, text="Your Student's Data", font=("Cooper Black",45),text_color="red",fg_color="white")
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

        labl = CTkLabel(frm,text="Family SSSM ID : ",font=("Times New Roman",22,"bold"),fg_color="white")
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


        home_btn4 = CTkButton(frm, text="HomePage",font=("Bahnschrift SemiBold",22),height=50,fg_color="#474747",command=goto_home)
        home_btn4.place(x=700,y=625)

        print_btn2 = CTkButton(frm, text="Print",font=("Bahnschrift SemiBold",22),height=50,command=print_func)
        print_btn2.place(x=520,y=625)
        

        #show record _________________-------------
  

        try:
            img = CTkImage(Image.open(show_record[0][27]), size=(80, 110))
            btn = CTkButton(frm, text='', height=100, width=100, image=img, bg_color="white", border_color="black",fg_color="white",hover_color="white",border_width=2)
            btn.place(x=1100, y=100)
        except:
            btn = CTkButton(frm, text='Image is not\n available', text_color="black", height=120, width=120, bg_color="white",border_color="black", fg_color="white", hover_color="white", border_width=2)
            btn.place(x=1100, y=100)

        
        
        labl = CTkLabel(frm,text=show_record[0][1],font=("Times New Roman",22),fg_color="white")
        labl.place(x=270,y=100)

        labl = CTkLabel(frm,text=show_record[0][14],font=("Times New Roman",22),fg_color="white")
        labl.place(x=285,y=150)

        labl = CTkLabel(frm,text=show_record[0][2],font=("Times New Roman",22),fg_color="white")
        labl.place(x=195,y=200)

        labl = CTkLabel(frm,text=show_record[0][3],font=("Times New Roman",22),fg_color="white")
        labl.place(x=680,y=200)

        labl = CTkLabel(frm,text=show_record[0][13],font=("Times New Roman",22),fg_color="white")
        labl.place(x=1045,y=400)

        labl = CTkLabel(frm,text=show_record[0][4],font=("Times New Roman",22),fg_color="white")
        labl.place(x=282,y=250)

        labl = CTkLabel(frm,text=show_record[0][15],font=("Times New Roman",22),fg_color="white")
        labl.place(x=615,y=250)

        labl = CTkLabel(frm,text=show_record[0][16],font=("Times New Roman",22),fg_color="white")
        labl.place(x=180,y=400)

        labl = CTkLabel(frm,text=show_record[0][6],font=("Times New Roman",22),fg_color="white")
        labl.place(x=220,y=300)

        labl = CTkLabel(frm,text=show_record[0][7],font=("Times New Roman",22),fg_color="white")
        labl.place(x=1055,y=300)

        labl = CTkLabel(frm,text=show_record[0][8],font=("Times New Roman",22),fg_color="white")
        labl.place(x=180,y=350)

        labl = CTkLabel(frm,text=show_record[0][17],font=("Times New Roman",22),fg_color="white")
        labl.place(x=700,y=350)

        labl = CTkLabel(frm,text=show_record[0][9],font=("Times New Roman",22),fg_color="white")
        labl.place(x=1020,y=350)

        labl = CTkLabel(frm,text=show_record[0][10],font=("Times New Roman",22),fg_color="white")
        labl.place(x=293,y=450)

        labl = CTkLabel(frm,text=show_record[0][11],font=("Times New Roman",22),fg_color="white")
        labl.place(x=1110,y=450)

        labl = CTkLabel(frm,text=show_record[0][0],font=("Times New Roman",22),fg_color="white")
        labl.place(x=645,y=150)

        labl = CTkLabel(frm,text=show_record[0][12],font=("Times New Roman",22),fg_color="white")
        labl.place(x=700,y=400)

        labl = CTkLabel(frm,text=show_record[0][5],font=("Times New Roman",22),fg_color="white")
        labl.place(x=1065,y=250)

        labl = CTkLabel(frm,text=show_record[0][18],font=("Times New Roman",22),fg_color="white")
        labl.place(x=344,y=500)

        labl = CTkLabel(frm,text=show_record[0][19],font=("Times New Roman",22),fg_color="white")
        labl.place(x=730,y=500)

        labl = CTkLabel(frm,text=show_record[0][22],font=("Times New Roman",22),fg_color="white")
        labl.place(x=1115,y=500)

        labl = CTkLabel(frm,text=show_record[0][20],font=("Times New Roman",22),fg_color="white")
        labl.place(x=353,y=550)

        labl = CTkLabel(frm,text=show_record[0][21],font=("Times New Roman",22),fg_color="white")
        labl.place(x=740,y=550)

        show_record=[]


class update_entry_page:

    def credential_page(self):
        def goto_update_page():
            global scholar_no
            
            try:
                scholar_no = int(entr_scholar.get())
            except:
                scholar_no = 0
            
            
            df = pd.read_excel("C:/record_save/record.xlsx",sheet_name="Sheet1")
            if scholar_no in df['Scholar'].values:
                frm.destroy()
                page = update_final()
                page.update_page()
            else:
                messagebox.showerror("Error","Scholar number do not exist!")



        frm = CTkFrame(root, width=400, height=500,fg_color='#a64ac9')
        frm.place(x=470,y=100)

        try:
            stud_img = CTkImage(Image.open("images/data-recovery.png"), size=(180, 180))
            s_img = CTkLabel(frm,text="", image=stud_img)
            s_img.place(x=105,y=50)
        except:
            None
        
        close_btn = CTkButton(frm, text="X",font=("Bahnschrift SemiBold",22),height=10,width=10,fg_color="red",command=frm.destroy)
        close_btn.place(x=375,y=0)


        entr_student_name = CTkEntry(frm, font=("Bahnschrift SemiBold",22),text_color="#7f7e82",height=50,width=300)
        entr_student_name.insert(0,"Student Name")
        entr_student_name.place(x=50,y=250)

        entr_scholar = CTkEntry(frm, font=("Bahnschrift SemiBold",22),text_color="#7f7e82",height=50,width=300)
        entr_scholar.insert(0,"Scholar Number")
        entr_scholar.place(x=50,y=320)


        update_btn = CTkButton(frm, text="Update",font=("Bahnschrift SemiBold",22),height=50,fg_color="#61892f",command=goto_update_page)
        update_btn.place(x=125,y=400)



class update_final():
    def update_page(self):
        def goto_home():
            hom = window()
            hom.home_page()
            frm.destroy()
            
        def update():
            df = pd.read_excel("C:/record_save/record.xlsx",sheet_name="Sheet1")
            column = sel_e.get()
            if column == '':
                messagebox.showerror("Error","Please select a column")
            else:
                new_value = new_val_e.get()

                ind=df['Scholar'].tolist().index(scholar_no)   

                df.loc[ind,column] = new_value           

                df.to_excel("C:/record_save/record.xlsx",index = False)

                messagebox.showinfo("Done","data updated successfully")


        
        frm = CTkFrame(root,width=1375 ,height=1000 ,fg_color="white")
        frm.place(x=0,y=0)

        heading = CTkLabel(frm,text = "Update Details",fg_color="white",font=("Britannic Bold",45), text_color="#add8e6")
        heading.place(x=550,y=40)

        sel_l = CTkLabel(frm,text="Select what to update",font=("Times New Roman",22),fg_color="white")
        sel_l.place(x=300,y=200)

        new_val_l = CTkLabel(frm,text="What is the new value",font=("Times New Roman",22),fg_color="white")
        new_val_l.place(x=850,y=200)


        sel_e = CTkComboBox(frm,state="readonly",font=("Bahnschrift SemiLight SemiConde",25),width=200,values = ['Name','Father Name','Mother Name','Mobile','Address','SSSM ID','UID','DOB','Prev schl','Prev class','Admsn class','Gender','Cast','Family sssmid','Annual income','Total marks','Obtained marks','Percentage','Pass/fail','image'])
        sel_e.place(x=300,y=225)

        new_val_e = CTkEntry(frm,font=("Bahnschrift SemiLight SemiConde",25),width=300)
        new_val_e.place(x=850,y=225)


        updt_btn = CTkButton(frm, text="Update",font=("Bahnschrift SemiBold",22),height=50,fg_color="#6d7829",command=update)
        updt_btn.place(x=600,y=400)

        hom_btn = CTkButton(frm, text="HomePage",font=("Bahnschrift SemiBold",22),height=50,fg_color="#482978",command=goto_home)
        hom_btn.place(x=600,y=500)


class promot_student:
    def promot_entry_page(self):
        def goto_promot_page():
            global scholar_no
            
            try:
                scholar_no = int(entr_scholar.get())
            except:
                scholar_no = 0
            
            
            df = pd.read_excel("C:/record_save/record.xlsx",sheet_name="Sheet1")
            if scholar_no in df['Scholar'].values:
                frm.destroy()
                page = promot_final()
                page.promot_page()
            else:
                messagebox.showerror("Error","Scholar number do not exist!")

        
        frm = CTkFrame(root, width=400, height=500,fg_color='#5cdb95')
        frm.place(x=470,y=100)

        try:
            stud_img = CTkImage(Image.open("images/next-level.png"), size=(180, 180))
            s_img = CTkLabel(frm,text="", image=stud_img)
            s_img.place(x=105,y=50)
        except:
            None
        
        close_btn = CTkButton(frm, text="X",font=("Bahnschrift SemiBold",22),height=10,width=10,fg_color="red",command=frm.destroy)
        close_btn.place(x=375,y=0)


        entr_student_name = CTkEntry(frm, font=("Bahnschrift SemiBold",22),text_color="#7f7e82",height=50,width=300)
        entr_student_name.insert(0,"Student Name")
        entr_student_name.place(x=50,y=250)

        entr_scholar = CTkEntry(frm, font=("Bahnschrift SemiBold",22),text_color="#7f7e82",height=50,width=300)
        entr_scholar.insert(0,"Scholar Number")
        entr_scholar.place(x=50,y=320)


        promot_btn = CTkButton(frm, text="Promot",font=("Bahnschrift SemiBold",22),height=50,fg_color="#05386b",command=goto_promot_page)
        promot_btn.place(x=125,y=400)


class promot_final:
    def promot_page(self):
        def goto_home():
            hom = window()
            hom.home_page()
            frm.destroy()
            

        def promot():
            df = pd.read_excel("C:/record_save/record.xlsx",sheet_name="Sheet1")
            max_mark = max_e.get()
            obt_mark = obt_e.get()
            percent = per_e.get()
            classs = cls_e.get()
            passOrFail = p_f_e.get()

            if max_mark=='' or obt_mark=='' or percent=='' or classs=='' or passOrFail=='':
                messagebox.showerror("Error","Please fill all the details")
            else:
                ind=df['Scholar'].tolist().index(scholar_no)   

                df.loc[ind,'Total marks'] = max_mark
                df.loc[ind,'Obtained marks'] = obt_mark
                df.loc[ind,'Percentage'] = percent
                df.loc[ind,'Admsn class'] = classs
                df.loc[ind,'Pass/Fail'] = passOrFail

                df.to_excel("C:/record_save/record.xlsx",index = False)

                goto_home()

                messagebox.showinfo("Done","data updated successfully")



        
        frm = CTkFrame(root,width=1375 ,height=1000 ,fg_color="white")
        frm.place(x=0,y=0)

        heading = CTkLabel(frm,text = "Educational Details",fg_color="white",font=("Britannic Bold",45), text_color="#add8e6")
        heading.place(x=475,y=40)

        max_l = CTkLabel(frm,text="Maximum Marks",font=("Times New Roman",22),fg_color="white")
        max_l.place(x=270,y=180)

        obt_l = CTkLabel(frm,text="Obtained Marks",font=("Times New Roman",22),fg_color="white")
        obt_l.place(x=770,y=180)

        per_l = CTkLabel(frm,text="Percentage",font=("Times New Roman",22),fg_color="white")
        per_l.place(x=270,y=320)

        cls_l = CTkLabel(frm,text="Promot To Class",font=("Times New Roman",22),fg_color="white")
        cls_l.place(x=550,y=440)

        p_f_l = CTkLabel(frm,text="Pass OR Fail",font=("Times New Roman",22),fg_color="white")
        p_f_l.place(x=770,y=320)



        max_e = CTkEntry(frm, font=("Times New Roman",22), width=300)
        max_e.place(x=270,y=210)

        obt_e = CTkEntry(frm, font=("Times New Roman",22), width=300)
        obt_e.place(x=770, y=210)

        per_e = CTkEntry(frm, font=("Times New Roman",22), width=300)
        per_e.place(x=270,y=350)

        p_f_e = CTkComboBox(frm,state="readonly", font=("Times New Roman",22),values = ['Pass','Fail'])
        p_f_e.place(x=770, y=350)

        cls_e = CTkComboBox(frm,state="readonly", font=("Times New Roman",22),values = ['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th'],width=300)
        cls_e.place(x=550,y=470)


        home_btn3 = CTkButton(frm, text="<<HomePage",font=("Bahnschrift SemiBold",22),height=50,fg_color="#474747",command=goto_home)
        home_btn3.place(x=400,y=600)
                
        save_btn = CTkButton(frm, text="SAVE",font=("Bahnschrift SemiBold",22),height=50,fg_color="#3c7534",command = promot)
        save_btn.place(x=800,y=600)


#________________DELETE DATA__________________________________
class delete_student:
    def delete_entry_page(self):
        def confirm_delete():
            global scholar_no
            
            try:
                scholar_no = int(entr_scholar.get())
            except:
                scholar_no = 0
            
            
            df = pd.read_excel("C:/record_save/record.xlsx",sheet_name="Sheet1")
            if scholar_no in df['Scholar'].values:
                result = messagebox.askquestion("Confirm?","Are you sure you want to delete data Permanently?",icon='warning')
                if result=='yes':
                    df = pd.read_excel("C:/record_save/record.xlsx",sheet_name="Sheet1")
                    filtered_df = df[df['Scholar'] != scholar_no]
                    filtered_df.to_excel("C:/record_save/record.xlsx",index=False)
                    messagebox.showinfo("Done","Data deleted successfully !")
                    frm.destroy()
                else:
                    frm.destroy()

            else:
                messagebox.showerror("Error","Scholar number do not exist!")

        
        frm = CTkFrame(root, width=400, height=500,fg_color='#d4a59a')
        frm.place(x=470,y=100)

        try:
            stud_img = CTkImage(Image.open("images/folder.png"), size=(180, 180))
            s_img = CTkLabel(frm,text="", image=stud_img)
            s_img.place(x=110,y=50)
        except:
            None
        
        close_btn = CTkButton(frm, text="X",font=("Bahnschrift SemiBold",22),height=10,width=10,fg_color="red",command=frm.destroy)
        close_btn.place(x=375,y=0)


        entr_student_name = CTkEntry(frm, font=("Bahnschrift SemiBold",22),text_color="#7f7e82",height=50,width=300)
        entr_student_name.insert(0,"Student Name")
        entr_student_name.place(x=50,y=250)

        entr_scholar = CTkEntry(frm, font=("Bahnschrift SemiBold",22),text_color="#7f7e82",height=50,width=300)
        entr_scholar.insert(0,"Scholar Number")
        entr_scholar.place(x=50,y=320)


        delete_btn = CTkButton(frm, text="Delete",font=("Bahnschrift SemiBold",22),height=50,fg_color="#844d36",command=confirm_delete)
        delete_btn.place(x=125,y=400)



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

        frm = CTkFrame(root, width=400, height=500,fg_color="#31ec56")
        frm.place(x=470,y=100)

        close_btn = CTkButton(frm, text="X",font=("Bahnschrift SemiBold",22),height=10,width=10,fg_color="red",command=frm.destroy)
        close_btn.place(x=375,y=0)

        try:
            stud_img = CTkImage(Image.open("images/call-sheet.png"), size=(130, 130))
            s_img = CTkLabel(frm,text="", image=stud_img)
            s_img.place(x=135,y=50)
        except:
            None
    
        lab = CTkLabel(frm,text='Choose the column name',font=("Bahnschrift SemiLight SemiConde",17))
        lab.place(x=50,y=225)

        lab = CTkLabel(frm,text='Enter the value',font=("Bahnschrift SemiLight SemiConde",17))
        lab.place(x=50,y=310)

        entr_column = CTkComboBox(frm,font=("Bahnschrift SemiLight SemiConde",17),width=300,state="readonly",values=['Scholar','Name','Gender','DOB','Cast','Class'])
        entr_column.place(x=50,y=250)

        entr_value = CTkEntry(frm, font=("Bahnschrift SemiBold",17),width=300)
        entr_value.place(x=50,y=335)

        generate_btn = CTkButton(frm, text="Generate List",font=("Bahnschrift SemiBold",22),height=50,fg_color="#ef036c",command=generate)
        generate_btn.place(x=125,y=400)

     
if __name__ == "__main__":
    default_dir = os.getcwd()
    
    profile=''
    record = []
    data_row =[]
    show_record = []

    new_record = ['','','','','','','','','','','','','','','','','','','','','','','','','','','','']

    scholar_no=0
    
    app = login()
    app.login_page() 

root.mainloop()
