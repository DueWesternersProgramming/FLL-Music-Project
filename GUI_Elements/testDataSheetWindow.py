import tkinter

top = tkinter.Tk()
global i
global j
def refreshSheet(e,i,j):
  e.insert(0,lst[i][j])
  e.delete(0,tkinter.END)
  e.insert(0,lst[i][j])

global lst

lst = [('Team','Practice match','Match 1'),
      ('Team 1','456','Pune'),
      ('Team 2','789','Mumbai'),
      ('Team 3','987','Mumbai'),
      ('Team 4','654','Delhi')]
numrows = len(lst)
numcols = len(lst[0])

for i in range(numrows):
  for j in range(numcols):
    e = tkinter.Entry(top, width=15, fg='blue', font=('Arial',10, 'bold'))
    e.grid(row=i, column=j)
    refreshSheet(e,i,j)

def acsessData(r,c):
  value = lst[r][c]
  return value
def hideSheet():
  for widget in top.winfo_children():
    widget.grid_remove()

def showSheet():
  for widget in top.winfo_children():
    widget.grid()
hideSheet()
top.mainloop()