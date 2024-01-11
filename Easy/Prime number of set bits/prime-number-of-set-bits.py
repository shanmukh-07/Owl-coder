#User function Template for python3
class Solution:
	def primeSetBits(self, L, R):
		def fun(n):
		    if n<2:
		        return False
		    for i in range(2,int(n**0.5)+1):
		        if n%i == 0:
		            return False
		    return True
		def fun1(n):
		    c = 0
		    while n:
		        if n&1 == 1:
		            c += 1
		        n>>=1
		    if fun(c):
		        return 1
		    return 0
		s = 0
		for i in range(L,R+1):
		    s += fun1(i)
		return s



#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		L,R = input().split()
		L=int(L)
		R=int(R)
		ob = Solution();
		print(ob.primeSetBits(L,R))

# } Driver Code Ends