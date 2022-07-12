"""
This program was written by Sam Horrobin on 23/11/19.
This program is used when the user selects 'popularity' in the GUI.
It returns the unique names of each book in the database and the number of times
each unique book name's copies have been checked out, in desceding order of popularity.
"""

import database as db

"""
popularityList has no parameters, as none are required, as it just goes through the
logfile, adding books to a list and adding he number of times they have been taken out
to another list, then sorting them into the correct order of popularity.
"""

def popularityList():
    namesList = []
    noTimesList = []
    noTimesList2 = []
    logRecords = db.getAllRecords('logfile.txt')
    for i in range(len(logRecords)):
        splitLogRecord = logRecords[i].split('_')
        bookName = splitLogRecord[1]
        if bookName not in namesList: #if the book hasn't been found yet add it to namesList
            namesList.append(bookName)
            noTimesList.append(int('1')) #at the same index as the name was added to nameList,
            #add 1 to noTimesList, to indicate it has been checked out once.
        else:
            #if it was in namesList however, increment the index that the book resides in in bookName
            #in noTimesList, to show the book has been checked out again.
            index = namesList.index(bookName)
            noTimesList[index] += 1
    #creates a duplicate list of the noTimesList
    for i in range(len(noTimesList)):
        noTimesList2.append(noTimesList[i])

    #sorts noTimesList2 in ascending order.
    noTimesList2.sort()

    for i in range(len(noTimesList2)):
        number = noTimesList2[i]  #gets the next lowest value in noTimesList2
        index = noTimesList.index(number)  #gets the index in noTimesList of the element that contains the same number (next lowest value)
        temp = namesList[i]   #sets the element being swapped = to a temporary value so it can be swapped.
        namesList[i] = namesList[index] #sets the position of the next lowest value (i)= to the book corresponding to it (swaps the books)
        namesList[index] = temp #makes position it was swapped from = to the other book title that hasn't been placed yet.
        noTimesList[index] = '' #makes the index of the number that just had the book swapped out of it = ''
                                            #so it cannot be incorrectly used in a future iteration.
        temp = noTimesList[i]
        noTimesList[i] = noTimesList[index]  #swapping the values around in noTimesList to reflect the swap that was made in bookNameList
        noTimesList[index] = temp

    #lists are reversed so they are in descending order.
    namesList.reverse()
    noTimesList2.reverse()

    realList = []
    
    for i in range(len(namesList)):
        realList.append(("""
%d --- %s, %d
"""%(i+1, namesList[i], noTimesList2[i])))

    return realList, namesList, noTimesList2



        
