#User function Template for python3

class Solution:

    def firstRepChar(self, s):
        d = {}
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 2
            if d[i]>1:
                return i
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        print(solObj.firstRepChar(s))
# } Driver Code Ends