#User function Template for python3
class Solution:
    def smallestNumber (self, S, D):
        if D*9 < S:
            return -1
        n = 10**(D-1)
        s = str(n)
        l = list(s)
        l = l[::-1]
        S-=1
        for i in range(len(l)):
            l[i] = int(l[i])
            if S>0:
                if S-l[i] >= 9:
                    l[i] += 9
                    S -= 9
                else:
                    l[i] += S
                    S = 0
        l = l[::-1]
        n = 0
        for i in l:
            n = n*10 + i
        return n


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S,D=map(int,input().strip().split(" "))

        ob = Solution()
        print(ob.smallestNumber(S,D))
# } Driver Code Ends