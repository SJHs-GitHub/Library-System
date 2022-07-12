"""
This program was written by Sam Horrobin on 20/11/19.
It contains the functions to read and write to either the database
or the logfile.
It is used when anything needs to be read or written to the db.
"""

"""
getAllRecords returns all the records in a specified text file (db),
in the form of a list, with each list element being one record.
Parameter db references whether it should read from database or logfile.
"""

def getAllRecords(db):
    allRecordsList = []
    dbFile = open(db, "r")
    x = True
    while x == True:
        record = dbFile.readline()
        if record == '': #reads the file appending records to the list until the
            #end of the file is reached, when the list is returned.
            x = False
            return allRecordsList
        else:
            allRecordsList.append(record)
    dbFile.close

"""
writeRecords writes a set of records (records) to a specified text file (db).
db references the text file to which to write (either database or logfile),
records holds a list of the records to be written to the file, with each list
element being one record. openMode is either 'a' or 'w', indicating
whether the file needs to be empty when records are written, or if they
are to be appened to the records already there.
"""

def writeRecords(db, records, openMode):
    dbFile = open(db, openMode)
    for i in range(len(records)):
        dbFile.write(records[i])
    dbFile.close
    return 'Operation was successful!'


    
