#User function Template for python3

class Solution:
    def inSequence(self, A, B, C):
        d = B-A
        if A == B:
            return 1
        if d == 0 and C == 0:
            return 1
        if d<0 and C<0:
            if d%C == 0:
                return 1
        elif d>0 and C>0:
            if d%C == 0:
                return 1
        return 0

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        A, B, C = [int(x) for x in input().split()]
        
        ob = Solution();
        print(ob.inSequence(A, B, C))
# } Driver Code Ends