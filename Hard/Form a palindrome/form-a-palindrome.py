#User function Template for python3

class Solution:
    def countMin(self, s):
        n = len(s)
        l = [[0]*n for i in range(n)]
        for i in range(n-1):
            if s[i] != s[i+1]:
                l[i][i+1] = 1
        for i in range(n-1,-1,-1):
            for j in range(i+2,n):
                if s[i] != s[j]:
                    l[i][j] = min(1+l[i+1][j],1+l[i][j-1])
                else:
                    l[i][j] = min(1+l[i+1][j],1+l[i][j-1],l[i+1][j-1])
        return l[0][n-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        Str = input()
        

        solObj = Solution()

        print(solObj.countMin(Str))
# } Driver Code Ends