'''
Tree definition for the cannibal and missionary problem
'''

from collections import deque


def get_after_carry_states(input_state):
    missionary = input_state[0]
    cannibal = input_state[1]
    boat_position = input_state[2]
    states_list = []
    '''
    If boat_position = 1, it means that is in the initial position,
    therefore we need to rest the number of cannibals or missionaries,
    because these ones, are going from the initial side of the river,
    to the next one.
    
    If boat_position = 0, it means that is in the final position,
    therefore we need to add the number of cannibals or missionaries,
    because these ones, are going back to the initial side of the river.
    '''
    if boat_position == 1:
        states_list = [
            [missionary - 1, cannibal, 0],
            [missionary - 2, cannibal, 0],
            [missionary, cannibal - 1, 0],
            [missionary, cannibal - 2, 0],
            [missionary - 1, cannibal - 1, 0],
        ]

    elif boat_position == 0:
        states_list = [
            [missionary + 1, cannibal, 1],
            [missionary + 2, cannibal, 1],
            [missionary, cannibal + 1, 1],
            [missionary, cannibal + 2, 1],
            [missionary + 1, cannibal + 1, 1],
        ]
    else:
        print
        "Error: Unknown boat position."
    return states_list


def is_state_safe(current_state, next_state, limits):
    missionaries_limit = limits[0]
    cannibals_limit = limits[1]
    # Current State values
    current_missionaries = current_state[0]
    current_cannibals = current_state[1]
    # Next State Values
    next_missionaries = next_state[0]
    next_cannibals = next_state[1]
    isLessThanZero = False
    areMoreCannibals = False
    isLimitExceeded = False

    if next_missionaries < 0 or next_cannibals < 0:
        isLessThanZero = True
    # Neither Missionaries or Cannibals can be less than Zero
    # Number of Missionaries can't be less than the Number Cannibals
    if next_missionaries != 0 and next_missionaries < next_cannibals:
        areMoreCannibals = True
    # Number of Missionaries or Cannibals in the current state can't be less than the ones in the next state
    if next_missionaries > missionaries_limit or next_cannibals > cannibals_limit:
        isLimitExceeded = True
    # Number of Missionaries can't be less of Cannibals on the other side
    if next_missionaries != missionaries_limit and (
            (missionaries_limit - next_missionaries) < (cannibals_limit - next_cannibals)):
        areMoreCannibals = True

    if isLessThanZero or areMoreCannibals or isLimitExceeded:
        return False
    else:
        return True


class CannibalMissionaryTree:
    '''
    __init__: Declares how the tree will be initialized
        :arg
        [list] start_state = (No. Cannibals, No. Missionaries, Boat Position)
        Note.
            No. Cannibals on Initial side of the River
            No. Missionaries on Initial side of the River
            For Boat Position 1=Initial side of the River, 0=Another Side of the River
        [list] goal state = ()
    '''

    def __init__(self, current_state=(3, 3, 1), limits=(3, 3)):
        self.current_state = current_state
        self.__current_cannibals = current_state[0]
        self.__current_missionaries = current_state[1]
        self.__current_boat_position = current_state[2]
        self.__limits = limits

    '''
    Definition of getters and setters
    '''

    def get_cannibals(self):
        return self.__current_cannibals

    def get_missionaries(self):
        return self.__current_missionaries

    def get_boat_position(self):
        return self.__current_boat_position

    def print_current_state(self):
        print('Current State is: ', self.current_state)

    def get_successor_states(self):
        safe_next_states = []
        missionary = self.get_missionaries()
        cannibal = self.get_cannibals()
        boat_position = self.get_boat_position()
        total_next_state = get_after_carry_states(self.current_state)
        for state in total_next_state:
            if is_state_safe(self.current_state, state, self.__limits):
                safe_next_states.append(tuple(state))
        return safe_next_states

    def print_successor_states(self):
        print("Successor states are:", self.get_successor_states())


