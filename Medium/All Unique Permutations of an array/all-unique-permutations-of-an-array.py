#User function Template for python3
from itertools import permutations
class Solution:
    def uniquePerms(self, arr, n):
        l = list(permutations(arr))
        d = {}
        for i in l:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        ll = [i for i in d.keys()]
        ll.sort()
        return ll
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        res = ob.uniquePerms(arr,n)
        for i in range(len(res)):
            for j in range(n):
                print(res[i][j],end=" ")
            print()
# } Driver Code Ends