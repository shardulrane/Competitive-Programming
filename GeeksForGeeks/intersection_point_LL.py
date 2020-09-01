'''
	Your task is to return the point of intersection
	in two linked list, connected in y shaped form.
	
	Function Arguments: head_a, head_b (heads of both the lists)
	
	Return Type: NODE present at the point of intersection, or -1 if no common point.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
def intersetPoint(a,b):
    la=0
    tempa=a
    tempb=b
    while a!=None:
        la+=1
        a=a.next
    lb=0  
    while b!=None:
        lb+=1
        b=b.next
    d=abs(la-lb)
    if la>lb:
        for i in range(0,d):
            tempa=tempa.next
        while tempa!=None or tempb!=None:
            if tempa==tempb:
                return tempa
            tempa=tempa.next
            tempb=tempb.next
    else:
        for i in range(0,d):
            tempb=tempb.next
        while tempa!=None or tempb!=None:
            if tempa==tempb:
                return tempb
            tempa=tempa.next
            tempb=tempb.next
    return -1
    



#{ 
#  Driver Code Starts
#Initial Template for Python 3

#Contributed by : Nagendra Jha

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        temp=None
    
    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            self.temp = self.head
            return
        else:
            self.temp.next = new_node
            self.temp = self.temp.next

if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        x,y,z = map(int,input().strip().split())
        a = LinkedList()  # create a new linked list 'a'.
        b = LinkedList()  # create a new linked list 'b'.
        nodes_a = list(map(int, input().strip().split()))
        nodes_b = list(map(int, input().strip().split()))
        nodes_common = list(map(int, input().strip().split()))

        for x in nodes_a:
            node=Node(x)
            a.append(node)  # add to the end of the list

        for x in nodes_b:
            node=Node(x)
            b.append(node)  # add to the end of the list

        for i in range(len(nodes_common)):
            node=Node(nodes_common[i])
            a.append(node)  # add to the end of the list a
            if i== 0:
                b.append(node)  # add to the end of the list b, only the intersection
        if intersetPoint(a.head,b.head) == -1:
            print(-1)
        else:
            print(intersetPoint(a.head,b.head).data) #print data present at the node.

# } Driver Code Ends