import tkinter 
import pandas
import random
import time

BACKGROUND_COLOR = "#B1DDC6"

current_card = {}
to_learn = {}

#Loading data
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def new_word():

    global current_card,flip_timer
    window.after_cancel(flip_timer)

    current_card = random.choice(to_learn)

    canvas.itemconfig(fr_top_text,text="French",fill="black")
    canvas.itemconfig(fr_bottom_text,text=current_card['French'],fill="black")
    canvas.itemconfig(bg,image=front)

    flip_timer = window.after(3000,func=flip_card)

def flip_card():
    canvas.itemconfig(bg, image = back)
    canvas.itemconfig(fr_top_text,text="English",fill="white")
    canvas.itemconfig(fr_bottom_text,text=current_card['English'],fill="white")

def is_known():
    to_learn.remove(current_card)

    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)

    new_word()



#UI SETUP
window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000,func=flip_card)

image1 = tkinter.PhotoImage(file="images/wrong.png")
image2 = tkinter.PhotoImage(file="images/right.png")
front = tkinter.PhotoImage(file="images/card_front.png")
back = tkinter.PhotoImage(file="images/card_back.png")

canvas = tkinter.Canvas(width=800,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
bg = canvas.create_image(800/2,526/2,image=front)

fr_top_text = canvas.create_text(400,150,text="French",fill="black",font=("Ariel",30,"italic"))
fr_bottom_text = canvas.create_text(400,263,text="",fill="black",font=("Ariel",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)

#buttons
no_button = tkinter.Button(image=image1,highlightthickness=0,borderwidth=0,command=new_word)
yes_button = tkinter.Button(image=image2,highlightthickness=0,borderwidth=0,command=is_known)

no_button.grid(column=0,row=1)
yes_button.grid(column=1,row=1)

new_word()

window.mainloop()
