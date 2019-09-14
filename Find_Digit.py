def findDigits(n):
    counter=0
    for i in n:
        if int(i)!=0 and int(n)%int(i)==0:
            counter+=1
    print(counter)
t = int(input())
for t_itr in range(t):
    n = input()
    result = findDigits(n)


