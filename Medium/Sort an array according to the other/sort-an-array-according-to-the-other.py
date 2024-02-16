#User function Template for python3

class Solution:
    def relativeSort (self,A1, N, A2, M):
        d = {}
        for i in A1:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        l,p = [],[]
        for i in A2:
            if i in d:
                for j in range(d[i]):
                    l.append(i)
                del d[i]
        for i,j in d.items():
            for k in range(j):
                p.append(i)
        p.sort()
        return l+p
        
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int (input ())
    while t > 0:
        n, m = list(map(int, input().split()))
        a1 = list(map(int, input().split()))
        a2 = list(map(int, input().split()))
        
        ob=Solution()
        a1 = ob.relativeSort (a1, n, a2, m)
        print (*a1, end = " ")
        
        print ()
        
        t -= 1

# } Driver Code Ends