
class Solution:
    def isMaxHeap(self,arr,n):
        d = {}
        c = 1
        for i in arr:
            if c >= n:
                break
            d[i] = [arr[c]]
            c += 1
            if c >= n:
                break
            d[i].append(arr[c])
            c += 1
        f = 0
        for i,j in d.items():
            if max(j) > i:
                f = 1
            if f == 1:
                return 0
        return 1
        
        
            
 # Driver Code Starts
if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]
        ob=Solution()
        print(int(ob.isMaxHeap(arr,n)))
# } Driver Code Ends