#User function Template for python3


class Solution:
	def threeDivisors(self, query, q):
		def fun(n):
		    if n<2:return False
		    for i in range(2,int(n**0.5)+1):
		        if n%i == 0:
		            return False
		    return True
        
        l = []
        for i in query:
            c = 0
            for j in range(2,int(i**0.5)+1):
                if fun(j):
                    c += 1
            l.append(c)
        return l

#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		q = int(input())
		query = []
		for _ in range(q):
			query.append(int(input()))
		
		ob = Solution()
		ans = ob.threeDivisors(query,q)
		for a in ans:
			print(a)

# } Driver Code Ends