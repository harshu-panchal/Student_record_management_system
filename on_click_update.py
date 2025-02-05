

from customtkinter import *

set_appearance_mode("light")

root = CTk()
root.state('zoomed')
root.config(background="white")

c = CTkCanvas(root,width=200,height=300)
c.pack()

t= CTkTabview(root)
t.insert(0,"dfgh")
t.insert(1,'sdsc')
t.pack()

l=CTkLabel(t,text="wvwd")


line=30
for i in range(90):
    c.create_line(4, line, 630, line)
    line += 30
                

root.mainloop()
