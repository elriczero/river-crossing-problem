# river-crossing-problem
In this repository I want to try to resolve the river crossing riddle about the 3 cannibals and 3 missionaries using DFS and BFS algorithms.

--- 

## Description of the problem
### Overview 
In this repository will be an implementation of the BFS and DFS for solving the missionaries and cannibals problem.

> Three missionaries meet three hungry cannibals at the edge of a river. </br> Next  to them is a boat that can take a  maximum of two people. </br> They must find  a sequence of crossings that allow both them and the cannibals to cross the river safely.

### Limitations
1. Three missionaries and three cannibals must cross a river using a boat.
2. The boat can carry at most two people.
3. If there are missionaries present on the any side of the bank, they cannot be outnumbered by cannibals (if they were, the cannibals would eat the missionaries).
4. The boat cannot cross the river by itself with no people on board.

> Source
> [Wikipedia](https://en.wikipedia.org/wiki/Missionaries_and_cannibals_problem)

## Formulation
### States
An ordered sequence of three numbers representing the number of  missionaries, cannibals, and boats that are in the starting bank of the  river.

### Initial State
The state where the three missionaries and cannibals are at the  starting bank of the river (3, 3, 1).

### Actions
Each boat crossing reduces the number of people on the river side 
where the crossing originates and increases it on the destination side.

### Goal Test
The current state is (0, 0, 0).

### Path Cost
Each step costs one unit. The path cost is the sum of all the steps in the 
path.

---
### Solution reference
The correct way to resolve this problem, will be following steps:
| Iteration | Cannibals | Missionaries | Boat |
|-----------|-----------|--------------|------|
| 1         | 3         | 3            | 0    |
| 2         | 2         | 2            | 1    |
| 3         | 2         | 3            | 0    |
| 4         | 0         | 3            | 1    |
| 5         | 1         | 3            | 0    |
| 6         | 1         | 1            | 1    |
| 7         | 2         | 2            | 0    |
| 8         | 2         | 0            | 1    |
| 9         | 3         | 0            | 0    |
| 10        | 1         | 0            | 1    |
| 11        | 2         | 0            | 0    |
| 12        | 0         | 0            | 1    |

