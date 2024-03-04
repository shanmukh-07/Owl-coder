#User function Template for python3
class Solution:

	def checkTriplet(self,arr, n):
	    s = set(arr)
	    l = []
	    for i in s:
	        l.append(i**2)
	    arr = list(s)
	    for i in range(len(arr)):
	        for j in range(i+1,len(arr)):
	            a = arr[i]**2+arr[j]**2
	            if a in l:
	                return 1
	    return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.checkTriplet(arr, n)
        if ans:
            print("Yes")
        else:
            print("No")
        tc -= 1

# } Driver Code Ends