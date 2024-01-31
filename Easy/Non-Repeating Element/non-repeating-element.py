#User function Template for python3
from collections import OrderedDict
class Solution:
    def firstNonRepeating(self, arr, n): 
        d = OrderedDict()
        for i in arr:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for i,j in d.items():
            if j == 1:
                return i
                break
        return 0



#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import defaultdict 

for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.firstNonRepeating(arr, n))
    
# } Driver Code Ends