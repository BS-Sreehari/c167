from tkinter import*
from PIL import ImageTk, Image


root = Tk()


root.title("Canvas drawing with functions")
root.geometry("600x600")


colour = Label(root, text = "Colour: ")
colour.place(relx = 0.6, rely = 0.9, anchor = CENTER)

color_input = Entry(root)
color_input.place(relx = 0.8, rely = 0.9, anchor = CENTER)
color_input.insert(0, "black")

canvas = Canvas(root, height = 510, width = 590, bg = "white", highlightbackground = "gray")
canvas.pack()

img = ImageTk, PhotoImage(Image.open("start_point1.png"))
my_image = canvas.create_image(50, 50, image = img)

direction = ""

oldx = 50
oldy = 50
newx = 50
newy = 50

def draw(direction, oldx, oldy, newx, newy):
    input_fill_color = color_input.get()
    if(direction == "right"):
        right_line = canvas.create_line(oldx, oldy, newx, newy, width = 3, fill = input_fill_color)
    if(direction == "left"):
      left_line = canvas.create_line(oldx, oldy, newx, newy, width = 3, fill = input_fill_color)
    if(direction == "up"):
        up_line = canvas.create_line(oldx, oldy, newx, newy, width = 3, fill = input_fill_color)
    if(direction == "down"):
       down_line = canvas.create_line(oldx, oldy, newx, newy, width = 3, fill = input_fill_color)
        
    
root.bind("<Right>", right_dir)
root.bind("<Left>", left_dir)
root.bind("<Up>", up_dir)
root.bind("<down>", down_dir)

def right_dir() :
    global oldx
    global oldy
    global newy
    global newx
    oldx = newx
    oldy = newy
    newx = newx + 5
    direction = "right"
    draw(direction, oldx, oldy, newx, newy)
    
    
def left_dir() :
    global oldx
    global oldy
    global newx
    global newy
    oldx = newx
    newx = newx - 5
    direction = "left"
    draw(direction, oldx, oldy , newx, newy)
    
    
def up_dir() :
    global oldx
    global oldy
    global newx
    global newy
    newy = newy - 5
    direction = "up"
    draw(direction, oldx, oldy, newx, newy)
    
    
def down_dir() :
    global oldx
    global oldy
    global newx
    global newy
    newy = newy + 5
    direction = "down"
    draw(direction, oldx, oldy, newx, newy)

root.mainloop()
