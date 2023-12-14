import sys
    
fh = open('IterativeDFS_output.txt', 'w')

class IterativeDFS:
   
    def __init__(self, nodes_count):
        self.size = nodes_count
        self.neighbors = [[] for i in range(nodes_count)]

    def add_edge(self, u, v):
        self.neighbors[u].append(v)

    def dfs_iterative(self, s, visited):
        stack = [s]
        preorder = []
        postorder = []
        parent = []


        while len(stack) > 0:
            u = stack[-1]
            visited_neigh = 0  
            if not visited[u]:
                visited[u] = True
                preorder.append(u)

            for v in (self.neighbors[u]):
                if visited[v]:
                    visited_neigh = visited_neigh + 1
                if not visited[v]:
                    stack.append(v)
                    parent.append((u, v))
                    break
            if visited_neigh == len(self.neighbors[u]):
                stack.pop()
                postorder.append(u)
        
        
        
        for x in preorder:
            #print(x)
            fh.write("%s\n"%str(x))
        #print("============")
        for i, y in enumerate(postorder):
            if i == len(postorder) - 1:
                #print(y)
                fh.write("%s" % str(y))
            else:
                #print(y)
                fh.write("%s\n" % str(y))
        
        #fh.close()
        

    def dfs(self,order):
        visited = [False] * self.size
        #Fno=1
        for i in order:
            if not visited[i]:
                
                self.dfs_iterative(i, visited)  

input_filename = sys.argv[2]

with open(input_filename, "r") as file:
    lines=file.readlines()
    order=[]
    if lines:
        order.append(int(lines[-1]))
        for j in range(int(lines[0])):
            if j!=order[0]:
                order.append(j)
                
        G = IterativeDFS(int(lines[0])) # No of nodes
        for line in lines[2:-1]:
            line = line.split()
            
            
            G.add_edge(int(line[0]), int(line[1]))


G.dfs(order)
