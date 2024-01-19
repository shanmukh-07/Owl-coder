#User function Template for python3

class Solution:
    def getLastDigit(self, a, b):
        a = int(a)
        b = int(b)
        if b%4 == 0 and b>4:
            c = 4
        else:
            c = b%4
        return (a**c)%10

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        a,b=map(str,input().split())
        
        ob = Solution()
        print(ob.getLastDigit(a,b))
# } Driver Code Ends