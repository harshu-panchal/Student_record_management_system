from customtkinter import *
from tkinter import filedialog as fd
import os, shutil

def image_upload():
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
    print(f)

'''
def enable():
    btn1.configure(state="NORMAL")

def dd():
    print("hello")


root = CTk()

btn1 = CTkButton(root,text="hello",state=DISABLED,command=dd)


btn = CTkButton(root, text="upload",command=enable)
btn1.pack()
btn.pack()
'''
root.mainloop()

