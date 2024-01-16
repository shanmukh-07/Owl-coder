#User function Template for python3

class Solution:
    def reverseWords(self, s):
        l = s.split(".")
        ll = []
        for i in l:
            ll.append(i[::-1])
        return ".".join(ll)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.reverseWords(s)
        print(ans)
# } Driver Code Ends