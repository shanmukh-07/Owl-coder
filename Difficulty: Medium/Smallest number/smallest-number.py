#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    def smallestNumber (self, S, D):
        if D*9 < S:
            return -1
        n = 10**(D-1)
        s = str(n)
        l = list(s)
        l = l[::-1]
        S-=1
        for i in range(len(l)):
            l[i] = int(l[i])
            if S>0:
                if S-l[i] >= 9:
                    l[i] += 9
                    S -= 9
                else:
                    l[i] += S
                    S = 0
        l = l[::-1]
        n = 0
        for i in l:
            n = n*10 + i
        return n




#{ 
 # Driver Code Starts.
# Position this line where user code will be pasted.

import sys
import math
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1

for _ in range(t):
    s = int(data[index])
    d = int(data[index + 1])
    index += 2
    ob = Solution()
    print(ob.smallestNumber(s, d))

# } Driver Code Ends