from collections import OrderedDict
class Solution:
    def removeDuplicates(self, arr):
        return list(OrderedDict.fromkeys(arr))


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().removeDuplicates(arr)
        for i in range(len(res)):
            print(res[i], end=" ")
        print('')


# } Driver Code Ends