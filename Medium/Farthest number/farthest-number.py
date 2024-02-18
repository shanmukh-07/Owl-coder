#User function Template for python3

from bisect import bisect_left as bl
class Solution:
    def farNumber(self,n,arr):
        l = [-1]*n
        s = [0]*n
        s[n-1] = arr[-1]
        for i in range(n-2,-1,-1):
            s[i] = min(arr[i],s[i+1])
        for i in range(n-1):
            j = bl(s,arr[i],i+1)
            if j and s[j-1] < arr[i]:
                l[i] = j-1
            else:
                pass
        return l


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tcs=int(input())
    for _ in range(tcs):
        N=int(input())
        Arr=[int(x) for x in input().split()]
        
        ob = Solution()
        ans = ob.farNumber(N,Arr)
        
        for i in ans:
            print(i,end=" ")
        print()
# } Driver Code Ends