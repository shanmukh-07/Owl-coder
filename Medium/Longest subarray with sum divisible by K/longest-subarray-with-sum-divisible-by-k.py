#User function Template for python3
class Solution:
	def longSubarrWthSumDivByK (self,arr,  n, k) : 
		d = {}
		d[0] = -1
		pre = 0
		ans = 0
		for i in range(n):
		    pre += arr[i]
		    if pre<=0:
		        pre += k
		    a = pre%k
		    if a in d:
		        m = i-d[a]
		        ans = max(ans,m)
		    else:
		        d[a] = i
	    return ans
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

	for _ in range(0,int(input())):
		n, K = map(int ,input().split())
		arr = list(map(int,input().strip().split()))
		ob = Solution()
		res = ob.longSubarrWthSumDivByK(arr, n, K)
		print(res)




# } Driver Code Ends