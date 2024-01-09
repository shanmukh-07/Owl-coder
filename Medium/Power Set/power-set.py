#User function Template for python3

class Solution:
	def AllPossibleStrings(self, s):
	    n = len(s)
	    l = []
		for i in range(2**n):
		    ss = ""
		    for j in range(n):
		        if (i>>j)&1:
		            ss += s[j]
		    l.append(ss)
		l.sort()
		l.pop(0)
		return l


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution();
		ans = ob.AllPossibleStrings(s)
		for i in ans:
			print(i, end = " ");
		print()
# } Driver Code Ends