#User function Template for python3
class Solution:

	def constructLowerArray(self,arr, n):
		lst = []
		l1 = []
		for i in range(n-1,-1,-1):
		    l = 0
		    r = len(lst)-1
		    while l<=r:
		        m = (l+r)//2
		        if lst[m] > arr[i]:
		            r = m-1
		        elif lst[m]<arr[i]:
		            l = m+1
		        else:
		            r = m-1
		    lst.insert(l,arr[i])
		    l1.append(l)
		return l1[::-1]
		    

#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.constructLowerArray(arr, n)
        for x in ans:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends