"""
This program was written by Sam Horrobin on 22/11/19.
This program is run when the user selects 'checkout', when they want to checkout a book.
First the inputs (memberID and bookID) are validated, then the information in database and
the logfile is updated to reflect the book being checked out.
If either of the inputs are invalid it returns an appropriate error message.
"""
import database as db
import booksearch as bs
import time
from datetime import datetime

"""
validateCheckout validates the two inputs, memberID and bookID, to make sure they are
of the correct type and form, and that the input bookID is actually present in the database,
and if so at which index the record is stored in the db.
If either are invalid, an appropriate message is returned.
These are the parameters of the function, and are the information that will be added
to the logfile (and memberID in database) to show which book was checked out (bookID),
and by who (memberID).
"""

def validateCheckout(memberID, bookID):
    #below is the validation for memberID (making sure it is
    #a 4 digit integer and is not 0000.
    try:
        memberID = int(memberID)
    except ValueError:
        return "Error - Invalid Member ID. \n\
Please try again."
    if len(str(memberID)) != 4:
        return "Error - Invalid Member ID. \n\
Please try again."
    if str(memberID) == '0000':
        return "Error - Invalid Member ID. \n\
Please try again."

    str(memberID)

    checkedOut = False
    updateIndex = 0
    try:
        bookID = int(bookID) #checks if bookID is an integer first (correct type).
        # purpose of this try block is checking if bookID is present in db, and if so at which index
        #is the record in database, so it can be updated correctly.
        books = db.getAllRecords('database.txt')
        #for loop goes through each record until book is found or end is reached.
        for i in range(len(books)):
            splitBook = books[i].split('_')     #splits the record up at the underscore positions
            #so each field (eg name, or memberID) is it's own list element so each field
            #in the record can be checked.
            if splitBook[0] == str(bookID):
                #if runs if the desired ID is present in a record
                splitBook[-1] = splitBook[-1].strip()
                if splitBook[-1] == '0':
                    #if memberID is zero, can be checked out.
                    updateIndex = i       #sets the variable = to the position of the record
                    #in the db so the correct record can be updated later.
                    checkedOut = True
                    break      #breaks out of the for loop so program flow can continue.
                else:
                    #if memberID is not zero it must already be checked out
                    #so cannot be checked out now
                    return "That book has already been checked out, so is not available. \n\
Please try again."
                    
            else:
                pass
        #the program runs the below code when the for loop has been fully iterated through.
        #2 reasons why this code could be ran - book is checked out already,
        #or the bookID doesn't exist. The next code is ran only if ID doesn't exist, by
         # using checkedOut == False so checked out books cannot run this code
         #and give the wrong message back to user.
        if i+1 == len(books) and checkedOut == False :
            return "Book ID not in database. \n\
Please try again."
                    
    except ValueError:
        return "Error - Invalid Book ID. \n\
Please try again."

    successfulReturn = checkoutInTxtFile(updateIndex, memberID)
    return successfulReturn

"""
checkoutInTxtFile first updates the informtion in the database to reflect the book's new owner.
Then it writes a new record in the log file to record the information about the checkout
(e.g. who, when, which book).
recordIndex stores the value of the index of the record in the database file which
needs to have it's 'memberID' field updated to the memberID of who checked the book out.
memberID stores the value of the memberID who checked the book out, for addition
to the new logfile record.
"""

def checkoutInTxtFile(recordIndex, memberID):
    books = db.getAllRecords('database.txt')  
    splitBook = books[recordIndex].split('_') #recordIndex = updateIndex above, and is the index of the correct record
    #found before. It is split so individual fields can be changed.
    splitBook[-1] = str(memberID,)+'%s'%('\n') #sets the final element of the record = to the memberID
    joinBook = ", ".join(splitBook) #makes the record one list element again.
    joinBook = joinBook.replace(', ', '_') #puts it back into stored format.
    books[recordIndex] = joinBook #puts updated record back into list of records.
    success = db.writeRecords('database.txt', books, 'w') #writes records back to file.
    
    dateTime = datetime.now()
    currentDate = ("%s/%s/%s" % (dateTime.day, dateTime.month, dateTime.year)) 
    logRecord = [str(splitBook[0]), splitBook[1], str(memberID), currentDate, '-'] #creates a new record for the log file using
    #correct data for each field.
    joinedLogRecord = ', '.join(logRecord)
    joinedLogRecord = joinedLogRecord.replace(', ', '_')
    joinedLogRecord = joinedLogRecord+'%s'%('\n')
    returnedFromDB = db.writeRecords('logfile.txt', joinedLogRecord, 'a')
    return success
    
    
    
    
    
    

 

