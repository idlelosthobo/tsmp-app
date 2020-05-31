import tkinter as tk
from tkinter import ttk
from tsmp.map import Map
from solution.solve import Solve
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy
from random import randint


class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.notebook_information = ttk.Notebook(self)
        self.notebook_visual = ttk.Notebook(self)
        self.tab_node = ttk.Frame(self.notebook_information)
        self.tab_solve = ttk.Frame(self.notebook_information)
        self.tab_map_visual = ttk.Frame(self.notebook_visual)
        self.tab_shortest_visual = ttk.Frame(self.notebook_visual)
        self.tab_longest_visual = ttk.Frame(self.notebook_visual)
        self.notebook_information.add(self.tab_node, text='Nodes')
        self.notebook_information.add(self.tab_solve, text='Solve')
        self.notebook_visual.add(self.tab_map_visual, text='Map')
        self.notebook_visual.add(self.tab_shortest_visual, text='Shortest')
        self.notebook_visual.add(self.tab_longest_visual, text='Longest')
        self.grid()
        self.node_count = tk.IntVar(self, 6)
        self.map = None
        self.create_widgets()

    def create_widgets(self):
        self.label_node_count = tk.Label(self, text='Node Count').grid(row=0, column=0, pady=5, padx=5)
        self.entry_node_count = tk.Entry(self, textvariable=self.node_count).grid(row=0, column=1, pady=5)
        self.button_generate_map = tk.Button(self, text='Generate Map', command=self.generate_map).grid(row=0, column=2, pady=5)
        self.button_solve_map = tk.Button(self, text='Solve Map', command=self.solve_map).grid(row=0, column=3, pady=5)

        TREE_NODE_INFORMATION_COLUMNS = ('Node', 'X Position', 'Y Position',)
        self.tree_node_information = ttk.Treeview(self.tab_node, columns=TREE_NODE_INFORMATION_COLUMNS, show='headings')
        self.tree_node_information.grid(row=0, column=0, sticky='nwse')
        self.tree_node_information.column('X Position', anchor='e')
        self.tree_node_information.column('Y Position', anchor='e')
        for COLUMN in TREE_NODE_INFORMATION_COLUMNS:
            self.tree_node_information.heading(COLUMN, text=COLUMN)

        TREE_SOLVE_INFORMATION_COLUMNS = ('Type', 'Distance', 'Path',)
        self.tree_solve_information = ttk.Treeview(self.tab_solve, columns=TREE_SOLVE_INFORMATION_COLUMNS, show='headings')
        self.tree_solve_information.column('Distance', anchor='e')
        self.tree_solve_information.column('Path', anchor='center')
        self.tree_solve_information.grid(row=0, column=0, sticky='nwse')
        for COLUMN in TREE_SOLVE_INFORMATION_COLUMNS:
            self.tree_solve_information.heading(COLUMN, text=COLUMN)

        self.notebook_information.grid(row=4, column=0, columnspan=4, padx=5, sticky='nwse')
        self.notebook_visual.grid(row=4, column=5, columnspan=4, padx=5, sticky='nwse')

    def generate_map(self):
        self.clear_tree(self.tree_node_information)
        self.map = Map(self.node_count.get())
        self.draw_map()
        for key, value in self.map.node_list.items():
            self.tree_node_information.insert('', 'end', values=(key, value.x, value.y))

    def solve_map(self):
        self.clear_tree(self.tree_solve_information)
        solve = Solve(self.map)
        solve.run()
        self.draw_path(solve.shortest_path, self.tab_shortest_visual)
        self.draw_path(solve.longest_path, self.tab_longest_visual)
        self.tree_solve_information.insert('', 'end', values=('Shortest', str(solve.shortest_distance), str(solve.shortest_path)))
        self.tree_solve_information.insert('', 'end', values=('Longest', str(solve.longest_distance), str(solve.longest_path)))

    def clear_tree(self, tree):
        for i in tree.get_children():
            tree.delete(i)

    def draw_map(self):
        x = list()
        y = list()
        for key, value in self.map.node_list.items():
            x.append(value.x)
            y.append(value.y)

        self.draw_visual(x, y, self.tab_map_visual)

    def draw_path(self, path, tab):
        x = list()
        y = list()
        for node_number in path.node_order_list:
            x.append(self.map.node_list[node_number].x)
            y.append(self.map.node_list[node_number].y)

        self.draw_visual(x, y, tab, True)

    def draw_visual(self, x, y, tab, line=False):
        fig = Figure(figsize=(6, 4), dpi=100)
        if line:
            fig.add_subplot(111).plot(x, y, 'C3', lw=3)
        fig.add_subplot(111).scatter(x, y, s=120)

        self.canvas = FigureCanvasTkAgg(fig, master=tab)  # A tk.DrawingArea.
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=0, sticky='nwse')
