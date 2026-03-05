# Libraries
import tkinter
import webbrowser

from tkinter.scrolledtext import ScrolledText

# Variables
title = "WMD Identifier"
font = "Arial"
padding = 10

# Window
window = tkinter.Tk()
window.title(title)
window.geometry("800x500")

# This function wipes the current screen, then it instatiates the next one
def ChangeScreens(screen):
    # Clear the window
    for widget in window.winfo_children():
        widget.destroy()

    screen()

# This function creates the Back Button and Next Button that can be found on most of the screens
def BackAndNext(prevScreen, nextScreen):
    # Prepare a frame for the buttons
    buttonFrame = tkinter.Frame(window)
    buttonFrame.pack(side=tkinter.BOTTOM, fill=tkinter.X)

    # Back Button
    def back():
        ChangeScreens(prevScreen)
    backButton = tkinter.Button(buttonFrame, text="Back", command=back, font=(font, 20), width=5)
    backButton.pack(side=tkinter.LEFT, padx=padding, pady=padding)

    # Next Question Button
    def next():
        ChangeScreens(nextScreen)
    nextButton = tkinter.Button(buttonFrame, text="Next", command=next, font=(font, 20), width=5)
    nextButton.pack(side=tkinter.RIGHT, padx=padding, pady=padding)

def StartScreen():
    # Title
    titleLabel = tkinter.Label(window, text=title, font=(font, 60))
    titleLabel.pack(pady=padding)

    # Start Button
    def start():
        ChangeScreens(MultipleChoice)
    startButton = tkinter.Button(
        window,
        text="Start",
        command=start,
        font=(font, 40), # The font size affects the width and height of the button
        width=7) # Width overrides the font size's set width
    startButton.pack(pady=padding)

    # Learn More button
    def learnMore():
        ChangeScreens(LearnMoreScreen)
    lmButton = tkinter.Button(
        window,
        text="Learn More",
        command=learnMore,
        font=(font, 40),
        width=10)
    lmButton.pack(pady=padding)

""" I've tried to make this function act as sort of a base for other screen functions, but I just
can't figure it out. I think it would be easier if I was able to use Python classes, but I don't
know. """
""" Showcases a screen that displays a multiple choice question where the user can pick multiple
answers """
def MultipleChoice():
    BackAndNext(StartScreen, MultipleChoice2)

    # Question
    question = tkinter.Label(window, text="Pick your answers", font=(font, 30))
    question.pack(pady=padding)

    # Options
    options = []
    for i in range(4):
        options.append(tkinter.Checkbutton(
            window,
            text="Option #"+str(i + 1),
            var=tkinter.BooleanVar(),
            font=(font, 20)))
        options[i].pack(pady=padding)

""" Showcases a screen that displays a multiple choice question where the user can only pick one
answer (I need to think of a better name for this function, MultipleChoice2 is a placeholder) """
def MultipleChoice2():
    BackAndNext(MultipleChoice, StartScreen)

    # Question
    question = tkinter.Label(window, text="Pick an answer", font=(font, 30))
    question.pack(pady=padding)

    # Options
    options = []
    state = tkinter.IntVar(value=1)
    for i in range(4):
        options.append(tkinter.Radiobutton(
            window,
            text="Option "+str(i+1),
            variable=state,
            value=i,
            font=(font, 20)))
        options[i].pack(pady=padding)

def LearnMoreScreen():
    # Scrolling Text Box
    textBox = ScrolledText(window, width=50, height=10, wrap=tkinter.WORD)
    textBox.pack(padx=padding, fill=tkinter.BOTH, expand=True)
    with open("LearnMore.txt", "r") as file:
        content = file.read()
    textBox.insert(tkinter.END, content)
    textBox.config(state="disabled")

    # Hyperlink for more resources
    def openLink(event):
        webbrowser.open("https://ia800603.us.archive.org/12/items/fflch-livro-weapons-of-math-destruction-cathy-240826-220339/(FFLCH)%20LIVRO%20Weapons%20of%20Math%20Destruction%20-%20Cathy%20_240826_220339.pdf")
    link = tkinter.Label(window, text="Learn even more!", fg="blue", cursor="hand2")
    link.pack(pady=padding)
    link.bind("<Button-1>", openLink)

    # Back Button
    buttonFrame = tkinter.Frame(window)
    buttonFrame.pack(side=tkinter.BOTTOM, fill=tkinter.X)
    def back():
        ChangeScreens(StartScreen)
    backButton = tkinter.Button(buttonFrame, text="Back", command=back, font=(font, 20), width=5)
    backButton.pack(side=tkinter.LEFT, padx=padding, pady=padding)

# Start Program
StartScreen()
window.mainloop()