for _ in range(int(input())):
    n11, k = input().split()
    k = int(k)
    arr = map(int, input().split())
    listt = []
    for i in arr:
        if k % i == 0:
            listt.append(i)
    listt.sort(reverse=True)
    if len(listt) == 0:
        print(-1)
    else:
        print(listt[0])