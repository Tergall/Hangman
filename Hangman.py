from tkinter import *
import random
import os, sys

window = Tk()
window.title("HANGMAN")
window.configure(width = (int(window.winfo_screenwidth())), height = (int(window.winfo_screenheight()))) # set window width and height

bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))

textfile = open(os.path.join(bundle_dir, "hangman_wordlist.txt"), "r")                                # pre-game, setting the variables
all_words = tuple(textfile.readlines())
textfile.close()

#main font variable
font = 'calibri'

#colour values variables
main_background = '#9AB8BA'
font_default = '#E4F4F4'
font_pressed = '#9AB8BA'
background_pressed = '#13282B'
background_default = '#055256'
font_label = '#0C3D59'



gaming = True
difficulty = 1
used = ""
initial_health = 1
parts = []

def pregame():
    wordlist = []
    global initial_health, health, chosen_word, used_letters, difficulty, used, parts, gaming
    if difficulty == 1:                                                         # easy
        initial_health = 11
        for word in all_words:
            if len(word.rstrip("\n")) >= 9:
                wordlist.append(word.rstrip("\n"))
    elif difficulty == 2:                                                       # medium
        initial_health = 8
        for word in all_words:
            if len(word.rstrip("\n")) >= 6 and len(word.rstrip("\n")) <= 9:
                wordlist.append(word.rstrip("\n"))
    elif difficulty == 3:                                                       # hard
        initial_health = 6
        for word in all_words:
            if len(word.rstrip("\n")) == 4 or len(word.rstrip("\n")) == 5:
                wordlist.append(word.rstrip("\n"))            
    health = initial_health
    chosen_word = random.choice(wordlist)
    label_puzzle["text"] = f'{len(chosen_word) * "_ "} [{len(chosen_word)}]'
    label_used["text"] = "Used letters: \n[ ]"
    label_feedback["text"] = ""
    used_letters = []
    parts = [False] * 11
    gaming = True
    canvas.delete('all')
    

def changeframe(from_f, to_f):
    from_f.pack_forget()
    to_f.pack()


def change_difficulty():
    global difficulty
    if difficulty == 1:
        difficulty += 1
        button_difficulty['text'] = 'NORMAL'
        label_info.config(text = 'HEALTH: 8\nWORDS: MEDIUM ')   
    elif difficulty == 2:
        difficulty += 1
        button_difficulty['text'] = 'HARD'
        label_info.config(text = 'HEALTH: 6\nWORDS: SHORT ')
    else:
        difficulty = 1
        button_difficulty['text'] = 'EASY'
        label_info.config(text = 'HEALTH: 11\nWORDS: LONG ')
	

def winning_moment():
    label_feedback["text"] = "You won!"
    global gaming
    gaming = False


def losing_moment():
    label_feedback["text"] = f"You lost! The correct word was: {chosen_word}"
    global gaming
    gaming = False


def key_pressed(event):
    if gaming == False:
        return
    global health
    if not event.char.isalpha():
        label_feedback["text"] = "Invalid character"
        return
    if event.char in chosen_word:
        used_letters.append(event.char)
        label_feedback["text"] = "Correct!"
    else:
        used_letters.append(event.char)
        health -= 1
        label_feedback["text"] = "Wrong"
        draw_part(20, 20, health)

    
    puzzle = ""
    for letter in chosen_word:
        if letter in used_letters:
            puzzle += letter
        else:
            puzzle += "_ "
    label_puzzle["text"] = f"{puzzle}  ({len(chosen_word)})"

    used = []
    for letter in used_letters:
        if letter not in used:
            used.append(letter)
    label_used["text"] = "Used letters: \n[" + ", ".join(sorted(used)) + "]"
    
    if "_" not in puzzle:                                             
        winning_moment()
    if health <= 0:
        losing_moment()

def draw_part(x1, y1, health):
    size = canvas.winfo_width() * 0.9
    l_width = size / 30
    x2 = x1 + size
    y2 = y1 + size
    dim1 = size / 3
    dim2 = dim1 / 2
    dim3 = dim2 / 2
    dim4 = dim3 / 2
    global parts
    part = round(((initial_health - health) / initial_health) * len(parts))
    if part >= 1 and parts[0] == False:
        canvas.create_line(x1, y2, x1 + dim1, y2, width = l_width, capstyle = ROUND, fill = font_label)
        parts[0] = True
    if part >= 2 and parts[1] == False:
        canvas.create_line(x1  + dim2, y2, x1 + dim2, y1, width = l_width, capstyle = ROUND, fill = font_label)
        parts[1] = True
    if part >= 3 and parts[2] == False:
        canvas.create_line(x1  + dim2, y1, x2 - dim2, y1, width = l_width, capstyle = ROUND, fill = font_label)
        parts[2] = True
    if part >= 4 and parts[3] == False:
        canvas.create_line(x1  + dim2, y1 + dim2, x1 + dim1, y1, width = l_width, capstyle = ROUND, fill = font_label)
        parts[3] = True
    if part >= 5 and parts[4] == False:
        canvas.create_line(x2 - (dim2 + dim3), y1, x2 - (dim2 + dim3), y1 + dim2 + dim3, width = l_width, capstyle = ROUND, fill = font_label)
        parts[4] = True
    if part >= 6 and parts[5] == False:
        canvas.create_oval(x2 - (dim1), y1 + dim2 + dim3, x2 - (dim2), y1 + (dim1 + dim3), width = l_width, fill = font_label, outline = font_label)
        parts[5] = True
    if part >= 7 and parts[6] == False:
        canvas.create_line(x2 - (dim2 + dim3), y1 + (dim1 + dim3), x2 - (dim2 + dim3), y1 + (2 * dim1), width = l_width, capstyle = ROUND, fill = font_label)
        parts[6] = True
    if part >= 8 and parts[7] == False:
        canvas.create_line(x2 - (dim2 + dim3), y1 + (dim1 + dim3), x2 - dim1, y1 + (dim1 + dim2 + dim4), width = l_width, capstyle = ROUND, fill = font_label)
        parts[7] = True
    if part >= 9 and parts[8] == False:
        canvas.create_line(x2 - (dim2 + dim3), y1 + (dim1 + dim3), x2 - dim2, y1 + (dim1 + dim2 + dim4), width = l_width, capstyle = ROUND, fill = font_label)
        parts[8] = True
    if part >= 10 and parts[9] == False:
        canvas.create_line(x2 - (dim2 + dim3), y1 + (2 * dim1), x2 - dim1, y1 + (2 * dim1 + dim3+ dim4), width = l_width, capstyle = ROUND, fill = font_label)
        parts[9] = True
    if part >= 11 and parts[10] == False:
        canvas.create_line(x2 - (dim2 + dim3), y1 + (2 * dim1), x2 - dim2, y1 + (2 * dim1 + dim3+ dim4), width = l_width, capstyle = ROUND, fill = font_label)
        parts[10] = True

