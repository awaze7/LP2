import sys

class Graph():
    def __init__(self,vertices):
        self.V=vertices
        self.graph=[[0 for column in range(vertices)]
                    for row in range(vertices)]
    
    def printMST(self,parent): #to print the constructed MST stored in parent[]
        total_cost = 0  #to store the total ----weight of the MST
        print("Edge\tWeight")
        for i in range(1,self.V):
            print(parent[i],"-",i,"\t",self.graph[i][parent[i]])
            total_cost+=self.graph[i][parent[i]]
        print("Total Cost of MST:", total_cost)
    
    def minKey(self,key,mstSet): #to find the vertex with min distance from the set of vertices not yet included 
        min=sys.maxsize
        
        for v in range(self.V):
            if key[v]<min and mstSet[v]==False:
                min=key[v]
                min_index=v
        
        return min_index
        
    
    def primMST(self):
        key=[sys.maxsize]*self.V #Key values used to pick min weight edge
        
        parent=[None]*self.V #to store constructed MST
        
        key[0]=0
        
        mstSet=[False]*self.V  #keeps track of vertices already included in MST
        
        parent[0]=-1 #as 0 is taken as root node in MST
        
        for cout in range(self.V):
            
            #picks min dist vertex from set of vertices not yet visited,for first iteration is u is equal to src
            u=self.minKey(key,mstSet)
            
            mstSet[u]=True # to include the min dist vertex in the MST set
            
            for v in range(self.V):
                #graph[u][v] is non-zero and vertex v is not included yet and key[v] greater than weight of u-v
                if self.graph[u][v]>0 and mstSet[v]==False and key[v]>self.graph[u][v]:
                    key[v]=self.graph[u][v]
                    parent[v]=u
                    
        self.printMST(parent)
            
        

if __name__=='__main__':
    g=Graph(5)
    g.graph=[[0, 2, 0, 6, 0],
               [2, 0, 3, 8, 5],
               [0, 3, 0, 0, 7],
               [6, 8, 0, 0, 9],
               [0, 5, 7, 9, 0]]
    g.primMST()
