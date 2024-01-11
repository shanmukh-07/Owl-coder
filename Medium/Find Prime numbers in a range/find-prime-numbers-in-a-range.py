#User function Template for python3

class Solution:        
    def primeRange(self,M,N):
        l = [1]*(N+1)
        l[0] = 0
        l[1] = 0
        for i in range(2,int(N**0.5)+1):
            if l[i] == 1:
                for j in range(i*i,N+1,i):
                    l[j] = 0
        ll = []
        for i in range(M,N+1):
            if l[i] == 1:
                ll.append(i)
        return ll
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        M,N=map(int,input().strip().split(" "))
        ob=Solution()
        ans=ob.primeRange(M,N)
        for i in ans:
            print(i,end=" ")
        print()    
# } Driver Code Ends