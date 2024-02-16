class Solution:
    def firstRepeated(self,arr, n):
        d = {}
        m = float('+inf')
        for i in range(n):
            if arr[i] not in d:
                d[arr[i]] = i+1
            else:
                m = min(m,d[arr[i]])
        if m == float("+inf"):return -1
        return m
#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.firstRepeated(arr, n))
# } Driver Code Ends