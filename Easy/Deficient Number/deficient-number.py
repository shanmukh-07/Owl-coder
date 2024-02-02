#User function Template for python3
class Solution:
    def isDeficient (self, x):
        def fun(n):
            s = set()
            for i in range(1,int(n**0.5)+1):
                if n%i == 0:
                    s.add(i)
                    if n//i != i:
                        s.add(n//i)
            return sum(s)
        if fun(x) < 2*x:return "YES"
        return "NO"
             


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        x = int(input())
        
        ob = Solution()
        print(ob.isDeficient(x))
# } Driver Code Ends