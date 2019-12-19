#2019-20 Fall Computer Science Principles Final Exam

#Ms. Haubold

#Layla Nettavong
#3rd hour
#12/19/19
#Computer Science


#### INSTRUCTIONS ####
#Create an etch a sketch turtle game GOOD
#The turtle should move with the arrow keys (up, down, left and right), and draw DONE
#Space should clear the screen DONE
#o and p should make the pen size bigger and smaller DONE
#u should pick the pen up or put the pen down NOT DOING
#All code must be commented GOOD
#BONUS
#Add a feature to change colors DONE
#

#import required libraries
import turtle as trtl 
wn = trtl.Screen()

#create turtle
drawer = trtl.Turtle()
#for color functions
color1 = 1
color2 = 2
current_size = 1
size = 0
#for start
drawer.pencolor("blue")

#movement functions
def up():
    drawer.setheading(90)
    drawer.forward(10)
  
def down():
    drawer.setheading(270)
    drawer.forward(10)
  
def right():
    drawer.setheading(0)
    drawer.forward(10)
  
def left():
    drawer.setheading(180)
    drawer.forward(10)

#color/drawing functions
def space():
    drawer.clear()

def pensize_up():
    global size
    global current_size
    new_size = current_size + size
    if (current_size <= 1 ):
        wn.onkeypress (pensize_up,"o")
        drawer.pensize(new_size)
        size += 1
        
def pensize_down():
    global size
    new_size  =current_size + size
    another_size = new_size - current_size
    if (new_size >= 1):
        wn.onkeypress(pensize_down,"p")
        drawer.pensize(another_size)
        size -= 1
             
def drawer_color1():
    global color1
    if (color1 <= 1):
        wn.onkeypress(drawer_color1,"b")
        drawer.pencolor("blue")

def drawer_color2():
    global color2
    if (color2 <= 2):
        wn.onkeypress(drawer_color2,"r")
        drawer.pencolor("red")

#create screen
wn.bgcolor("black")

#bind to keypresses
wn.onkeypress(up,"Up")
wn.onkeypress(down,"Down")
wn.onkeypress(right,"Right")
wn.onkeypress(left,"Left")
wn.onkeypress(space,"space")
wn.onkeypress(pensize_up,"o")
wn.onkeypress(pensize_down,"p")
wn.onkeypress(drawer_color1,"b")
wn.onkeypress(drawer_color2,"r")

#listen
wn.listen()

#mainloop
wn.mainloop()