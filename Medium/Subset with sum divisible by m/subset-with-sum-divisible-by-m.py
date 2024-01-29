#User function Template for python3

class Solution:
	def DivisibleByM(self, nums, m):
		c = 0
		l = len(nums)
		for i in range(2**l):
		    s = 0
		    for j in range(n):
		        if (i>>j)&1:
		            s += nums[j]
		    if s%m == 0 and s != 0:
		        c = 1
		        break
		return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split();
		n = int(n);
		m = int(m);
		nums = list(map(int, input().split()))
		ob = Solution();
		ans = ob.DivisibleByM(nums, m)
		print(ans)
# } Driver Code Ends