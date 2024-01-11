#User function Template for python3
class Solution:
    def leastPrimeFactor (self, n):
        def fun(n):
            p = float("inf")
            i = 2
            while i*i<=n:
                while n%i == 0:
                    p = min(p,i)
                    n = n//i
                i+=1
            if n>1:
                p = min(p,n)
            return p
        l = []
        for i in range(n+1):
            if i == 1:
                l.append(1)
            else:
                l.append(fun(i))
        return l
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.leastPrimeFactor(n)
		for i in range(1, n+1):
			print(ans[i], end = " ")
		print()

# } Driver Code Ends