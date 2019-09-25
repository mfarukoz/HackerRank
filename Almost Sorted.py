def almostSorted():
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    arr2=arr[:]
    arr2.sort()
    check1=[]
    check2=[]
    for i in range(len(arr)):
        if arr[i]!=arr2[i]:
            check1.append(i+1)
        if 0<i<len(arr)-1:
            if arr[i-1]<arr[i]>arr[i+1] or arr[i-1]>arr[i]<arr[i+1]:
                check2.append(i+1)
    if len(check1)==0:
        print('yes')
    elif len(check1)==2:
        print('yes')
        print('swap',check1[0],check1[1])
    elif len(check2)==2 and arr[check2[0]-2]<arr[check2[0]-1] and arr[check2[1]-1]<arr[check2[0]]:
        print('yes')
        print('reverse',check2[0],check2[1])
    else:
        print('no')

almostSorted()
