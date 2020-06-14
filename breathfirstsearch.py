class Graph:
    def __init__(self,nodes,edge):
        self.__nodes=nodes
        self.__edge=edge
        self.__adjlist={}
    def add_adj_list(self):
        for i in nodes:
            k=[]
            self.__adjlist[i]=k
        for i in edge:
            self.__adjlist[i[0]].append(i[1])
           
            self.__adjlist[i[1]].append(i[0])
            
    def print_adj_list(self):
        for i in self.__adjlist:
            print(i,end=" ")
            for j in self.__adjlist[i]:
                print("->"+str(j),end =" ")
            print()
    def bfs(self,start):
        stack=[]
        
        i=0
        while(len(stack)!=len(nodes)):
            for j in self.__adjlist[start]:
                if start not in stack:
                    stack.append(start)
                if start in stack and j not in stack:
                    stack.append(j)
            i=i+1
            start=stack[i]
            
        print(stack)
nodes=[1,2,3,4,5,6,7,8,9,10]
edge=[[1,4],[1,2],[4,3],[3,10],[3,9],[3,2],[2,5],[2,7],[2,8],[5,7],[5,6],[5,8],[8,7]]
g=Graph(nodes,edge)    
g.add_adj_list()
g.print_adj_list()
g.bfs(1)
