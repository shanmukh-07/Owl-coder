#User function Template for python3

class Solution:
    def isPerfectNumber(self, n):
        sm = 1
        for i in range(2,int(n**0.5)+1):
            if n%i == 0:
                sm += i
                if i != n//i:
                    sm += n//i
        return sm == n


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        ans = (ob.isPerfectNumber(N))
        if (ans):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends