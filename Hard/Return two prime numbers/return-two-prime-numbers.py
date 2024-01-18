#User function Template for python3

class Solution:
    def primeDivision(self, N):
        def fun(n):
            if n<2:
                return False
            for i in range(2,int(n**0.5)+1):
                if n%i == 0:
                    return  False
            return True
        i = 1
        j = N-1
        l = []
        while i <= j:
            if fun(i) and fun(j):
                l.append((i,j))
            i+=1
            j-=1
        return l[0]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        p1, p2 = ob.primeDivision(N)
        print(p1,end=" ")
        print(p2)
# } Driver Code Ends