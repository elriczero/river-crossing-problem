from tree_definition import CannibalMissionaryProblem
from tree_definition import Node
from tree_definition import Solution

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    initialProblem = CannibalMissionaryProblem((3, 3, 1))
    print(initialProblem)

    solutionBFS = Solution((3, 3, 1), (0, 0, 0))
    solutionBFS.bfs_search()
    solutionDFS = Solution((3, 3, 1), (0, 0, 0))
    solutionDFS.dfs_search()


