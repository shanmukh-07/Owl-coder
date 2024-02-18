#User function Template for python3

class Solution:
    def Solve(self, n, a):
        # d = {}
        # for i in a:
        #     if i not in d:
        #         d[i] = 1
        #     else:
        #         d[i] += 1
        # l = []
        # for i,j in d.items():
        #     if j > n//3:
        #         l.append(i)
        # if len(l) == 0:return -1
        # return l
        c = n//3
        s = set()
        for i in a:
            if a.count(i) > c:
                s.add(i)
        l = list(s)
        if len(l) == 0:return [-1]
        return l
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        ob = Solution()
        res = ob.Solve(n, a)
        for val in res:
            print(val, end = ' ')
        print()
# } Driver Code Ends