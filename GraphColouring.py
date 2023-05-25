class Graph:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=[[0 for j in range(vertices)] for i in range(vertices)]
    
    def isSafe(self,v,colour,c):
        for i in range(self.V):
            if self.graph[v][i]==1 and colour[i]==c:
                return False
        return True
    
    def graphColourUtil(self,m,colour,v):
        if v==self.V:
            return True
        
        for c in range(1,m+1):
            if self.isSafe(v,colour,c)==True:
                colour[v]=c
                if self.graphColourUtil(m,colour,v+1)==True:
                    return True
                colour[v]=0
        
    def graphColouring(self,m):
        
        colour=[0]*self.V
        
        if self.graphColourUtil(m,colour,0)==None:
            return False
        
        print("Solution exit and following are the assigned colours: ")
#         for c in colour:
#             print(c,end=' ')
        for v in range(self.V):
            print("Vertex ", v, " is coloured with", colour[v])
        return True


g=Graph(4)
g.graph=[[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
m=3

g.graphColouring(m)
# Time Complexity: O(m^V). There is a total of O(m^V) combinations of colors. 
# Auxiliary Space: O(V). The recursive Stack of the graph coloring function will require O(V) space.
