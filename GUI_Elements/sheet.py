import tkinter
import customtkinter


global startingDataLst
startingDataLst = [('Team','Practice match','Match 1','Match 2', 'Match 3'),
        ('Team 1','','','','',''),
        ('Team 2','','','','',''),
        ('Team 3','','','','',''),
        ('Team 4','','','','','')]
global numrows, numcols, numCells
numrows = len(startingDataLst)
numcols = len(startingDataLst[0])
numCells = numcols*numrows

def initDisplaySheet(window):
    global acsessDisplayLst
    acsessDisplayLst = []
    for row in range(numrows):

        for col in range(numcols):

            global entry
            entry = tkinter.Entry(window,width=15, fg='blue', font=('Arial',25, 'bold'), border=5)
            entry.grid(row=row+1, column=col+1)
            
            entry.insert(0,startingDataLst[row][col])
            acsessDisplayLst.append(entry)

def initEntrySheet(window):
    global acsessEntryLst
    acsessEntryLst = []
    for row in range(numrows):

        for col in range(numcols):

            global entry
            entry = tkinter.Entry(window,width=25, fg='blue', font=('Arial',40, 'bold'), border=5)
            
            entry.grid(row=row+1, column=col+1)
            #entry.grid_location(50,50)
            entry.insert(0,startingDataLst[row][col])
            acsessEntryLst.append(entry)


def getData(index):
    return acsessEntryLst[index].get()

def showNewData():
    for i in range():
        acsessLst()
def createDisplayLst():
    displayLst = []
    for index in range(numCells):
        displayLst.append(getData(index))
    return displayLst
