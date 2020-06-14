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
    def dfs(self,start):
        boolean_list={}
        for i in self.__nodes:
            boolean_list[i]=False    
        i=start
        
        stack=[]
        stack.append(i)
        stack1=[]
        stack1.append(i)
        boolean_list[i]=True
        while(len(stack1)!=len(nodes)):
            t=self.__adjlist[i]
            z=False
            for j in t:
                
                if boolean_list[j]==False:
                    
                    i=j
                    boolean_list[j]=True
                    stack1.append(j)
                    stack.append(j)
                    
                    z=True
                    break
                
            if z==False:
                
                i=stack.pop()
        print(stack1)
    
            
        
nodes=[1,2,3,4,5,6,7,8,9,10]
edge=[[1,4],[1,2],[4,3],[3,10],[3,9],[3,2],[2,5],[2,7],[2,8],[5,7],[5,6],[5,8],[8,7]]
g=Graph(nodes,edge)    
g.add_adj_list()
g.print_adj_list()
g.dfs(1)

