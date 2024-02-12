#User function Template for python3

class Solution:
    def sequence(self, n):
        m = 10**9+7
        s = 0
        tmp = 1
        for i in range(1,n+1):
            val = 1
            k = i
            while k>0:
                val = (val*tmp)%m
                tmp += 1
                k-=1
            s = (s%m + val%m)%m
        return s
        
        
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        print(ob.sequence(N))
# } Driver Code Ends