'''
Function Arguments :
		@param  :m (boolean matrix of size n*n), n(no of rows and cols )
		@return : Integer
'''
def getId(arr,n):
    ans = -1
    for i in range(n):
        count = 0
        for j in arr[i]:
            
            if j == 0:
                count += 1
            else:
                break
        if count == n and ans == -1:
            ans = i
        elif count == n:
            return -1
    return ans


#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

#Contributed by :Shardul Rane

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        k = 0
        m = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(a[k])
                k+=1
            m.append(row)
        print(getId(m,n))
# } Driver Code Ends