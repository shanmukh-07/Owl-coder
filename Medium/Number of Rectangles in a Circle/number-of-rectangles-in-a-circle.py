#User function template for Python

class Solution:
    def rectanglesInCircle(self,r):
        c = 0
        d = 2*r
        for i in range(1,d):
            for j in range(1,d):
                if i*i+j*j <= 4*r*r:
                    c += 1
        return c
































#{ 
 # Driver Code Starts
#Initial Template for Python

import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.rectanglesInCircle(N)
        print(ans)

# } Driver Code Ends