#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    def findMaxProduct(self, arr):
        def mx_ng(arr):
            ans = float("-inf")
            for i in arr:
                if i<0 and i>ans:
                    ans = i
            return ans
        zc = arr.count(0)
        if zc == len(arr):return 0
        p = 1
        l = 0
        z = False
        for i in arr:
            if i != 0:
                l += 1
                p *= i
            else:
                z = True
        if p<0 and l>1:
            m = mx_ng(arr)
            p //= m
        ans = 0 if z and p<0 else p
        if ans<0:
            return ans%(-10**9+7)
        elif ans>0:
            return ans%(10**9+7)
        else:
            return 0
        
        
        

#{ 
 # Driver Code Starts.
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        arr = list(map(int, data[index:index + n]))
        index += n
        solution = Solution()
        ans = solution.findMaxProduct(arr)
        results.append(ans)
    
    for result in results:
        print(result)
# } Driver Code Ends