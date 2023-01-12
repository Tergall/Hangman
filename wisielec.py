from tkinter import *

window = Tk() # declare the window
window.title("HANGMAN") # set window title
window.configure(width = (int(window.winfo_screenwidth())), height= (int(window.winfo_screenheight()))) # set window width and height
window.configure(bg='grey') # set window background color

def changeframe(from_f, to_f):
    from_f.pack_forget()
    to_f.pack()

def changedifficulty(button):
    if button['text'] == 'EASY':
        button['text'] = 'NORMAL'
    elif button['text'] == 'NORMAL':
        button['text'] = 'HARD'
    else:
        button['text'] = 'EASY'
	


#okienko główne
frame_main = Frame(window, width = (int(window.winfo_screenwidth())), height= (int(window.winfo_screenheight())), bg='pink')
frame_main.pack(side=TOP)
frame_main.pack_propagate(False)
frame1 = Frame(frame_main, bg = 'pink')
frame1.pack(expand = True)

#okienko gry
frame_game = Frame(window, width = (int(window.winfo_screenwidth())), height= (int(window.winfo_screenheight())))
frame_game.pack(side=TOP)
frame_game.pack_propagate(False)
frame3 = Frame(frame_game, bg = 'pink')
frame3.pack(expand = True)

#okienko z ustawieniami
frame_settings = Frame(window, width = (int(window.winfo_screenwidth())), height= (int(window.winfo_screenheight())))
frame_settings.pack(side=TOP)
frame_settings.pack_propagate(False)
frame2 = Frame(frame_settings, bg = 'pink')
frame2.pack(expand = True)




button_play = Button(frame1, text = 'PLAY',width = 25, height = 2, fg = 'black', bg = 'purple', command = lambda : changeframe(frame_main, frame_game))
button_play.pack()

button_settings = Button(frame1, text = 'SETTINGS',width = 25, height = 2, bg = 'purple', command = lambda : changeframe(frame_main, frame_settings) )
button_settings.pack(pady=15)

button_back = Button(frame3, text = 'BACK',width = 25, height = 2, bg = 'purple', command = lambda : changeframe(frame_game, frame_main) )
button_back.pack()

label_difficulty = Label(frame2, text= 'CHOOSE YOUR DIFFICULTY')
button_Back = Button(frame2, text = 'RETURN',width = 25, height = 2, bg = 'purple', command = lambda : changeframe(frame_settings, frame_main) )
button_easy = Button(frame2, text = 'EASY',width = 25, height = 2, bg = 'purple', command = lambda : changedifficulty(button_easy))
label_difficulty.pack()
button_easy.pack()
button_Back.pack()



window.mainloop()