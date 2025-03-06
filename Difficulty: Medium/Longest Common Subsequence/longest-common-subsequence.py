#User function Template for python3

class Solution:
    
    #Function to find the length of longest common subsequence in two strings.
    def lcs(self,s1,s2):
        m = len(s1)
        n = len(s2)
        l = [[0]*(n+1) for i in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s1[i-1] == s2[j-1]:
                    l[i][j] = l[i-1][j-1]+1
                else:
                    l[i][j] = max(l[i-1][j],l[i][j-1])
        return l[m][n]

#{ 
 # Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        s1 = str(input())  # Take first string as input
        s2 = str(input())  # Take second string as input
        ob = Solution()
        # Call the lcs function and print the result
        print(ob.lcs(s1, s2))
        print("~")

# } Driver Code Ends