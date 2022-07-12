"""
This program was written by Sam Horrobin on 21/11/19
It is used when the user wants to view the details about all the books with
a certain name. It returns a list of all books with that name and their
associated information from database.
"""

import database as db

"""
getBook takes wantedBook as a parameter and this is the name input by the user.
All books with this name have their associated information taken from the
database and are returned and presented for the user.
"""

def getBook(wantedBook):
    returnList = []
    bookList = db.getAllRecords('database.txt')
    for i in range(len(bookList)):
        if wantedBook in bookList[i]:
            returnList.append(bookList[i])
    return returnList
















