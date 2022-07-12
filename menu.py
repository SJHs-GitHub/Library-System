"""
This program was written by Sam Horrobin on 9/12/19.
This program provides a GUI using tkinter, as well as handling
all the inputs and outputs to the program, and providing the
graphing functionality for the popularity of books using matplotlib.
This program is the basis for all user interaction with the program.
"""

import booksearch as bs
import bookcheckout as bc
import bookreturn as br
import booklist as bl
from tkinter import *
#import matplotlib.pyplot as plot
#------------------------
#checkout functions
"""
this function is ran when the user selects checkout in the GUI.
checkout changes the text displayed to an appropriate message telling the user
what to do next. It then configures the enter button to change it's command to
the function for checkout to work, so when the enter button is pressed,
the code that is ran means the checkout function will be ran.
"""

def checkout():
    changeText("Please enter the ID of the member who is  \n\
checking out the book out, then the ID of the \n\
book that is being checked out. (e.g. 1111 4).")
    enterButton.config(command = checkoutEnter)

"""
checkoutEnter is ran after the user selects enter, after they selected checkout.
It gets the input from the entry and calls the bookcheckout function validateCheckout
with the appropriate data from the entry as parameters, then displays the
message returned from the function call.
"""

def checkoutEnter():
    memBookIds = entry1.get()
    memberID = memBookIds[:5]
    bookID = memBookIds[5:]
    returned = bc.validateCheckout(memberID, bookID)
    changeText(returned)
#------------------------
#return functions
"""
this function is ran when the user selects return in the GUI.
returnBook changes the text displayed to an appropriate message telling the user
what to do next. It then configures the enter button to change it's command to
the function for return to work, so when the enter button is pressed,
the code that is ran means the return function will be ran.
"""

def returnBook():
    changeText("Please enter the ID of the \n\
book that is being returned. (e.g. 1111).")
    enterButton.config(command = returnEnter)

"""
returnEnter is ran after the user selects enter, after they selected return.
It gets the input from the entry and calls the bookreturn function validateReturn
with the appropriate data from the entry as parameters, then displays the
message returned from the function call.
"""

def returnEnter():
    bookID = entry1.get()
    returned = br.validateReturn(bookID)
    changeText(returned)
#------------------------
#search functions
"""
this function is ran when the user selects search in the GUI.
search changes the text displayed to an appropriate message telling the user
what to do next. It then configures the enter button to change it's command to
the function for search to work, so when the enter button is pressed,
the code that is ran means the search function will be ran.
"""
    
def search():
    changeText("Enter name of desired book\n")
    enterButton.config(command = searchEnter)

"""
searchEnter is ran after the user selects enter, after they selected search.
It gets the input from the entry and calls the function getBook from booksearch
with the appropriate data from the entry as parameters, then displays the
message returned from the function call.
"""

def searchEnter():
    wantedBook = entry1.get()
    Books = bs.getBook(wantedBook)
    label2.config(text = Books)
#------------------------
#popularity functions
"""
popularity is ran when the user selects 'popularity' from the GUI.
It calls the booklist function popularityList which returns 3 things,
popBooks, which is a text description of the popularity of books,
namesList, which is a sorted list of book names, in decreasing popularity
order, and noTimesList2, which holds the number of times each book
was checked out. It then uses the imported matplotlib module to create
a bar chart to visually display the data.
"""
def popularity():
    popBooks, namesList, noTimesList2 = bl.popularityList()
    label2.config(text = popBooks)
    """
    figure = plot.figure()            #creates a figure
    axes = figure.add_subplot()          #adds axes to the figure.
    axes.bar(namesList, noTimesList2)       #makes it a bar chart, defines data for axes (x, y).
    axes.set_title("Popularity!")
    plot.xlabel('Book Name')
    plot.ylabel('Times Checked Out')
    plot.show()    #displays the chart.
    """
#------------------------
"""
enter is the default function the enter button is bound to. This changes when the user
selects an option.
"""
 
def enter():
    "DEFAULT"

"""
changeText is used to change the text that is displayed in the GUI.
It is called by many functions and is the primary way of
outputting information to the user.
"""

def changeText(newText):
   label2.config(text = newText)

"""
Below is all the code that implements the GUI, through tkinter.
First a tkinter window is created, and it is customised to how I want it to look.
Then a frame is created to hold the other widgets.
After, the other widgets are created, with them each being placed where I want them
in the frame using the grid method, and some are further configured to change
additional properties (eg adding borders with relief and bd, selecting font types and sizes).
Then the mainloop method is ran, starting the program by creating the GUI and waitinf for
an event to occur.
"""
    

frontPage = Tk()

frontPage.title("Library System")
frontPage.configure(background = "azure")
frontPage.geometry("480x640")
frontPage.resizable(width=False, height=False)

frame = Frame(bg = "azure")
frame.pack(side=TOP)

label = Label(frame, text = "First select the operation\
 you wish to perform.\n Then follow the on screen commands.", width = 38, bg = "azure")
label.grid(column = 0, row = 0, columnspan = 4)
label.config(font=("Calibri", 12))

checkoutButton = Button(frame, text = "Checkout", height = 1, width = 12, command = checkout, bg = "azure")
checkoutButton.grid(column = 0, row = 1)
checkoutButton.config(font=("Calibri", 12), relief = "solid", bd = 1)

returnButton = Button(frame, text = "Return", height = 1, width = 12, command = returnBook, bg = "azure")
returnButton.grid(column = 1, row = 1)
returnButton.config(font=("Calibri", 12), relief = "solid", bd = 1)

searchButton = Button(frame, text = "Search", height = 1, width = 12, command = search, bg = "azure")
searchButton.grid(column = 2, row = 1)
searchButton.config(font=("Calibri", 12), relief = "solid", bd = 1)

popButton = Button(frame, text = "Popularity", height = 1, width = 12, command = popularity, bg = "azure")
popButton.grid(column = 3, row = 1)
popButton.config(font=("Calibri", 12), relief = "solid", bd = 1)

entry1 = Entry(frame, bg = 'sky blue', width = 40)
entry1.grid(column = 0, row = 2, columnspan = 4)
entry1.configure(font=("Calibri", 12), relief = "solid", bd = 1)
entry1.bind(enter())

enterButton = Button(frame, text = "Enter", height = 1, width = 12, command = enter, bg = "azure")
enterButton.grid(column = 0, row = 3, columnspan = 4)
enterButton.config(font=("Calibri", 12), relief = "solid", bd = 1)

label2 = Label(frame, text = "", width = 50, bg = "white")
label2.grid(column = 0, row = 4, columnspan = 4)
label2.config(font=("Calibri", 12), relief = "solid", bd = 1 )

frontPage.mainloop()


