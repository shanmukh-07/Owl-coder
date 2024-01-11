#User function Template for python3

class Solution:
    def sieveOfEratosthenes(self, n):
    	l = [0]*(n+1)
    	l[0] = 1
    	l[1] = 1
    	for i in range(2,int(n**0.5)+1):
    	    if l[i] == 0:
    	        for j in range(i*i,n+1,i):
    	            l[j] = 1
    	ll = []
    	for i in range(n+1):
    	    if l[i] == 0:
    	        ll.append(i)
    	return ll


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sieveOfEratosthenes(N)
        for i in ans:
            print(i, end=" ")
        print()
# } Driver Code Ends