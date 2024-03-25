#User function Template for python3
class Solution:
	def NBitBinary(self, n):
		l = []
		def fun(s,ln,z):
		    if ln == n:
		        l.append(s)
		        return
		    fun(s+"1",ln+1,z)
		    if ln-z > z:
		        fun(s+'0',ln+1,z+1)
		fun('1',1,0)
		return l
		        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()	
		answer = ob.NBitBinary(n)
		for value in answer:
			print(value,end=" ")
		print()


# } Driver Code Ends