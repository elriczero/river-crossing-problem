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


def is_state_safe(current_state, next_state):
    # missionary_limit = limits[0]
    # cannibal_limit = limits[1]
    # Current State values
    current_missionaries = current_state[0]
    current_cannibals = current_state[1]
    # Next State Values
    next_missionaries = next_state[0]
    next_cannibals = next_state[1]
    if (
            # Neither Missionaries or Cannibals can be less than Zero
            next_missionaries < 0 or
            next_cannibals < 0 or
            # Number of Missionaries can't be less than the Number Cannibals
            (next_missionaries != 0 and next_missionaries < next_cannibals) or
            # Number of Missionaries or Cannibals in the current state can't be less than the ones in the next state
            current_missionaries < next_missionaries or
            current_cannibals < next_cannibals or
            # Number of Missionaries can't be less of Cannibals on the other side
            (
                    next_missionaries != current_missionaries and
                    ((current_missionaries - next_missionaries) < (current_cannibals - next_cannibals))
            )
    ):
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

    def __init__(self, current_state=[3, 3, 1]):
        self.current_state = current_state
        self.__current_cannibals = current_state[0]
        self.__current_missionaries = current_state[1]
        self.__current_boat_position = current_state[2]

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
            if is_state_safe(self.current_state, state):
                safe_next_states.append(state)
        return safe_next_states

    def print_successor_states(self):
        print("Succesor states are:", self.get_successor_states())


class Node:
    def __init__(self, state, parent=None, children=None):
        self.state = state
        self.__parent = parent
        self.__children = children

    def update_children(self):
        problem = CannibalMissionaryTree(self.state)
        self.children = problem.get_successor_states()

    def get_children(self):
        return self.__children

    def get_parent(self):
        return self.__parent


class Solution:
    def __init__(self, search_method, start_state, goal_state):
        self.frontier = []
        self.explored = []
        self.search_method = search_method  # Must be BFS or DFS
        self.start_state = start_state
        self.goal_state = goal_state

    def search(self):
        # Initialize Node with the Start State Information
        initial_node = Node(self.start_state)
        print("")
