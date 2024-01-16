#User function Template for python3

class Solution:
    #Function to count number of ways to reach the nth stair.
    def countWays(self,n):
        if n == 1:
            return 1
        a = 1
        b = 1
        for i in range(n-1):
            c = a+b
            a = b
            b = c
        m = 10**9 + 7
        return c%m


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
sys.setrecursionlimit(10**6)

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        ob=Solution()
        print(ob.countWays(m))

# } Driver Code Ends