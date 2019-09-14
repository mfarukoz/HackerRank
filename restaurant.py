def restaurant(l, b):
    global gcd
    n=min([l,b])
    for i in range(n,0,-1):
        if l%i==0 and b%i==0:
            gcd=i
            break
    print(int((l*b)/(gcd**2)))
t = int(input())
for t_itr in range(t):
    lb = input().split()
    l = int(lb[0])
    b = int(lb[1])
    result = restaurant(l, b)
