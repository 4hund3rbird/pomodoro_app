from tkinter import *




#UI setup-----------------------------------------------------------------

def create_circle(x, y, r, canvasName): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1)


window=Tk()
window.config(width=400,height=500,bg="black",highlightthickness=0,padx=50,pady=50)
window.title("Pomodoro application")

time=Label(text="00:01",font=('arial',20,"italic"),fg="white",bg="black")
# create_circle(200,250,10,circle_canvas)


#timer mechanism---------------------------------------------------------

#break and work count mechanism------------------------------------------
#reset mechanism---------------------------------------------------------

window.mainloop()
