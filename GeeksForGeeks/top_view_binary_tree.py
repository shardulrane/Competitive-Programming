

'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
import collections
def verticalOrder(root):
    if root is None:
        return
    que=[]
    hd=dict()
    m={}
    que=[root]
    hd[root]=0
    m[0]=[root.data]
    while len(que)>0:
        temp=que.pop(0)
        if temp.left:
            que.append(temp.left)
            hd[temp.left]=hd[temp]-1
            hdn=hd[temp.left]
            if m.get(hdn) is None:
                m[hdn]=[]
            m[hdn].append(temp.left.data)
        if temp.right:
            que.append(temp.right)
            hd[temp.right]=hd[temp]+1
            hdn=hd[temp.right]
            if m.get(hdn) is None:
                m[hdn]=[]
            m[hdn].append(temp.right.data)
    op=[]
    mord=collections.OrderedDict(sorted(m.items())) 
    for i in mord.values():
        op.append(i[0]) 
    return op


def topView(root):
    op1=verticalOrder(root)
    for i in range(0,len(op1)):
        print(op1[i],end=" ")
        
    



#{ 
#  Driver Code Starts
#Initial Template for Python 3


#Contributed by Sudarshan Sharma

from collections import deque
import queue 

class Node: 
    # Constructor to create a new Node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
  
def make_tree():
    n=int(input())
    l=list(map(str,input().split()))
    head=None
    q=deque()
    i=0
    while(n>0):
        a,b,c=l[i],l[i+1],l[i+2]
        if(not head):
            head=Node(int(a))
            q.append(head)
        pick=q[0]
        q.popleft()
        if(c=='L'):
            pick.left=Node(int(b))
            q.append(pick.left)
        n=n-1
        if(not n):
            break
        a,b,c=l[i+3],l[i+4],l[i+5]
        if(c=='R'):
            pick.right=Node(int(b))
            q.append(pick.right)
        i=i+6
        n=n-1
    return head
            

if __name__ == '__main__':
    t=int(input())
    for _ in range(0,t):
        root=make_tree()
        topView(root)
        print()

# } Driver Code Ends