window.bind("<Key>", key_pressed)

def info(e):
    if difficulty == 1:
        label_info.config(text = 'HEALTH: 11\nWORDS: LONG ')
    elif difficulty == 2:
        label_info.config(text = 'HEALTH: 8\nWORDS: MEDIUM ')
    else:
        label_info.config(text = 'HEALTH: 6\nWORDS: SHORT ')



def close(e):
    
    label_info.config(text = '\n')



#main window
frame_menu = Frame(window, width = (int(window.winfo_screenwidth())), height = (int(window.winfo_screenheight())), bg = main_background)
frame_game = Frame(window, width = (int(window.winfo_screenwidth())), height = (int(window.winfo_screenheight())), bg = main_background)
frame_settings = Frame(window, width = (int(window.winfo_screenwidth())), height = (int(window.winfo_screenheight())), bg = main_background)

#menu
frame_menu.pack(side = TOP)
frame_menu.pack_propagate(False)
frame1 = Frame(frame_menu, bg = main_background)
frame1.pack(expand = True)

#game
frame_game.pack_propagate(False)
frame3 = Frame(frame_game, bg = main_background)
frame3.pack(expand = True)

#settings
frame_settings.pack_propagate(False)
frame2 = Frame(frame_settings, bg = main_background)
frame2.pack(expand = True)


button_play = Button(frame1, text = 'PLAY', width = 25, height = 2, fg = font_default, bg = background_default, highlightcolor = 'white', activebackground = background_pressed, activeforeground = font_pressed, font=(font, 20), command = lambda : [changeframe(frame_menu, frame_game), pregame()])
button_play.pack()

button_settings = Button(frame1, text = 'SETTINGS', width = 25, height = 2, fg = font_default, bg = background_default, activeforeground = font_pressed, activebackground = background_pressed, font=(font, 20), command = lambda : changeframe(frame_menu, frame_settings) )
button_settings.pack(pady=15)
button_exit = Button(frame1, text='EXIT', width = 25, height = 2, bg = background_default, fg = font_default, activeforeground = font_pressed, activebackground = background_pressed, font = (font, 20), command = window.destroy)
button_exit.pack()


button_back = Button(frame_game, text = 'BACK',width = 25, height = 2, fg = font_default, activeforeground = font_pressed, activebackground = background_pressed, bg = background_default,font=(font, 20) ,command = lambda : changeframe(frame_game, frame_menu) )
button_back.place(x=5, y = 5)
label_puzzle = Label(frame_game, text = "", bg = main_background, font=(font, 35), fg = font_label)
label_puzzle.place(relx = 0.312, y = 200)
label_used = Label(frame_game, text = "", bg = main_background, font = (font, 35), wraplength = 500, justify = LEFT, fg = font_label)
label_used.place(relx = 0.677, y = 200)
label_feedback = Label(frame_game, text = "", bg = main_background, font = (font, 35), fg = font_label)
label_feedback.place(relx = 0.5, y = 100, anchor = CENTER)
canvas = Canvas(frame_game, width = 500, height = 500, bg = main_background, borderwidth = 0, highlightthickness = 0)
canvas.place(relx = 0.5, rely = 0.65, anchor = CENTER)

label_difficulty = Label(frame2, text = 'CHOOSE YOUR DIFFICULTY', bg = main_background, fg = font_label, font = (font, 30))
button_Back = Button(frame2, text = 'BACK', width = 25, height = 2, bg = background_default, activeforeground = font_pressed, activebackground = background_pressed, fg = font_default, font=(font, 20), command = lambda : changeframe(frame_settings, frame_menu) )
button_difficulty = Button(frame2, text = 'EASY', width = 25, height = 2, bg = background_default, activeforeground = font_pressed, activebackground = background_pressed, fg = font_default, font=(font, 20), command = lambda : change_difficulty())
label_info = Label(frame2, text = '\n', bg = main_background, font=(font, 20), fg = font_label )
label_difficulty.pack()
label_info.pack(pady = 5)
button_difficulty.pack(pady = 15)
button_Back.pack(pady = 15)

button_difficulty.bind('<Enter>', info)
button_difficulty.bind('<Leave>', close)

window.mainloop()
