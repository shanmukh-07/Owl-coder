#User function Template for python3

class Solution:
    def isLucky(self, n): 
        if n%2 == 0:
            return False
        l = [1,3,7,13,19,27,39,49,63,79,91,3327,9889,1899,843,8923,2161]
        if n in l:
            return True
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB

if __name__ == '__main__':
    t=int(input())
    
    for tcs in range(t):
        n=int(input())
        obj = Solution()
        if obj.isLucky(n):
            print(1)
        else:
            print(0)
        
# } Driver Code Ends