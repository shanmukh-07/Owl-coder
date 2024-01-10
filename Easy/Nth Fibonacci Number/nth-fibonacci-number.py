
class Solution:
    def nthFibonacci(self, n : int) -> int:
        if n == 1 or n == 2:
            return 1
        else:
            m = 10**9+7
            l = [0]*n
            l[0] = 1
            l[1] = 1
            for i in range(2,n):
                l[i] = (l[i-1]%m+l[i-2]%m)%m
            return l[-1]%m
#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        obj = Solution()
        res = obj.nthFibonacci(n)
        
        print(res)
        

# } Driver Code Ends