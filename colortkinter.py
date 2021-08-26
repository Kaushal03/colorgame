from tkinter import *
import time
import os
import random
from tkinter import messagebox as mb

rt=Tk()
rt.geometry("1600x800+0+0")
rt.configure(bg="light green")
########################################################################################################################
rt.title("COLOR GUESSING GAME")
colours = ['red','Blue','Green','Pink','black', 
		'Yellow','Orange','White','Purple','Brown'] 
score = 0

# the game time left, initially 30 seconds. 
timeleft = 30

# function that will start the game. 
def startGame(event): 
	
	if timeleft == 30: 
		
		# start the countdown timer. 
		countdown() 
		
	# run the function to 
	# choose the next colour. 
	nextColour() 

# Function to choose and 
# display the next colour. 
def nextColour(): 

	# use the globally decladark green 'score' 
	# and 'play' variables above. 
	global score 
	global timeleft 

	# if a game is currently in play 
	if timeleft > 0: 

		# make the text entry box active. 
		e.focus_set() 

		# if the colour typed is equal 
		# to the colour of the text 
		if e.get().lower() == colours[1].lower(): 
			
			score += 1

		# clear the text entry box. 
		e.delete(0,END) 
		
		random.shuffle(colours) 
		
		# change the colour to type, by changing the 
		# text _and_ the colour to a random colour value 
		label.config(fg = str(colours[1]), text = str(colours[0])) 
		
		# update the score. 
		scoreLabel.config(text = "Score: " + str(score)) 


# Countdown timer function 
def countdown(): 

	global timeleft 

	# if a game is in play 
	if timeleft > 0: 

		# decrement the timer. 
		timeleft -= 1
		
		# update the time left label 
		timeLabel.config(text = "Time left: "
							+ str(timeleft)) 
								
		# run the function again after 1 second. 
		timeLabel.after(1000, countdown) 

########################################################################################################################
Tops=Frame(rt,width = 1600,height = 50,bg="light green",relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(rt,width = 550,height = 700,bg="light green",relief=SUNKEN)
f1.pack(side=LEFT)

f2=Frame(rt,width = 300,height = 700,bg="light green",relief=SUNKEN)
f2.pack(side=RIGHT)
########################################################################################################################
lblInfo=Label(Tops,font=("arial",30,"bold"),text="WELCOME TO THE COLOR GUESSING GAME ",bg="light green",fg="dark green",bd=10,anchor="w")
lblInfo.pack()

localtime=time.asctime(time.localtime(time.time()))#DATE TIME FUNCTION

lblDateTime=Label(Tops,font=("arial",20,"bold"),text=localtime,fg="dark green",bg="light green",bd=10,anchor="w")
lblDateTime.pack()

lblInfo=Label(Tops,font=("arial",23,"bold"),text="",bg="light green",fg="dark green",bd=10,anchor="w")
lblInfo.pack()

lblInfo=Label(Tops,font=("arial",23,"bold"),text="PRESS START BUTTON TO START THE GAME ",bg="light green",fg="dark green",bd=10,anchor="w")
lblInfo.pack()
#########################################################################################################################
def start():
    global root
    global e
    global timeLabel
    global label
    global scoreLabel
    root=Toplevel(rt)
    root.title("COLOR GUESSING GAME")
    root.configure(bg="light green")
    
    instructions = Label(root,font = ('arial', 12,'bold'), text = "Type in the colour"
						"of the words, and not the word text!",bg="light green",fg='dark green') 
    instructions.pack() 

    # add a score label 
    scoreLabel = Label(root, text = "Press enter to start", font = ('arial', 12,'bold'),bg="light green",fg='dark green') 
    scoreLabel.pack() 

    # add a time left label 
    timeLabel = Label(root, text = "Time left: " +str(timeleft), font = ('arial', 12,'bold'),bg="light green",fg='dark green') 
                                
    timeLabel.pack() 

    # add a label for displaying the colours 
    label = Label(root, font = ('arial', 60),bg="light green",fg='dark green') 
    label.pack() 

    # add a text entry box for 
    # typing in colours 
    e = Entry(root, font=('arial',40,'bold'),bg="light green",fg='dark green') 

    # run the 'startGame' function 
    # when the enter key is pressed 
    root.bind('<Return>', startGame) 
    e.pack() 

    # set focus on the entry box 
    e.focus_set() 

    # start the GUI 
    root.mainloop()
lblInfo=Label(rt,font=("arial",23,"bold"),text="",bg="light green",fg="dark green",bd=10,anchor="w")
lblInfo.pack()

btn15=Button(rt,padx=16,pady=16,bd=8,fg="dark green",font=("arial",18,"bold"),text="START",bg="light green",
                    command=start,anchor="w",width=10,height=0,compound="c")
btn15.place(x=220,y=420)

def call(): 
	res = mb.askquestion('Exit Application', 'Do you really want to exit') 
	
	if res == 'yes' : 
		rt.destroy() 
		
	else : 
		mb.showinfo('Return', 'Returning to main application') 



btn16=Button(rt,padx=16,pady=16,bd=8,fg="dark green",font=("arial",18,"bold"),text="Quit",bg="light green",
                    command=call,anchor="w",width=10,height=0,compound="c")
btn16.place(x=620,y=420)

rt.mainloop()
  
    
