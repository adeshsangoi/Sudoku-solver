# Sudoku-solver
Sudoku solver using vertex coloring 

Vertex Coloring concept is used to solve the sudoku.
Vertex Coloring - In a given graph, no 2 adjascent vertices can have the same color.

Lets consider the 81 number blocks in a 3 X 3 sudoku as 81 nodes of a graph. 
Whenever 2 same blocks cant have the same number, an edge is formed between them.
Hence a particular node is connected to all nodes in its row and its column and in its 3X3 grid.
And then we use vertex coloring algorithm which will ensure no 2 adjascent nodes get the same value.
We will use backtracking if the number given to any node exceeds 9

How to Run the code:
  python3 sudoku_solver.py
  Mention number of entries given in table
  Mention an entry as row_num column_num value ( Sample inputs are given in file input 17 and input 21)

