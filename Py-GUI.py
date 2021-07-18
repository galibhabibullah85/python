from tkinter import *
root = Tk()
root.title("First py software")

#widthxHeight
root.geometry("1200x500")
root.minsize(600,400)
root.maxsize(1250,550)

#showing text
text = Label(
  text="Hello there",
  bd='black',#background color
  #background='black', same as bd
  fg='white',#fore-ground color
  #foreground='white' same as fg
  padx=10, #padding in x-axis
  pady=10, #padding in y-axis
  #font=("sarif",30,"bold"), same as the down one
  font="sarif 30 bold",#"font-family font-size text-style"
  borderwidth=3,
  relief=SUNKEN, #border-styling
  )
text.pack(#printing the label in aoftware-interface
  anchor='nw', #label position[nw(north-west),ne,se,sw]
  side=BOTTOM,#label positioning[RIGHT,LEFT,TOP,BOTTOM]
  fill='x',#width=100%
  fill=Y,#height=100%
  padx=20,pady=20,
  )
  
#------playing with frames
frame1 = Frame(root,bd='tomato',borderwidth=2,relief=SUNKEN)
frame1.pack(side=LEFT,fill='y')
frame1_label = Label(frame1,text="I am inside f1")
frame1_label.pack()

frame2 = Frame(root)#div tags
frame2.pack(fill='y')
frame2_label = Label(frame2,text="I am inside frame2")
frame2_label.pack()
#------playing with frames

#showing png image
photo = PhotoImage(file="img.png")
img = Label(image=photo)
img.pack()

#showing jpg images
from PIL import Image,ImageTk #pip install pillow
jpg = Image.open("img.jpg")
photo = ImageTk.PhotoImage(file=jpg)
img = Label(image=photo)
img.pack()

#playing with buttons
def alert():
  print('Warning')
b1 = Button(text="Save",command=alert)
b1.pack()

#grid packing
a = Label(root,text="user")
b = Label(root,text="pass")
a.grid(row=0,column=1)
b.grid(row=1,column=1)

#playing with user input
name = StringVar()
usr_input = Entry(root,textveriable=name)
usr_input.grid()
def showval():
  print(name.get())
Button(root,text="Check",command=showval).grid()


root.mainloop()