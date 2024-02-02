#User function Template for python3

class Solution:
    def pattern(self, N):
        if N<1:return [N]
        l = []
        while N>0:
            l.append(N)
            N-=5
        t = l[::-1]
        l.append(t[0]-5)
        return l+t
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        ans = ob.pattern(N)
        for i in ans:
            print(i, end = " ")
        print()
# } Driver Code Ends