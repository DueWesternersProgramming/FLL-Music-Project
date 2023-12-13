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

def initDisplaySheet(window,lst=startingDataLst):
    global acsessDisplayLst
    acsessDisplayLst = []
    for row in range(numrows):
        for col in range(numcols):
            global display
            display = tkinter.Label(window,width=20, fg='blue', font=('Arial',20, 'bold'), border=5,text=(lst[row][col]))

            display.grid(row=row+1, column=col+1,ipadx=10,ipady=2)
            #entry.insert(0,str(lst[row][col]))
            acsessDisplayLst.append(display)
    print(lst[row][col])

def initEntrySheet(window):
    global acsessEntryLst
    acsessEntryLst = []
    for row in range(numrows):
        for col in range(numcols):
            global entry
            entry = tkinter.Entry(window,width=20, fg='blue', font=('Arial',20, 'bold'), border=5)

            entry.grid(row=row+1, column=col+1)
            entry.insert(0,startingDataLst[row][col])
            acsessEntryLst.append(entry)


def getEntryData(index):
    return acsessEntryLst[index].get()

def destroyCell(index):
  acsessDisplayLst[index].destroy()

def destroyAllCells():

  for i in range(numCells):
    destroyCell(i)

def createDisplayLst():
    displayLst = []
    for h in range(0,numcols):
      for i in range(0,numCells):
        displayLst.append(getEntryData(i))

    return displayLst

def update(win):
   destroyAllCells()
   displayLst = createDisplayLst()
   print(displayLst)
   initDisplaySheet(win,displayLst)
