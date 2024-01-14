#User function Template for python3

class Solution:
    def findNth(self,N):
        t = 1
        r = 0
        b = 9
        while(N>0):
            r = r+(N%b)*t
            N = N//b
            t = t*10
        return r


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t=int(input())
for i in range(0,t):
    n=int(input())
    obj=Solution()
    s=obj.findNth(n)
    print(s)
# } Driver Code Ends