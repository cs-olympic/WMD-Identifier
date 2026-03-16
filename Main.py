""" In this file, there used to be a MultiSelect function and a SingleSelect function that were
meant to be base functions for the question functions, but I couldn't figure that out. There is
also a bug that makes it so that one of the radio buttons in a single select question is
automaticly selected, I also can't figure that one out. Lastly, there is plenty of spelling
mistakes in the comments. I was hoping to make for questions and more screens for this projects,
but time didn't allow for them. """

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
    "Discrimitive" : 0, # How discrimitive the algorithim is
    "Scale" : 0, # The reach of the algorithim
    "Harmfulness" : 0} # How Harmful the algorithim is

# Window
window = tkinter.Tk()
window.title(title)
window.geometry("800x550")

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
        argument=None, # The option button that are apart of the screen
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
            questionType(argument, changing)

        # Debugging
        print(scores)

        ChangeScreens(nextScreen)
    nextButton = tkinter.Button(buttonFrame, text="Next", command=next, font=(font, 20), width=5)
    nextButton.pack(side=tkinter.RIGHT, padx=padding, pady=padding)

def LearnMoreButton(anchor):
    def learnMore():
        ChangeScreens(LearnMoreScreen)
    lmButton = tkinter.Button(
        window,
        text="Learn More",
        command=learnMore,
        font=(font, 40),
        width=10,)
    lmButton.pack(pady=padding, anchor=anchor)

# Logic that happens when the user has left a screen with a single select question
def SingleSelectLogic(
        var, # The variable that is geeting checked
        changing): # The score that is getting changed
    scores[changing] += var.get()

# The logic that happens when the user has left a screen with a multi select question
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
        font=(font, 40),
        width=7)
    startButton.pack(pady=padding)

    LearnMoreButton(anchor="n")

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
    optionsText.reverse()
    var = tkinter.IntVar(value=1)
    for i in range(len(optionsText)):
        options.append(tkinter.Radiobutton(
            window,
            text=optionsText[i],
            variable=var,
            value=i,
            font=(font, 20)))
        options[i].pack(pady=padding)
    
    BackAndNext(StartScreen, Question2, SingleSelectLogic, var, "Opaqueness")

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
    var = tkinter.IntVar(value=1)
    for i in range(len(optionsText)):
        options.append(tkinter.Radiobutton(
            window,
            text=optionsText[i],
            variable=var,
            value=i,
            font=(font, 20)))
        options[i].pack(pady=padding)
    
    BackAndNext(Question1, Question3, SingleSelectLogic, var, "Opaqueness")

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
    
    BackAndNext(Question2, Question4, MultiSelectLogic, options, "Discrimitive")

""" This question ask the user how large the insurence company is, this provides an estimate for the
app's scale score. """
def Question4():
    # Question
    question = tkinter.Label(
        window,
        text="How many people does your\ninsurance provider serve?",
        font=(font, 30))
    question.pack(pady=padding)

    """ These options could be better, but because I don't research insurence providers
    professionally, these are the best I can think of. """
    # Options
    options = []
    optionsText = [
        "Less than 2,000",
        "2,001 - 10,000",
        "10,001 - 100,000",
        "100,001 - 1 million",
        "1 million - 10 million",
        "More than 10 million"]
    var = tkinter.IntVar(value=1)
    for i in range(len(optionsText)):
        options.append(tkinter.Radiobutton(
            window,
            text=optionsText[i],
            variable=var,
            value=i,
            font=(font, 20)))
        options[i].pack(pady=padding)
    
    BackAndNext(Question3, Question5, SingleSelectLogic, var, "Scale")

# This question asks the user if their insurence rates are high.
def Question5():
    # Question
    question = tkinter.Label(
        window,
        text="Would you consider your\ninsurance rates high?",
        font=(font, 30))
    question.pack(pady=padding)

    """ I accidentally wrote the optionText list in the wrong order, so instead of rewriting it,
    I instead used the reverse function because of lazyness. """
    # Options
    options = []
    optionsText = ["Yes, they are very high", "They are pretty normal", "No, they seem pretty low"]
    optionsText.reverse()
    var = tkinter.IntVar(value=1)
    for i in range(len(optionsText)):
        options.append(tkinter.Radiobutton(
            window,
            text=optionsText[i],
            variable=var,
            value=i,
            font=(font, 20)))
        options[i].pack(pady=padding)
    
    BackAndNext(Question4, Summary, SingleSelectLogic, var, "Harmfulness")

def Summary():
    message = ""

    # Screen Logic
    totalMaxScore = 18
    finalScore = 0
    for key, value in scores.items():
        finalScore += value
    if finalScore >= (totalMaxScore / 4) * 3:
        message = "You ARE being\naffected by a WMD"
    elif finalScore >= (totalMaxScore / 4) * 2:
        message = "You might be\naffected by a WMD,\nbut you will need\nto do more research"
    else:
        message = "You are NOT being\naffected by a WMD"
    
    # Label that give the user the result of the questionare
    messageLabel = tkinter.Label(window, text=message, font=(font, 50))
    messageLabel.pack(pady=50)

    LearnMoreButton("s")

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