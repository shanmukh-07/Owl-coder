#User function Template for python3

class Solution:
    def largestSubsquare(self, n, a):
        v = [[0]*n for _ in range(n)]
        h = [[0]*n for _ in range(n)]
        s = 0
        for i in range(n):
            for j in range(n):
                if a[i][j] == 'X':
                    v[i][j] = 1 if i == 0 else v[i-1][j]+1
                    h[i][j] = 1 if j == 0 else h[i][j-1]+1
        for i in range(n):
            for j in range(n):
                val = min(v[i][j],h[i][j])
                while val > s:
                    if v[i][j-val+1] >= val and h[i-val+1][j] >= val:
                        s = val
                    val -= 1
        return s
                    
                    
                    
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        a=[]
        for i in range(n):
            s=list(map(str,input().strip().split()))
            a.append(s)
        ob=Solution()
        print(ob.largestSubsquare(n,a))
# } Driver Code Ends