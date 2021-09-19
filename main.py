# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from tree_definition import CannibalMissionaryTree
from tree_definition import Node
from tree_definition import Solution


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    # p = Person('Nikhil')
    # p.say_hi()

    # initialProblem = CannibalMissionaryTree((3, 3, 1))
    # initialProblem.print_current_state()
    # initialProblem.get_successor_states()
    # initialProblem.print_successor_states()

    # node = Node([3, 3, 1])
    # node.update_children()
    # print(node)

    solution = Solution((3, 3, 1), (0, 0, 0))
    solution.bfs_search()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
