#User function Template for python3

class Solution:
    def fibSum (self,N):
        m = 10**9+7
        a = 0
        b = 1
        sl = 0
        for i in range(N):
            c = (a%m+b%m)%m
            a = b
            b = c
            sl+=a
        return sl%m


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        print(ob.fibSum(N))
# } Driver Code Ends