t=int(input())
while t>0:
    t-=1
    n=int(input())
    arr=[int(x) for x in input().split()]
    intervals=[]
    for i in range(0,len(arr)-1,2):
        temp=[]
        temp.append(arr[i])
        temp.append(arr[i+1])
        intervals.append(temp)
    intervals.sort(key=lambda x:x[0])
    #print(intervals)
    i=1
    while i<len(intervals):
        if intervals[i][0]<=intervals[i-1][1]:
            intervals[i-1][0]=min(intervals[i][0],intervals[i-1][0])
            intervals[i-1][1]=max(intervals[i][1],intervals[i-1][1])
            intervals.pop(i)
        else:
            i+=1
    for k in range(0,len(intervals)):
        ti=intervals[k]
        for j in range(0,len(ti)):
            print(ti[j],end=" ")
    print()
            
        
    