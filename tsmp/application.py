import tkinter as tk
from tkinter import ttk
from tsmp.map import Map
from solution.solve import Solve


class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.node_count = tk.IntVar(self, 6)
        self.map = None
        self.create_widgets()

    def create_widgets(self):
        self.label_node_count = tk.Label(self, text='Node Count').grid(row=0, column=0, pady=5, padx=5, sticky=tk.W)
        self.input_node_count = tk.Entry(self, textvariable=self.node_count).grid(row=0, column=1, pady=5)
        self.button_generate_map = tk.Button(self, text='Generate Map', command=self.generate_map).grid(row=0, column=2, pady=5)
        self.button_solve_map = tk.Button(self, text='Solve Map', command=self.solve_map).grid(row=0, column=3, pady=5)

        TABLE_MAP_COLUMNS = (
            'Node',
            'X',
            'Y',
        )
        self.table_map = ttk.Treeview(self, columns=TABLE_MAP_COLUMNS, show='headings')
        self.table_map.grid(row=3, column=0, columnspan=4, padx=5)
        for COLUMN in TABLE_MAP_COLUMNS:
            self.table_map.heading(COLUMN, text=COLUMN)

    def generate_map(self):
        self.map = Map(self.node_count.get())
        for key, val in self.map.node_list:
            self.table_map.insert('', 'end', values=(key, val.x, val.y))

    def solve_map(self):
        solve = Solve(self.map)
        solve.run()
