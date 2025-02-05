#print the screen
from customtkinter import *
from PIL import Image
from PIL import ImageGrab
import win32print
import os

set_appearance_mode("light")

def para():
    text="""Amazon Web Services Inc AWS is a subsidiary of Amazon that provides on-demand cloud computing platforms and APIs to individuals companies \nand governments on a metered pay-as-you-go basis Oftentimes clients will use this in combination with autoscaling a process that allows a client to use more computing in times of high application usage and then scale down to reduce costs when there is less traffic These cloud computing web services provide various services related to networking compute storage middleware IoT and other processing capacity as well as software tools via AWS server farms This frees clients from managing scaling and patching hardware and operating systemsOne of the foundational services is Amazon Elastic Compute Cloud EC2 which allows users to have at their disposal a virtual cluster of computers with extremely high availability which can be interacted with over the internet via REST APIs a CLI or the AWS console AWSs virtual computers emulate most of the attributes of a real computerincluding hardware central processing units CPUs and graphics processing units GPUs for processing localRAM memory hard-diskSSD storage a choice of operating systems networking and pre-loaded application software such as web servers databases and customer relationship management CRM.AWS services are delivered to customers via a network of AWS server farms located throughout the world. Fees are based on a combination of usage (known as a Pay-as-you-go model), hardware, operating system, software, or networking features chosen by the subscriber required availability, redundancy, security, and service options. Subscribers can pay for a single virtual AWS computer, a dedicated physical computer, or clusters of either.[7] Amazon provides select portions of security for subscribers (e.g. physical security of the data centers) while other aspects of security are the responsibility of the subscriber (e.g. account management, vulnerability scanning, patching). AWS operates from many global geographical regions including seven in North America.[8]"""
    lbl.insert(END,text)

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


    

root = CTk()

root.state('zoomed')
root.config(background="white")

heading = CTkLabel(root,text = "General Information",fg_color="white",font=("Britannic Bold",45), text_color="red")
heading.pack()

lbl = CTkTextbox(root,font=("Times New Roman",22),height=1000,width=1000)
lbl.pack(pady=50)

print_btn = CTkButton(root,text="Print",command=print_func)
print_btn.place(x=630,y=650)


para()

