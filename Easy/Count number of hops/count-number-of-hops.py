#User function Template for python3

class Solution:
    #Function to count the number of ways in which frog can reach the top.
    def countWays(self,n):
        m = 10**9+7
        l = [0]*(n+2)
        l[0] = 1
        l[1] = 1
        l[2] = 2
        for i in range(3,n+1):
            l[i] = (l[i-1]%m + l[i-2]%m + l[i-3]%m)%m
        return l[n]%m


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