#User function Template for python3

class Solution:
    def maxProduct(self, arr, n):
        arr.sort()
        p,pp = 1,1
        p = arr[0]*arr[1]*arr[n-1]
        pp = arr[n-1]*arr[n-2]*arr[n-3]
        return max(p,pp)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.maxProduct(arr, n)
        print(ans)
        tc -= 1
# } Driver Code Ends