class Node:
    def __init__(self, state, parent=None, children=None):
        self.__state = state
        self.__parent = parent
        self.__children = children

    def get_state(self):
        return self.__state

    def get_children(self):
        return self.__children

    def get_parent(self):
        return self.__parent

    def __str__(self):
        nodeInformation = "\n_________________________\n"
        nodeInformation += "Node Information is:"
        nodeInformation += "\nState: {:s}"
        nodeInformation += "\nParent: {:s}"
        nodeInformation += "\nChildren: {:s}"
        nodeInformation = nodeInformation.format(str(self.get_state()), str(self.get_parent()),
                                                 str(self.get_children()))
        return nodeInformation

    def update_children(self):
        problem = CannibalMissionaryTree(self.get_state())
        self.__children = problem.get_successor_states()


class Solution:
    def __init__(self, start_state, goal_state):
        self.frontier = []
        self.explored = []
        self.start_state = start_state
        self.goal_state = goal_state
        self.nodes_visited = 0
        self.path = []

    def get_frontier_elements(self):
        element_list = []
        for element in self.frontier:
            element_list.append(element.get_state())
        return element_list

    def get_explored_elements(self):
        element_list = []
        for element in self.explored:
            element_list.append(element.get_state())
        return element_list

    def get_current_iteration_info(self):
        message = "\n________________________________\n"
        message += "Iteration No."
        message += str(self.nodes_visited)
        message += "\nFrontier is:\n"
        message += str(self.get_frontier_elements())
        message += "\nExplored is:\n"
        message += str(self.get_explored_elements())
        return message

    def get_node_backchain(self, end_node):
        return_path = []
        while end_node:
            return_path.append(end_node.get_state())
            end_node = end_node.get_parent()
        return_path.reverse()
        return return_path

    def bfs_search(self):
        solutionFound = False
        # Initialize Node with the Start State Information
        initial_node = Node(self.start_state)
        initial_node.update_children()

        # Start the frontier information
        self.frontier.append(initial_node)
        # "Initial node is: \n"
        # print(initial_node)
        # print("\n")
        checking_set = set()  # Initialize empty set to perform the checking easier

        while self.frontier:
            # print("\nFrontier is:\n")
            # print(self.get_frontier_elements())
            # print("\nExplored is:\n")

            # print(self.get_explored_elements())

            # print(self.get_current_iteration_info())
            # Get the first frontier Node to read
            frontier_node = self.frontier.pop(0)
            # print(frontier_node)
            # Update the Frontier and the Explored Lists
            self.explored.append(frontier_node)
            self.nodes_visited += 1
            checking_set.add(tuple(frontier_node.get_state()))

            # Check if Node is Goal State
            if frontier_node.get_state() == self.goal_state:
                solutionFound = True
                print("\nSolution Found using BFS Search at ...",self.nodes_visited)
                print(self.get_node_backchain(frontier_node))
                return True

            # Append successors to the frontier list
            children_frontier_node = frontier_node.get_children()
            for child in children_frontier_node:
                child_t = tuple(child)
                if child_t in checking_set:
                    continue
                else:
                    new_node = Node(state=child, parent=frontier_node, children=None)
                    new_node.update_children()
                    self.frontier.append(new_node)
        return solutionFound

    def dfs_search(self):
        solutionFound = False
        # Initialize Node with the Start State Information
        initial_node = Node(self.start_state)
        initial_node.update_children()

        # Start the frontier information
        self.frontier.append(initial_node)
        # "Initial node is: \n"
        # print(initial_node)
        # print("\n")
        checking_set = set()  # Initialize empty set to perform the checking easier

        while self.frontier:
            # print(self.get_current_iteration_info())
            # Get the first frontier Node to read
            frontier_node = self.frontier.pop(0)
            # print(frontier_node)
            # Update the Frontier and the Explored Lists
            self.explored.append(frontier_node)
            self.nodes_visited += 1
            checking_set.add(tuple(frontier_node.get_state()))

            # Check if Node is Goal State
            if frontier_node.get_state() == self.goal_state:
                solutionFound = True
                print("\nSolution Found using DFS Search at...", self.nodes_visited)
                print(self.get_node_backchain(frontier_node))
                return True

            # Append successors to the frontier list
            children_frontier_node = frontier_node.get_children()
            for child in children_frontier_node:
                child_t = tuple(child)
                if child_t in checking_set:
                    continue
                else:
                    new_node = Node(state=child, parent=frontier_node, children=None)
                    new_node.update_children()
                    self.frontier.insert(0, new_node)
        return solutionFound
