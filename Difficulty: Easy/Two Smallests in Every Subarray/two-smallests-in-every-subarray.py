class Solution:
    def pairWithMaxSum(self, arr):
        if len(arr)<2:
            return -1
        s = 0
        for i in range(len(arr)-1):
            s = max(s,arr[i]+arr[i+1])
        return s


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split("\n")

    t = int(data[0])
    lines = data[1:]

    for line in lines:
        s = list(map(int, line.strip().split()))
        solution = Solution()
        res = solution.pairWithMaxSum(s)
        print(res)

# } Driver Code Ends