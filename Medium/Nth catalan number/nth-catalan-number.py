import math
class Solution:
    def findCatalan(self, n : int) -> int:
        s1 = math.factorial(2*n)
        s2 = math.factorial(n+1)
        s3 = math.factorial(n)
        m = 10**9 + 7
        return (s1//(s2*s3))%m
        



#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        obj = Solution()
        res = obj.findCatalan(n)
        
        print(res)
        

# } Driver Code Ends