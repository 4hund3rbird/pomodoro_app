from tkinter import *

from matplotlib.pyplot import text
#global constants--------------------------------------------------------
FONT=('arial',40,"italic")
WIN_HEIGHT=500
WIN_WIDTH=400
II=0
HOURS=20
MINUTES=30

hours=str(HOURS)
minutes=str(MINUTES)
sec=0
def timer(h,m):
    if m < 0:
            m=59
            h=h-1
    if h < 0 :
            pass
    if h>=0 :
            hours=f"{h}"
            minutes=f"{m}"
            if h < 10:
                hours="0"+hours
            if m < 10:
                minutes="0"+minutes

            canvas.itemconfig(time,text=f"{hours}:{minutes}")
            window.after(1000,timer,h,m-1)

#UI setup-----------------------------------------------------------------


window=Tk()
window.config(width=WIN_WIDTH,height=WIN_HEIGHT,bg="black",highlightthickness=0,padx=50,pady=50)
window.title("Pomodoro application")
window.geometry(f"{WIN_WIDTH}x{WIN_HEIGHT}")

canvas=Canvas(width=200,height=200,highlightthickness=0,bg="black")
time=canvas.create_text(100,100,text=f"{hours}:{minutes}",fill="white",font=FONT)
canvas.pack()
def start_timer():
    timer(int(hours),int(minutes))


start_button=Button(text="start",command=start_timer)
start_button.pack()

#timer mechanism---------------------------------------------------------

    
#break and work count mechanism------------------------------------------
#reset mechanism---------------------------------------------------------

window.mainloop()
