def fun(arr,mid,K):
    c = 1
    s = 0
    for i in range(len(arr)):
        s += arr[i]
        if s > mid:
            c += 1 
            s = arr[i]
    if c<=K:
        return True
    return False
            
        
n,K = map(int,input().split())
arr = list(map(int,input().split()))
m = max(arr)
s = sum(arr)
while m<=s:
    mid = (m+s)//2
    if fun(arr,mid,K):
        ans = mid
        s = mid-1
    else:
        m = mid+1
print(ans)