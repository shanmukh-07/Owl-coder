#User function Template for python3

class Solution:
    def sumOfSubsets(self, n):
    	s = n*(n+1)//2
    	return s*(1<<(n-1))


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        print(ob.sumOfSubsets(N))
# } Driver Code Ends