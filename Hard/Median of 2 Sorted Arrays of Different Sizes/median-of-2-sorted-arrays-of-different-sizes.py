#User function Template for python3

class Solution:
    def MedianOfArrays(self, array1, array2):
        a = sorted(arr1+arr2)
        l = len(a)
        if l%2 != 0:
            return a[l//2]
        b = a[l//2]
        c = a[l//2 - 1]
        d = (b+c)/2
        if d == int(d):
            return int(d)
        return d


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):
        m = input()
        arr1=[int(x) for x in input().split()]
        n = input()
        arr2=[int(x) for x in input().split()]
        
        
        ob = Solution()
        print(ob.MedianOfArrays(arr1,arr2))

# } Driver Code Ends