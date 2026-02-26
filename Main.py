# Libraries
import tkinter
import webbrowser

from tkinter.scrolledtext import ScrolledText

# Variables
Title = "WMD Identifier"
Font = "Arial"
Padding = 10

# Window
Window = tkinter.Tk()
Window.title(Title)
Window.geometry("800x500")

def ChangeScreens(screen):
    # Clear the window
    for widget in Window.winfo_children():
        widget.destroy()

    screen()

def BackAndNext(prevScreen, nextScreen):
    # Prepare a frame for the buttons
    buttonFrame = tkinter.Frame(Window)
    buttonFrame.pack(side=tkinter.BOTTOM, fill=tkinter.X)

    # Back Button
    def back():
        ChangeScreens(prevScreen)
    backButton = tkinter.Button(buttonFrame, text="Back", command=back, font=(Font, 20), width=5)
    backButton.pack(side=tkinter.LEFT, padx=Padding, pady=Padding)

    # Next Question Button
    def next():
        ChangeScreens(nextScreen)
    nextButton = tkinter.Button(buttonFrame, text="Next", command=next, font=(Font, 20), width=5)
    nextButton.pack(side=tkinter.RIGHT, padx=Padding, pady=Padding)

def StartScreen():
    # Title
    titleLabel = tkinter.Label(Window, text=Title, font=(Font, 60))
    titleLabel.pack(pady=Padding)

    # Start Button
    def start():
        ChangeScreens(MultipleChoice)
    startButton = tkinter.Button(
        Window,
        text="Start",
        command=start,
        font=(Font, 40), # The font size affects the width and height of the button
        width=7) # Width overrides the font size's set width
    startButton.pack(pady=Padding)

    # Learn More button
    def learnMore():
        ChangeScreens(LearnMoreScreen)
    lmButton = tkinter.Button(
        Window,
        text="Learn More",
        command=learnMore,
        font=(Font, 40),
        width=10)
    lmButton.pack(pady=Padding)

# Showcases a screen that displays a multiple choice question
def MultipleChoice():
    BackAndNext(StartScreen, StartScreen)

    # Question
    question = tkinter.Label(Window, text="Pick an answer", font=(Font, 30))
    question.pack(pady=Padding)

    # Choices
    choices = []
    for i in range(4):
        choices.append(tkinter.Checkbutton(
            Window,
            text = "Choice #" + str(i + 1),
            var=tkinter.BooleanVar(),
            font=(Font, 20)))
        choices[i].pack(pady=Padding)

def LearnMoreScreen():
    # Scrolling Text Box
    textBox = ScrolledText(Window, width=50, height=10, wrap=tkinter.WORD)
    textBox.pack(padx=Padding, fill=tkinter.BOTH, expand=True)
    with open("LearnMore.txt", "r") as file:
        content = file.read()
    textBox.insert(tkinter.END, content)
    textBox.config(state="disabled")

    # Hyperlink for more resources
    def openLink(event):
        webbrowser.open("https://ia800603.us.archive.org/12/items/fflch-livro-weapons-of-math-destruction-cathy-240826-220339/(FFLCH)%20LIVRO%20Weapons%20of%20Math%20Destruction%20-%20Cathy%20_240826_220339.pdf")
    link = tkinter.Label(Window, text="Learn even more!", fg="blue", cursor="hand2")
    link.pack(pady=Padding)
    link.bind("<Button-1>", openLink)

    # Back Button
    buttonFrame = tkinter.Frame(Window)
    buttonFrame.pack(side=tkinter.BOTTOM, fill=tkinter.X)
    def back():
        ChangeScreens(StartScreen)
    backButton = tkinter.Button(buttonFrame, text="Back", command=back, font=(Font, 20), width=5)
    backButton.pack(side=tkinter.LEFT, padx=Padding, pady=Padding)

# Start Program
StartScreen()
Window.mainloop()