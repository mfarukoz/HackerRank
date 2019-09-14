def pickingNumbers(a):
    c=[]
    a.sort()
    for i in a:
        if i not in a:
            continue
        b=list(filter(lambda j: abs(i-j)<=1,a))
        a=[k for k in a if k not in b]
        c.append(len(b))
    print(max(c))
n = int(input().strip())
a = list(map(int, input().rstrip().split()))
result = pickingNumbers(a)


