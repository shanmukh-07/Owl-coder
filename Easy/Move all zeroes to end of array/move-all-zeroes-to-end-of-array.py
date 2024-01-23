#User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr, n):
    	l = []
    	for i in arr:
    	    if i!=0:
    	        l.append(i)
    	c = arr.count(0)
    	for i in range(c):
    	    l.append(0)
    	for i in range(n):
    	    arr[i] = l[i]
    	    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
# } Driver Code Ends