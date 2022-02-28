from tkinter import *
#global constants--------------------------------------------------------
FONT=('arial',20,"italic")
WIN_HEIGHT=500
WIN_WIDTH=400


#UI setup-----------------------------------------------------------------

def create_circle(x, y, r, canvasName): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1)


window=Tk()
window.config(width=WIN_WIDTH,height=WIN_HEIGHT,bg="black",highlightthickness=0)
window.title("Pomodoro application")
window.geometry(f"{WIN_WIDTH}x{WIN_HEIGHT}")





#timer mechanism---------------------------------------------------------
def timer():
    time=Label(text="00:01",font=FONT,fg="white",bg="black",highlightthickness=0)
    time.pack()
#break and work count mechanism------------------------------------------
#reset mechanism---------------------------------------------------------

window.mainloop()
