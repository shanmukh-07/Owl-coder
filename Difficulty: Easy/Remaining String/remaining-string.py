#User function Template for python3
class Solution:
	def printString(self, s, ch, count):
		ss = ""
		c = 0
		for i in range(len(s)):
		    if s[i] == ch:
		        c += 1
		    if c == count:
		        ss += s[i+1:]
		        break
		return ss


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()
        ch = input()[0]
        count = int(input())
        ob = Solution()
        answer = ob.printString(s, ch, count)

        print(answer)

# } Driver Code Ends