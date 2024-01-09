#User function Template for python3

class Solution:
    def asteroidCollision(self, N, a):
        s = []
        for i in a:
            while s and s[-1] > 0 and i < 0:
                if s[-1] + i < 0:  
                    s.pop()
                elif s[-1] + i > 0:
                    break
                else:
                    s.pop()
                    break
            else: 
                s.append(i)        
        return s
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        asteroids = list(map(int, input().split()))
        ob = Solution()
        res = ob.asteroidCollision(N, asteroids)
        for val in res:
            print(val, end = ' ')
        print()
# } Driver Code Ends