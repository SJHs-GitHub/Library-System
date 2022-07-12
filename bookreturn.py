"""
This program was written by Sam Horrobin on 22/11/19
This program is used when a book is returned to the library, so the library records
can be updated accordingly.
First, the input is validated, and if valid, the database and logfile are updated accordingly.
If the input is invalid it rteurns an appropriate message.
"""

import database as db
import booksearch as bs
import time
from datetime import datetime

"""
validateReturn validates the bookID to make sure it is of the correct type and form, and is
actually present in the database. If it isn't, an error message is returned, else program flow
continues.
The parameter bookID is the input from the user, and is used to see which record needs to be
updated in the database and the logfile.
"""

def validateReturn(bookID):
    returned = False
    try:
        bookID = int(bookID) #checks if bookID is an integer first (correct type).
        # purpose of this try block is checking if bookID is present in db, and if so at which index
        #is the record in database, so it can be updated correctly.
        books = db.getAllRecords('database.txt')
        #for loop goes through each record until book is found or end is reached.
        for i in range(len(books)):
            splitBook = books[i].split('_')     #splits the records up at the underscore positions
            #so each field (eg name, or memberID) is it's own list element so each field
            #in the record can be checked.
            if splitBook[0] == str(bookID):
                #if runs if the desired ID is present in a record
                splitBook[-1] = splitBook[-1].strip()
                if splitBook[-1] != '0':
                    #if memberID is not zero, can be returned.
                    updateIndex = i       #sets the variable = to the position of the record
                    #in the db so the correct record can be updated later.
                    returned = True
                    break      #breaks out of the for loop so program flow can continue.
                else:
                    #if memberID is zero it mustn't be checked out
                    #so cannot be returned
                    return "That book has not been checked out, \n\
so cannot be returned. Please re-try."

            else:
                pass
        #the program runs the below code when the for loop has been fully iterated through.
        #2 reasons why this code could be ran - book is not checked out,
        #or the bookID doesn't exist. The next code is ran only if ID doesn't exist, by
        # using returned == False so non-checked out books cannot run this code
        #and give the wrong message back to user.
        if i+1 == len(books) and returned == False:
            return "Book ID not in database. \n\
Please re-try."
                    
    except ValueError:
        return "Error - Invalid Book ID. \n\
Please try again."

    successfulReturn = returnInTxtFile(updateIndex, bookID)
    return successfulReturn

"""
returnInTxtFile updates the correct record in the database file to show the book has
been returned. It then searches through the logfile to find the record that needs to
be updated to show the book has been returned (as ths bookID will have a checkout date,
but not a return date, and so can be identified). recordIndex stores the value of the index
of the record in the database file which needs to have the memberID field updated.
bookID stores the value of the bookID which needs to be updated in the logfile.
"""

def returnInTxtFile(recordIndex, bookID):
    books = db.getAllRecords('database.txt')
    splitBook = books[recordIndex].split('_') #recordIndex = updateIndex above, and is the index of the correct record
    #found before. It is split so individual fields can be changed.
    splitBook[-1] = '0\n' #sets final field = 0, as book has been returned.
    joinBook = ", ".join(splitBook) #makes the record one list element again.
    joinBook = joinBook.replace(', ', '_') #puts it back into stored format.
    books[recordIndex] = joinBook #puts updated record back into list of records.
    success = db.writeRecords('database.txt', books, 'w') #writes records back to file.

    logRecords = db.getAllRecords('logfile.txt')
    #this for loop reads all the records in logfile, and iterates through each one until the correct record is found,
    #when the '-' which was previously the placeholder for the return date (to signify it needs to be returned)
    #
    for i in range(len(logRecords)):
        splitLogRecord = logRecords[i].split('_')
        if splitLogRecord[-1] == '-\n': #if the book hasn't been returned
            if splitLogRecord[0] == str(bookID): #and the bookID is the same as the bookID they are returning
                #update the record with today's date to show it was returned.
                dateTime = datetime.now()
                currentDate = ("%s/%s/%s\n" % (dateTime.day, dateTime.month, dateTime.year)) 
                splitLogRecord[-1] = currentDate
                joinedLogRecord = ', '.join(splitLogRecord)
                joinedLogRecord = joinedLogRecord.replace(", ", "_")
                logRecords[i] = joinedLogRecord
                break
            else:
                pass
        else:
            pass
    
    returnedStuff = db.writeRecords('logfile.txt', logRecords, 'w') #write records back to logfile.

    return success

