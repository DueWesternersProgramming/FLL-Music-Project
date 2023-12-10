import tkinter
import customtkinter

global lst
lst = [('Team','Practice match','Match 1','Match 2', 'Match 3'),
        ('Team 1','','','','',''),
        ('Team 2','','','','',''),
        ('Team 3','','','','',''),
        ('Team 4','','','','','')]
global numrows, numcols
numrows = len(lst)
numcols = len(lst[0])

def initSheet(window):

    for row in range(numrows):
        for col in range(numcols):
            global entry
            entry = tkinter.Entry(window,width=25, fg='blue', font=('Arial',40, 'bold'), border=5)
            entry.grid(row=row+1, column=col+1)
            #entry.grid_location(50,50)
            entry.insert(0,lst[row][col])

def getData():
    lst.clear()

    for i in range(numrows):
        pass
        #To-do:

    return lst