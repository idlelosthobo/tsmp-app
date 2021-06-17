from time import time

from tsmp.map import Map

CONSOLE_ERROR_PREFIX = 'Error:'
CONSOLE_POSTFIX = '->'

# Key (arguments, method)
CONSOLE_COMMANDS = {
    'quit': ('stop_running', 0),
    'generate': ('generate_map', 1),
    'solve': ('solve_map', 0),
}


class Console:

    def __init__(self):
        self.console_string = ''
        self.is_running = True
        self.map = None
        self.process_start_time = time()
        self.process_end_time = time()

    def generate_map(self, node_count_string):
        node_count = int(node_count_string)
        if 12 > node_count > 0:
            self.map = Map(node_count)
        else:
            self.print_error('Node count cannot be greater than 11')

    def run(self):
        while self.is_running:
            self.update_console_string()
            self.process_input()

    def process_input(self):
        input_string = input(self.console_string)
        input_list = input_string.split(' ')

        if input_list[0] in CONSOLE_COMMANDS:
            function_name = CONSOLE_COMMANDS[input_list[0]][0]
            function_argument_count = CONSOLE_COMMANDS[input_list[0]][1]

            if hasattr(self, function_name):
                if len(input_list[1:]) == function_argument_count:
                    getattr(self, function_name)(*input_list[1:])
                else:
                    self.print_error('Invalid amount of arguments sent with command')

    def solve_map(self):
        from tsmp.solutions.solve_solution import Solve
        solved_map = Solve(self.map)
        self.start_process_timer()
        solved_map.run()
        self.end_process_timer()
        print(solved_map.shortest_distance)

    def stop_running(self):
        self.is_running = False

    def start_process_timer(self):
        self.process_start_time = time()

    def end_process_timer(self):
        self.process_end_time = time()
        elapsed_time = self.process_end_time - self.process_start_time
        print('Completed in %s' % elapsed_time)

    def update_console_string(self):
        if self.map:
            console_string = '%s Node Map' % self.map.node_count
        else:
            console_string = 'No Data'

        self.console_string = '%s %s ' % (console_string, CONSOLE_POSTFIX)

    def print_error(self, error=None):
        if error:
            print('%s %s' % (CONSOLE_ERROR_PREFIX, error))