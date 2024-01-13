#User function Template for python3


class Solution:
    def nextHappy (self, N):
        def fun(n):
            s = set()
            while 1:
                if n == 1:
                    return True
                elif n in s:
                    return False
                s.add(n)
                n = sum(int(i)**2 for i in str(n))
        t = N+1
        while 1:
            if fun(t):
                return t
            t += 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())

        ob = Solution()
        print(ob.nextHappy(N))
# } Driver Code Ends