import tkinter as tk
from tkinter import ttk
from tsmp.map import Map
from solution.solve import Solve
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg)
from matplotlib.figure import Figure
from tsmp.settings import MAXIMUM_ACCURATE_NODE_COUNT

class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.notebook_information = ttk.Notebook(self)
        self.notebook_visual = ttk.Notebook(self)
        self.tab_map = ttk.Frame(self.notebook_information)
        self.tab_node = ttk.Frame(self.notebook_information)
        self.tab_path = ttk.Frame(self.notebook_information)
        self.tab_solution = ttk.Frame(self.notebook_information)
        self.tab_map_visual = ttk.Frame(self.notebook_visual)
        self.tab_shortest_visual = ttk.Frame(self.notebook_visual)
        self.tab_longest_visual = ttk.Frame(self.notebook_visual)
        self.tab_solution_visual = ttk.Frame(self.notebook_visual)
        self.notebook_information.add(self.tab_map, text='Map')
        self.notebook_information.add(self.tab_node, text='Nodes')
        self.notebook_information.add(self.tab_path, text='Path')
        self.notebook_information.add(self.tab_solution, text='Solution')
        self.notebook_visual.add(self.tab_map_visual, text='Map')
        self.notebook_visual.add(self.tab_solution_visual, text='Solution Path')
        self.notebook_visual.add(self.tab_shortest_visual, text='Shortest Path')
        self.notebook_visual.add(self.tab_longest_visual, text='Longest Path')
        self.grid()
        self.node_count = tk.IntVar(self, 6)
        self.solution_selected = tk.StringVar(self, 'Basic')
        self.map = None
        self.create_widgets()

    def create_widgets(self):
        self.label_node_count = tk.Label(self, text='Node Count ('+str(MAXIMUM_ACCURATE_NODE_COUNT)+' Maximum for Accurate Solve)').grid(row=0, column=0, pady=5, padx=5, sticky='e')
        self.entry_node_count = tk.Entry(self, textvariable=self.node_count).grid(row=0, column=1, pady=5, sticky='w')
        self.button_generate_map = tk.Button(self, text='Generate Map', command=self.generate_map).grid(row=0, column=2, pady=5)
        self.option_solution_select = tk.OptionMenu(self, self.solution_selected, 'Basic', 'Random', 'Weighted Angle').grid(row=0, column=3, pady=5)
        self.button_run_solution = tk.Button(self, text='Run Solution', command=self.run_solution).grid(row=0, column=4, pady=5)
        self.button_solve_map = tk.Button(self, text='Solve Map', command=self.solve_map).grid(row=0, column=5, pady=5)

        TREE_MAP_INFORMATION_COLUMNS = ('Type', 'Value')
        self.tree_map_information = ttk.Treeview(self.tab_map, height=20, columns=TREE_MAP_INFORMATION_COLUMNS, show='headings')
        self.tree_map_information.column('Value', anchor='e')
        self.tree_map_information.grid(row=0, column=0, sticky='nwse')
        self.tree_map_scrollbar = ttk.Scrollbar(self.tab_map, orient='vertical', command=self.tree_map_information.yview)
        self.tree_map_information.configure(yscroll=self.tree_map_scrollbar.set)
        self.tree_map_scrollbar.grid(row=0, column=1, sticky='nse')
        for COLUMN in TREE_MAP_INFORMATION_COLUMNS:
            self.tree_map_information.heading(COLUMN, text=COLUMN)

        TREE_NODE_INFORMATION_COLUMNS = ('Number', 'X Position', 'Y Position',)
        self.tree_node_information = ttk.Treeview(self.tab_node, height=20, columns=TREE_NODE_INFORMATION_COLUMNS, show='headings')
        self.tree_node_information.column('X Position', anchor='e')
        self.tree_node_information.column('Y Position', anchor='e')
        self.tree_node_information.grid(row=0, column=0, sticky='nwse')
        self.tree_node_scrollbar = ttk.Scrollbar(self.tab_node, orient='vertical', command=self.tree_node_information.yview)
        self.tree_node_information.configure(yscroll=self.tree_node_scrollbar.set)
        self.tree_node_scrollbar.grid(row=0, column=1, sticky='nse')
        for COLUMN in TREE_NODE_INFORMATION_COLUMNS:
            self.tree_node_information.heading(COLUMN, text=COLUMN)

        TREE_PATH_INFORMATION_COLUMNS = ('Solution', 'Type', 'Distance', 'Order',)
        self.tree_path_information = ttk.Treeview(self.tab_path, height=20, columns=TREE_PATH_INFORMATION_COLUMNS, show='headings')
        self.tree_path_information.column('Distance', anchor='e')
        self.tree_path_information.column('Order', anchor='center')
        self.tree_path_information.grid(row=0, column=0, sticky='nwse')
        self.tree_path_scrollbar = ttk.Scrollbar(self.tab_path, orient='vertical', command=self.tree_path_information.yview)
        self.tree_path_information.configure(yscroll=self.tree_path_scrollbar.set)
        self.tree_path_scrollbar.grid(row=0, column=1, sticky='nse')
        for COLUMN in TREE_PATH_INFORMATION_COLUMNS:
            self.tree_path_information.heading(COLUMN, text=COLUMN)

        TREE_SOLUTION_INFORMATION_COLUMNS = ('Type', 'Value',)
        self.tree_solution_information = ttk.Treeview(self.tab_solution, height=20, columns=TREE_SOLUTION_INFORMATION_COLUMNS, show='headings')
        self.tree_solution_information.column('Value', anchor='center')
        self.tree_solution_information.grid(row=0, column=0, sticky='nwse')
        self.tree_solution_scrollbar = ttk.Scrollbar(self.tab_solution, orient='vertical', command=self.tree_solution_information.yview)
        self.tree_solution_information.configure(yscroll=self.tree_solution_scrollbar.set)
        self.tree_solution_scrollbar.grid(row=0, column=1, sticky='nse')
        for COLUMN in TREE_SOLUTION_INFORMATION_COLUMNS:
            self.tree_solution_information.heading(COLUMN, text=COLUMN)

        self.label_node_count = tk.Label(self, text='Information').grid(row=1, column=0, columnspan=4, pady=5, padx=5)
        self.notebook_information.grid(row=2, column=0, columnspan=4, padx=10, sticky='nwse')
        self.label_node_count = tk.Label(self, text='Visual').grid(row=1, column=4, columnspan=2, pady=5, padx=5)
        self.notebook_visual.grid(row=2, column=4, columnspan=4, padx=10, sticky='nwse')

    def generate_map(self):
        self.clear_tree(self.tree_node_information)
        self.clear_tree(self.tree_map_information)
        self.clear_tree(self.tree_path_information)
        self.map = Map(self.node_count.get())
        self.draw_map()
        for key, value in self.map.node_list.items():
            self.tree_node_information.insert('', 'end', values=(key, value.x, value.y))
        self.tree_map_information.insert('', 'end', values=('Node Count', self.map.node_count))

    def solve_map(self):
        if self.map:
            solve = Solve(self.map)
            solve.run()
            self.draw_path(solve.shortest_path, self.tab_shortest_visual)
            self.draw_path(solve.longest_path, self.tab_longest_visual)
            self.tree_map_information.insert('', 'end', values=('Solve Paths', solve.path_count))
            self.tree_path_information.insert('', 'end', values=('Solve', 'Shortest Path', str(solve.shortest_distance), str(solve.shortest_path)))
            self.tree_path_information.insert('', 'end', values=('Solve', 'Longest Path', str(solve.longest_distance), str(solve.longest_path)))
            for key, val in solve.information.items():
                self.tree_solution_information.insert('', 'end', values=(key, val))

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
            fig.add_subplot(111).plot(x, y, 'C3', lw=3, alpha=0.5)
        fig.add_subplot().scatter(x, y, s=120)

        self.canvas = FigureCanvasTkAgg(fig, master=tab)  # A tk.DrawingArea.
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=0, sticky='nwse')

    def run_solution(self):
        if self.map:
            if self.solution_selected.get() == 'Random':
                from solution.random import Random
                random = Random(self.map)
                random.run()
                self.draw_path(random.shortest_path, self.tab_solution_visual)
                self.tree_path_information.insert('', 'end', values=('Random', 'Shortest Path', str(random.shortest_distance), str(random.shortest_path)))
                self.insert_solution_information(random)
            elif self.solution_selected.get() == 'Basic':
                from solution.basic import Basic
                basic = Basic(self.map)
                basic.run()
                self.draw_path(basic.shortest_path, self.tab_solution_visual)
                self.tree_path_information.insert('', 'end', values=('Basic', 'Shortest Path', str(basic.shortest_distance), str(basic.shortest_path)))
                self.insert_solution_information(basic)
            elif self.solution_selected.get() == 'Weighted Angle':
                from solution.weighted_angle import WeightedAngle
                weighted_angle = WeightedAngle(self.map)
                weighted_angle.run()
                self.draw_path(weighted_angle.shortest_path, self.tab_solution_visual)
                self.tree_path_information.insert('', 'end', values=('Weighted_angle', 'Shortest Path', str(weighted_angle.shortest_distance), str(weighted_angle.shortest_path)))
                self.insert_solution_information(weighted_angle)

    def insert_solution_information(self, solution):
        for key, val in solution.information.items():
            self.tree_solution_information.insert('', 'end', values=(key, val))
