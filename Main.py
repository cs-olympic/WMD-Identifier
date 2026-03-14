# Tkinter
import tkinter
from tkinter.scrolledtext import ScrolledText

# Other Libraries and Modules
import webbrowser

# Variables
title = "WMD Identifier"
font = "Arial"
padding = 10
scores = { # This scores variable will be edited with every question
    "Opaqueness" : 0, # How opaque the algorithim is
    "Discrimitive" : 0} # How discrimitive the algorithim is

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
def BackAndNext(
        prevScreen, # The previous screen
        nextScreen, # The next screen
        questionType=None, # The type of question
        options=None, # The option button that are apart of the screen
        changing=None): # The score that is being changed
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
        # Change the dictionary of scores based on which options are selected on the current screen
        if questionType != None:
            questionType(options, changing)

        # Debugging
        print(scores)

        ChangeScreens(nextScreen)
    nextButton = tkinter.Button(buttonFrame, text="Next", command=next, font=(font, 20), width=5)
    nextButton.pack(side=tkinter.RIGHT, padx=padding, pady=padding)

# The logic that happens when the user has left a screen with a Multi Select Question
def MultiSelectLogic(
        options, # The list of options that are going to have their state checked
        changing): # The score that is getting changed
    for option in options:
        if option.var.get():
            # Debugging
            print("The box is checked")

            scores[changing] += 1

def StartScreen():
    # Title
    titleLabel = tkinter.Label(window, text=title, font=(font, 60))
    titleLabel.pack(pady=padding)

    # Start Button
    def start():
        ChangeScreens(Question1)
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

""" This question asks the user how much they think they know about how their data is being used,
this question sees how opaque the algorithim is. """
def Question1():
    # Question
    question = tkinter.Label(
        window,
        text="How much do you think you know\nabout how your data is being used?",
        font=(font, 30))
    question.pack(pady=padding)

    # Options
    options = []
    optionsText = ["Everything", "Some Things", "Very Little", "Nothing"]
    state = tkinter.IntVar(value=1)
    for i in range(len(optionsText)):
        options.append(tkinter.Radiobutton(
            window,
            text=optionsText[i],
            variable=state,
            value=i,
            font=(font, 20)))
        options[i].pack(pady=padding)
    
    BackAndNext(StartScreen, Question2)

""" This question asks the user if the insurence company has informed them about how their model
works, this question also determines opaqueness. """
def Question2():
    # Question
    question = tkinter.Label(
        window,
        text="Has the insurance company told\nyou how their model works?",
        font=(font, 30))
    question.pack(pady=padding)

    # Options
    options = []
    optionsText = ["Yes", "Yes, but I think they lied", "No"]
    state = tkinter.IntVar(value=1)
    for i in range(len(optionsText)):
        options.append(tkinter.Radiobutton(
            window,
            text=optionsText[i],
            variable=state,
            value=i,
            font=(font, 20)))
        options[i].pack(pady=padding)
    
    BackAndNext(Question1, Question3)

# This question asks the user if they have given information that can be used to discriminate.
def Question3():
    # Question
    question = tkinter.Label(
        window,
        text="Which of these have you\nbeen asked to provide data for?",
        font=(font, 30))
    question.pack(pady=padding)

    """ There is definetly way more factor that can be used to discriminate, but these are the ones
    I can think of right now, this is why I changed the for loop from a hardcoded value, to
    something that changes as the list changes. """
    # Options
    options = []
    optionsText = [
        "Your race",
        "Your ethnitity",
        "Your financial status",
        "Your religion",
        "Your politics"]
    for i in range(len(optionsText)):
        var = tkinter.BooleanVar()
        option = tkinter.Checkbutton(
            window,
            text=optionsText[i],
            variable=var,
            font=(font, 20))
        option.var = var
        options.append(option)
        option.pack(pady=padding)
    
    BackAndNext(Question2, StartScreen, MultiSelectLogic, options, "Discrimitive")

""" I've tried to make this function act as sort of a base for other screen functions, but I just
can't figure it out. I think it would be easier if I was able to use Python classes, but I don't
know. """
""" Showcases a screen that displays a multiple choice question where the user can pick multiple
answers """
def MultiSelect():
    # Question
    question = tkinter.Label(window, text="Pick your answers", font=(font, 30))
    question.pack(pady=padding)

    # Options
    options = []
    for i in range(4):
        var = tkinter.BooleanVar()
        option = tkinter.Checkbutton(
            window,
            text="Option #"+str(i + 1),
            variable=var,
            font=(font, 20))
        option.var = var
        options.append(option)
        option.pack(pady=padding)
    
    BackAndNext(StartScreen, SingleSelect)

# Showcases a screen that displays a multiple choice question where the user only picks one answer
def SingleSelect():
    # Question
    question = tkinter.Label(window, text="Pick an answer", font=(font, 30))
    question.pack(pady=padding)

    """ There is a very stupid bug where some of the radio buttons are selected when they are
    created, but it is random, and programing languages aren't supposed to be random like this. 
    I have tried to fix this but I don't even know why it exists in the first place. """
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
    
    BackAndNext(MultiSelect, StartScreen)

def LearnMoreScreen():
    # Scrolling Text Box
    textBox = ScrolledText(window, width=50, height=10, wrap=tkinter.WORD)
    textBox.pack(padx=padding, fill=tkinter.BOTH, expand=True)
    with open("LearnMore.txt", "r") as file:
        content = file.read()
    textBox.insert(tkinter.END, content)
    textBox.config(state="disabled")

    """ There could be a better resource here, "Weapons of Math Destruction" shouldn't be the link
    that exists when we turn our project in. """
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