#User function Template for python3


class Solution:
    def find(self, arr, n, x):
        l = []
        if x not in arr:
            return [-1,-1]
        a = arr.index(x)
        l.append(a)
        b = arr.count(x)
        l.append(a+(b-1))
        return l


#{ 
 # Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ob = Solution()
    ans=ob.find(arr,n,x)
    print(*ans)
# } Driver Code Ends