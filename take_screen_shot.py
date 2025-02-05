
#function for taking a screen shot of the tkinter window through a button
from PIL import ImageGrab
def ss():
    x=root.winfo_rootx()
    y=root.winfo_rooty()
    width = root.winfo_width()
    height = root.winfo_height()

    screen = ImageGrab.grab(bbox=(x,y,x+width,y+height))
    screen.save("window_ss.png")
