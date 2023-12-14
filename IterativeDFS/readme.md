Project Description: The project implements a faithful iterative DFS with stack in linear time
such that
1.  each node enters the stack exactly once;
2.  the parent of a node is set once; and
3.  the same DFS forest and node order as the recursive DFS are returned.

The input and output are written through separate files to handle larger number of nodes and edges

Notes:

What if there are multiple disjoint components in a graph?

DFS-FOREST on a graph G will always start with some source node (In this case, it should start with the given input source node)
If there are multiple components in the graph and one iteration of DFS leaves some nodes unexplored, the next iteration should start with the first unexplored node (ordering of nodes is obvious [0 to n - 1])
This should automatically be handled if the ordering of the nodes if followed to check for the next unexplored node


Test Case Execution:

• The input file name will be given as a command line argument with the option -i or --input [See
below for example]
• Assume the file exists in the current directory where the program is located
• Output file must be named <input-file-name>_output.txt [See below for example]
• Output file must be created in the current directory where the program is located
See the following commands for python (but could be extrapolated for any other language) :
1 $ python3 dfs.py -i test_1.txt
2 $ python3 dfs.py --input test_1.txt
