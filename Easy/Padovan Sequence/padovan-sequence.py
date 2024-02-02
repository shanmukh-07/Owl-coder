#User function Template for python3

class Solution:
    def padovanSequence(self, n):
        m = 10**9 + 7
        if n<=2:return 1
        return (self.padovanSequence(n-2)%m+self.padovanSequence(n-3)%m)%m


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.padovanSequence(n))
# } Driver Code Ends