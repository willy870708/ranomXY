from tkinter import*
import random
import pyperclip

win = Tk()
win.title("Random x,y generator")
win.geometry("400x250+600+300")
win.config(bg="#323232")

text_title = Label(text="Random x,y Generator",bg="skyblue",fg="#323232")
text_title.config(font = "Arial 15")
text_title.pack()

min_range = Label(text = "minimal range",bg="#323232",fg="white",font = "標楷體 12")
min_range.pack()

min_entry = Entry()
min_entry.pack()

max_range = Label(text = "maximal range",bg="#323232",fg="white",font = "標楷體 12")
max_range.pack()

max_entry = Entry()
max_entry.pack()

x_show = Label(text = "",bg="#323232")
x_show.pack()

y_show = Label(text = "",bg="#323232")
y_show.pack()

def gen_xy():
    minvalue = int(min_entry.get())
    maxvalue = int(max_entry.get())
    x = str(random.randint(minvalue,maxvalue))
    y = str(random.randint(minvalue,maxvalue))
    x_show.config(text = "x: "+x,fg = "white",font = "Arial 12")
    y_show.config(text = "y: "+y,fg = "white",font = "Arial 12")

def copy():
    xy = x_show.cget("text")+"\n"+y_show.cget("text")
    pyperclip.copy(xy)

generator = Button(text = "Generator",font = "微軟正黑體 12",command = gen_xy)
generator.pack()

copy = Button(text = "Copy",font = "微軟正黑體 12",command = copy)
copy.pack()

win.mainloop()