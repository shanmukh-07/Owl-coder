#User function Template for python3

class Solution:
    def series(self, n):
        l = [0,1]
        m = 10**9+7
        for i in range(2,n+1):
            t = l[-1]+l[-2]
            l.append(t%m)
        return l
        
        
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        result = ob.series(N)
        print(*result)
# } Driver Code Ends