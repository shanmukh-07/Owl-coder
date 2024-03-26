#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

# return 1 in case of True and 0 in case of False
class Solution:
    def isAdditiveSequence(self, n):
        def fun(n):
            return len(n) == 1 or n[0] != '0'
        for i in range(1,len(n)-1):
            if not fun(n[:i]):
                continue
            for j in range(i+1,len(n)):
                if not fun(n[i:j]):
                    continue
                n1 = int(n[:i])
                n2 = int(n[i:j])
                k = j
                while k < len(n):
                    n3 = n1+n2
                    n3s = str(n3)
                    if not n.startswith(n3s,k):
                        break
                    k += len(n3s)
                    n1,n2 = n2,n3
                    if k == len(n):
                        return 1
        return 0
        
        

#{ 
 # Driver Code Starts.
        
if __name__ == "__main__":
    sol = Solution()
    t = int(input())
    for _ in range(t):
        s = input()
        print(sol.isAdditiveSequence(s))

# } Driver Code Ends