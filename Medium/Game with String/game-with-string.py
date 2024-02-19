#User function Template for python3

class Solution:
    def minValue(self, s, k):
        d = {}
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        l = [i for i in d.values()]
        l.sort()
        while k > 0:
            l[-1] = l[-1]-1
            k-=1
            l.sort()
        s = 0
        for i in l:
            s += i**2
        return s


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        k = int(input())
        
        ob = Solution()
        print(ob.minValue(s, k))
# } Driver Code Ends