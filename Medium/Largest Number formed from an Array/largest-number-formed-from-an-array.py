#User function Template for python3
class Solution:

	def printLargest(self, n, arr):
	    l = []
	    for i in arr:
	        l.append((i*10,i))
	    l.sort(reverse = True)
	    s = ""
	    for i,j in l:
	        s += j
        return s


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import functools

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(str, input().strip().split()))
        ob = Solution()
        ans = ob.printLargest(n, arr)
        print(ans)
        tc -= 1

# } Driver Code Ends