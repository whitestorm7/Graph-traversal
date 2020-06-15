class Graph:
    def __init__(self,edge):
        self.__edge=edge
        self.__adjlist={}
    def add_adj_list(self):
        
        for i in edge:
        
            if i[0] not in self.__adjlist:
                self.__adjlist[i[0]]=[]
            if i[1] not in self.__adjlist:
                self.__adjlist[i[1]]=[]
            self.__adjlist[i[0]].append(i[1])
            
            self.__adjlist[i[1]].append(i[0])
            
    def print_adj_list(self):
        for i in self.__adjlist:
            print(i,end=" ")
            for j in self.__adjlist[i]:
                print("->"+str(j),end =" ")
            print()
    def dfs(self,start):
        i=start
        stack=[]
        stack.append(i)    
        while(True):
            t=self.__adjlist[i]
            z=False
            for j in t:
                if j not in stack:
                    q=0
                    i=j
                    stack.append(j)
                    z=True
                    break   
            if j in stack and z==False:
                q=q-1
                if (-q)> len(stack):
                    break
                i=stack[q]
        print(stack)
    
            
        

edge=[[1,4],[1,2],[4,3],[3,10],[3,9],[3,2],[2,5],[2,7],[2,8],[5,7],[5,6],[5,8],[8,7]]
g=Graph(edge)    
g.add_adj_list()
g.print_adj_list()
g.dfs(1)

