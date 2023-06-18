#Created virtual environment and installed program within venv so it doesnt clash with other programs in the global enviroment 
#Import all tkinter functions 

from tkinter import *
# Global variable 
# assign the mathematical expression from user to a variable, currently an empty string 
num_operator = " "

#Defining userclick function for when user clicks on screen 
def userclick(num):
    global num_operator
    # Accounts for user mathetical expression - turns input into a string, concatenates string
    num_operator=num_operator+str(num)
    #eg num_operator = " " + "2" = " 2 ", - user clicks on number 2 
    # update the expression
    iptext.set(num_operator)

# Evaluate the users expression
def evaluate():
    global num_operator
    #eval() - evaluates the expression 
    output=str(eval(num_operator))
    iptext.set(output)

# Clears the display 
def clearDisplay():
    global num_operator
    #returns the expression back to empty, and updates the display
    num_operator=" "
    iptext.set(num_operator)


#Creating the GUI, creating the GUI Window
calc=Tk()
calc.title("Mac's Calculator")

# Adding the buttons to the GUI, describing font,size,command when button is clicked, text to display 
iptext=StringVar()
iparea=Entry(calc,font=('large,_font',15,'bold'),bd=10,justify="right",insertwidth=4,textvariable=iptext).grid(columnspan=10)

num1=Button(calc,font=('arial',15,'bold'),command=lambda:userclick(1),bg="lavender",text="1",bd=5,padx=15,pady=10).grid(row=1,column=0)

num2=Button(calc,font=('arial',15,'bold'),command=lambda:userclick(2),bg="lavender",text="2",bd=5,padx=15,pady=10).grid(row=1,column=1)

num3=Button(calc,font=('arial',15,'bold'),command=lambda:userclick(3),bg="lavender",text="3",bd=5,padx=15,pady=10).grid(row=1,column=2)

addition=Button(calc,font=('arial',15,'bold'),command=lambda:userclick('+'),bg="lavender",text="+",bd=5,padx=15,pady=10).grid(row=1,column=3)

num4=Button(calc,font=('arial',15,'bold'),command=lambda:userclick(4),bg="lavender",text="4",bd=5,padx=15,pady=10).grid(row=2,column=0)

num5=Button(calc,font=('arial',15,'bold'),command=lambda:userclick(5),bg="lavender",text="5",bd=5,padx=15,pady=10).grid(row=2,column=1)

num6=Button(calc,font=('arial',15,'bold'),command=lambda:userclick(6),bg="lavender",text="6",bd=5,padx=15,pady=10).grid(row=2,column=2)

subtract=Button(calc,font=('arial',15,'bold'),command=lambda:userclick('-'),bg="lavender",text="-",bd=5,padx=15,pady=10).grid(row=2,column=3)

num7=Button(calc,font=('arial',15,'bold'),command=lambda:userclick(7),bg="lavender",text="7",bd=5,padx=15,pady=10).grid(row=3,column=0)

num8=Button(calc,font=('arial',15,'bold'),command=lambda:userclick(8),bg="lavender",text="8",bd=5,padx=15,pady=10).grid(row=3,column=1)

num9=Button(calc,font=('arial',15,'bold'),command=lambda:userclick(9),bg="lavender",text="9",bd=5,padx=15,pady=10).grid(row=3,column=2)

multiply=Button(calc,font=('arial',15,'bold'),command=lambda:userclick('*'),bg="lavender",text="*",bd=5,padx=15,pady=10).grid(row=3,column=3)

num0=Button(calc,font=('arial',15,'bold'),command=lambda:userclick(0),bg="lavender",text="0",bd=5,padx=15,pady=10).grid(row=4,column=0)

Cancel=Button(calc,font=('arial',15,'bold'),command=clearDisplay,bg="lavender",text="C",bd=5,padx=15,pady=10).grid(row=4,column=1)

equal=Button(calc,font=('arial',15,'bold'),command=evaluate,bg="lavender",text="=",bd=5,padx=15,pady=10).grid(row=4,column=2)

division=Button(calc,font=('arial',15,'bold'),command=lambda:userclick('/'),bg="lavender",text="/",bd=5,padx=15,pady=10).grid(row=4,column=3)

calc.mainloop(),