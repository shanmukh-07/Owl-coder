#User function Template for python3

class Solution:
    def maxVolume(self, perimeter, area):
        L = (perimeter - ((perimeter**2 - 24*area)**0.5))/12
        V = (perimeter*L**2-8*L**3)/4
        return V
        
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import math
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        perimeter, area = [int(x) for x in input().split()]

        ob = Solution()
        print('%.2f' % ob.maxVolume(perimeter, area))

# } Driver Code Ends