from tkinter import *
from PIL import ImageTk,Image
rootVariable=Tk()


rememberIndexGoing=1

def move_Back(indexValue):
     global image1Label
     
     
     image1Label.grid_forget()
     image1Label=Label(image=imageList[indexValue])
     button_Forward=Button(rootVariable,text=">>",command=lambda:move_Forward(indexValue+1))
   
     button_Back=Button(rootVariable,text="<<",command=lambda:move_Back(indexValue-1))
   
     if(indexValue==0):
         button_Back=Button(rootVariable,text="<<",command=move_Back,state=DISABLED)
     image1Label.grid(row=0,column=0,columnspan=3)
     button_Back.grid(row=1,column=0)
     button_Forward.grid(row=1,column=2)
def move_Forward(indexValue):
    global image1Label
 
    image1Label.grid_forget()
    image1Label=Label(image=imageList[indexValue])
    button_Forward=Button(rootVariable,text=">>",command=lambda:move_Forward(indexValue+1))
    button_Back=Button(rootVariable,text="<<",command=lambda:move_Back(indexValue-1))
    if(indexValue==7):
        button_Forward=Button(rootVariable,text=">>",state=DISABLED)

    image1Label.grid(row=0,column=0,columnspan=3)
    button_Back.grid(row=1,column=0)
    button_Forward.grid(row=1,column=2)


rootVariable.title('Gallery')
image1=ImageTk.PhotoImage(Image.open("./Image1.jpg"))                     # remember the Syntax
image2=ImageTk.PhotoImage(Image.open("./Image2.jpg"))
image3=ImageTk.PhotoImage(Image.open("./Image3.jpg"))
image4=ImageTk.PhotoImage(Image.open("./Image4.jpg"))
image5=ImageTk.PhotoImage(Image.open("./Image5.jpg"))
image6=ImageTk.PhotoImage(Image.open("./Image6.jpg"))
image7=ImageTk.PhotoImage(Image.open("./Image7.jpg"))
image8=ImageTk.PhotoImage(Image.open("./Image8.jpg"))
imageList=[image1,image2,image3,image4,image5,image6,image7,image8]
image1Label=Label(image=image1)
image1Label.grid(row=0,column=0,columnspan=3)



# Creating the Buttons
button_Back=Button(rootVariable,text="<<",command=move_Back,state=DISABLED)
button_Exit=Button(rootVariable,text="EXIT",command=rootVariable.quit)
button_Forward=Button(rootVariable,text=">>",command=lambda:move_Forward(1))
#  Setting grid of the Buttons
button_Back.grid(row=1,column=0)
button_Exit.grid(row=1,column=1)
button_Forward.grid(row=1,column=2)




rootVariable.mainloop()