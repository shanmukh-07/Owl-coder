class Solution:
    # Your task is to Complete this function
    # functtion should return an integer
    def maxDistance(self, arr):
        d = {}
        s = 0
        for i in range(len(arr)):
            if arr[i] in d:
                s = max(s,i-d[arr[i]])
            else:
                d[arr[i]] = i
        return s



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.maxDistance(arr))

# } Driver Code Ends