import tkinter
from tsmp.application_tk import Application
from tsmp.settings import WINDOW_SIZE_X, WINDOW_SIZE_Y

root = tkinter.Tk()

root.minsize(WINDOW_SIZE_X, WINDOW_SIZE_Y)
root.title('Traveling Salesman Problem Tool')

for row_index in range(3):
    root.grid_rowconfigure(row_index, weight=1)
    for column_index in range(8):
        root.grid_columnconfigure(column_index, weight=1)

app = Application(master=root)
app.generate_map()
app.mainloop()

