
from tkinter import *
from timeit import default_timer as timer
import random

window = Tk()

window.geometry("450x200")
window.title("Hoooooww fast can you type? how fast can you type?")
x = 0


def game():
    global x

    if x == 0:
        window.destroy()
        x = x + 1

    def check_result():
        if entry.get() == words[word]:
            end = timer()
            print(end-start)

        else:
            print("wrong input")

        words = ['programming', 'coding', 'algorithm','systems','python','software']

        word = random.randint(0, (len(words)-1))

        start = timer()
        windows = Tk()
        windows.geometry("200x200")

        x2 = Label(windows, text=words[word], font="times 20")
        x2.place(x=150, y=10)


        x3 = Label(windows, text="Start Typing", font="times 20")
        x3.place(x=10, y=50)

        entry = Entry(windows)
        entry.place(x=280, y=55)

        button2 = Button(windows, text="Done",
                        command=check_result, width=12,bg='grey')
        button2.place(x=150, y=100)

        button3 = Button(windows, text="Try again",
                         command=game, width=12, bg='grey')
        button3.place(x=250, y=100)
        window.mainloop()

variable_x = Label(window,text="Lets start playing..", font="times 20")
variable_x.place(x=10, y=50)

button1 =Button(window, text="Go", command=game, width=12, bg='grey')
button1.place(x=150,y=100)





window.mainloop()
