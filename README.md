# river-crossing-problem
In this repository I want to try to resolve the river crossing riddle about the 3 cannibals and missionaries using DFS and BFS algorithms.

--- 

## Description of the problem
In repository an implementation of the BFS and DFS for solving the missionaries and cannibals problem.

### The problem
In the missionaries and cannibals problem, consists on: 
1. Three missionaries and three cannibals must cross a river using a boat 
2. The boat can carry at most two people.
3. If there are missionaries present on the any side of the bank, they cannot be outnumbered by cannibals (if they were, the cannibals would eat the missionaries).
4. The boat cannot cross the river by itself with no people on board.

> Source
> [Wikipedia](https://en.wikipedia.org/wiki/Missionaries_and_cannibals_problem)

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

