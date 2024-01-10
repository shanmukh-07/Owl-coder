#User function Template for python3

class Solution:
	def PowMod(self, x, n, m):
	    res = 1
	    while n!=0:
	        if n%2 != 0:
	            n = n-1
	            res = (res%m * x%m)
	        else:
	            n = n//2
	            x = x%m * x%m
	    return res%m


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		x, n , m = input().split()
		x = int(x)
		n = int(n) 
		m = int(m)
		ob = Solution();
		ans = ob.PowMod(x, n, m)
		print(ans)
# } Driver Code Ends