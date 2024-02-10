#User function Template for python3
class Solution:
	def subsetSums(self, arr, N):
		l = []
		for i in range(2**N):
		    s = 0
		    for j in range(N):
		        if (i>>j)&1:
		            s += arr[j]
		    l.append(s)
		return sorted(l)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends