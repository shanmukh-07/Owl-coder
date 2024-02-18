#User function Template for python3

class Solution:
    def maxValue(self, arr, n):
        l1,l2 = [],[]
        for i in range(n):
            l1.append(arr[i]+i)
            l2.append(-arr[i]+i)
        mx1 = max(l1)
        mn1 = min(l1)
        mx2 = max(l2)
        mn2 = min(l2)
        return max(mx1-mn1,mx2-mn2)
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.maxValue(arr,N))
# } Driver Code Ends