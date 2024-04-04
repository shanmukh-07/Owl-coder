#User function Template for python3

class Solution:
    #Function to find sum of all possible substrings of the given string.
    def sumSubstrings(self,s):
        m = 10**9 + 7
        l = len(s)
        prev = int(s[0])
        ans = prev
        for i in range(1,l):
            tmp = (int(s[i])*(i+1)+10*prev)%m
            ans = (ans+tmp)%m
            prev = tmp
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

import sys
sys.setrecursionlimit(10**6)

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        s = str(input())
        ob=Solution()
        print(ob.sumSubstrings(s))
# } Driver Code Ends