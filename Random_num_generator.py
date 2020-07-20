# Random Number Generator
import random
from guizero import App, Text, TextBox, PushButton, error
from tkinter import Spinbox


# Creating Random Number and validation
def createRanNumber():
    try:
        ranNum1 = int(ranInput1.get())
        ranNum2 = int(ranInput2.get())
        if ranNum1 < ranNum2:
            ranNum = random.randrange(ranNum1, ranNum2)
            ranNumText.value = int(ranNum)
        else:
            ranNum = random.randrange(ranNum2, ranNum1)
            ranNumText.value = int(ranNum)
    except:
        error("Num Generator", "Please provide two different numbers between 1 and 1000000")

# GUI
app = App(title="Random Number Generator", width=350, height=300)
range_text = Text(app, text="Enter a range.", align="top")
range_text.text_color = "blue"
generate_text = Text(app, text="Press the button to generate a random number.", align="top")
generate_text.text_color = "blue"
ranInput1 = Spinbox(from_=0, to=1000000, wrap="True")
ranInput2 = Spinbox(from_=0, to=1000000, wrap="True")
app.add_tk_widget(ranInput1)
app.add_tk_widget(ranInput2)
genNum = PushButton(app, command=createRanNumber, text="Generate Number")
ranNumText = Text(app, size=40, text="", font="Calibri", color="blue")
app.display()
