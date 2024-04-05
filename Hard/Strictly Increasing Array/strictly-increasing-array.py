#User function Template for python3
from bisect import bisect_right
class Solution:
	def min_operations(self,nums):
		n = len(nums)
		l = [nums[0]]
		for i in range(1,n):
		    num = nums[i]-i
		    pos = bisect_right(l,num)
		    if pos == len(l):
		        l.append(num)
		    else:
		        l[pos] = num
		return n-len(l)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		ob = Solution();
		ans = ob.min_operations(nums)
		print(ans)
# } Driver Code Ends