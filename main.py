import tkinter
from tsmp.application import Application


root = tkinter.Tk()
root.minsize(900,600)
root.title('Traveling Salesman Problem Tool')
app = Application(master=root)
app.mainloop()