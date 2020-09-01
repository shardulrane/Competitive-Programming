import sys
sys.setrecursionlimit(50000)
from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
        self.f=0
    def addEdge(self, u, v):
        self.graph[u].append(v)
    def dfs(self, i, visited):
        visited[i]=True
        for j in self.graph[i]:
            if not visited[j]:
                self.dfs(j, visited)
        self.f=i
        
    def mother(self, n, x=-1):
        visited=[False]*(n+1)
        visited[0]=True
        if x!=-1:
            self.dfs( x, visited)
        else:
            for i in range(1, n+1):
              if(not visited[i]):
                    self.dfs( i, visited)
            
        return [self.f, visited] 
        
        
for _ in range(int(input())):
    p, q =list(map(int, input().split()))
    g1=Graph()
    g2=Graph()
    for i in range(q):
        a,b=list(map(int, input().split()))
        g1.addEdge(a,b)
        g2.addEdge(b,a)
    
    x=g2.mother(p)
    x=x[0]
    #print(x)
    z=g2.mother(p,x)
    z=z[1]
    #print(z)
    if(z.count(True)!=p+1):
        print(0)
    else:
        y=g1.mother(p, x)
        y=y[1]
        print(y.count(True)-1)