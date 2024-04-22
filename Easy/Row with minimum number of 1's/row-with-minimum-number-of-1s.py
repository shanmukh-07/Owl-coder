#User function Template for python3

class Solution:
    def minRow(self,n,m,a):
        d = {}
        for i in range(n):
            c = a[i].count(1)
            if c not in d:
                d[c] = [i+1]
            else:
                d[c].append(i+1)
        m = min(d.keys())
        # print(d)
        return min(d[m])

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split(" "))
        A=[]
        for i in range(N):
            B=list(map(int,input().strip().split(" ")))
            A.append(B)
        ob=Solution()
        print(ob.minRow(N,M,A))
# } Driver Code Ends