#User function Template for python3
class Solution:
	def countgroup(self,arr): 
		xor = 0
		n = len(arr)
		mod = 10**9 + 7
		for i in range(n):
		    xor ^= arr[i]
		if xor != 0:
		    return 0
		return ((2**(n-1))-1) % mod



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.countgroup(arr)
        print(res)
        t -= 1

# } Driver Code Ends