#User function Template for python3
import math
class Solution:
    def trailingZeroes(self, N):
    	c = 0
    	while N>4:
    	    c+=N//5
    	    N//=5
    	return c
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input()) 
        ob = Solution()
        ans = ob.trailingZeroes(N)
        print(ans)
# } Driver Code Ends