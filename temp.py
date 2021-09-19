labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
graph = [
         [0, 0, 0, 0, 1, 1, 1, 0, 1, 0],
         [0, 0, 0, 0, 1, 0, 1, 1, 0, 1],
         [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
         [1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
         [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 1, 0, 0, 0, 0, 0]
        ]

# =======================
# Adds a node to the frontier if, and only if it is not contained in the frontier
# or the list of explored nodes.
# =======================
def add(successor, frontier, explored, type):
  new  = True
  # Revises if the node is already contained in the frontier
  for node in frontier:
    if node[0] == successor[0]:
      new = False
  # Revises if the node is already contained in the list of explored nodes
  if (new):
    for node in explored:
      if node[0] == successor[0]:
        new = False
  # If the node is not contained in the frontier or the list of explored nodes, it is added to the frontier
  if (new):
    if (type == "bfs"):
      frontier.append(successor)
    else:
      frontier.insert(0, successor)    
  return frontier

# =======================
# Formats the solution (not really needed, but helps the solution to be undestood).
# =======================
def format(parent, explored, solution):  
  if (parent != None):    
    for node in explored:      
      if node[0] == parent:
        return format(node[1], explored, parent + " -> " + solution)
  return solution

# =======================
# Implements BFS and DFS
# =======================
def search(frontier, explored, graph, labels, goal, type):
  # Sanity check in case the initial state is a goal one
  if (frontier[0] == goal):
      print(format(node[1], explored, node[0]) + ", with cost = " + str(node[2]))
      return True
  # As long as there are nodes in the frontier
  while (frontier):    
    # Extracts the first node from the frontier
    node = frontier.pop(0)    
    # Inserts the node into the list of explored nodes
    explored.append(node)    
    # Finds the index of the label in the node
    index = labels.index(node[0])
    # Creates the successors of the node and, if the successors are not contained in the frontier or the list of explored nodes, it is inserted into the frontier (FIFO)
    row = graph[index]    
    for i in range(len(row)):
      # If there is an edge going out from node
      if row[i]:
        # Creates a successor
        successor = (labels[i], node[0], node[2] + row[i])
        # If the successor is a goal state, the search finishes
        if (goal == successor[0]):                    
          print(format(node[0], explored, successor[0]) + ", with cost = " + str(successor[2]))
          return True
        # If the successor is not a goal state, the successor is added to the frontier
        frontier = add(successor, frontier, explored, type)
  # If the frontier is empty, no solution was found
  print("No solution found.")
  return False

frontier = [("H", None, 0)]
explored = []

search(frontier, explored, graph, labels, "D", "bfs")

frontier = [("H", None, 0)]
explored = []

search(frontier, explored, graph, labels, "D", "dfs")