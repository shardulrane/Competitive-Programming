from collections import Counter


def solve():
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    i = 0
    ans1 = float('inf')
    while (i <= n):
        x, y = 0, 0
        d = Counter(l[:i])
        d1 = Counter(l[i:])
        for j in d:
            if (d[j] > 1):
                x += d[j]
        for j in d1:
            if (d1[j] > 1):
                y += d1[j]
        if (i == 0):
            c = k + y
        elif (i == n):
            c = k + x
        else:
            c = 2 * k + x + y

        ans1 = min(c, ans1)
        i += 1

    a = set()
    p = 1
    for i in l:
        if i in a:
            a = {i}
            p += 1
        else:
            a.add(i)

    ans2 = p * k

    ans = min(ans1, ans2)
    print(ans)


for _ in range(int(input())):
    solve()
