#User function Template for python3

class Solution:
    ##Complete this function
    def searchInSorted(self,arr, N, K):
        # l = 0
        # h = N-1
        # while l<=h:
        #     m = (l+h)//2
        #     if arr[m] == K:
        #         return 1
        #     elif K>arr[m]:
        #         l = m+1
        #     else:
        #         h = m-1
        # return -1
        def fun(arr,l,h,t):
            if l>h:return -1
            m = (l+h)//2
            if arr[m] == t:
                return 1
            elif t>arr[m]:
                return fun(arr,m+1,h,t)
            else:
                return fun(arr,l,m-1,t)
        return fun(arr,0,N-1,K)
            





#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
	t = int(input())
	for _ in range(t):
		NK = input().strip().split()
		N = int(NK[0])
		K = int(NK[1])
		A = [ int(x) for x in input().strip().split() ]
		ob=Solution()
		print(ob.searchInSorted(A,N,K))

# } Driver Code Ends