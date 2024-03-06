#User function Template for python3

class Solution:
    def search(self, pattern, text):
        l = []
        l1 = len(text)
        l2 = len(pattern)
        for i in range(l1-l2+1):
            if text[i:i+l2] == pattern:
                l.append(i+1)
        # print(l)
        return l

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        for value in ans:
            print(value,end = ' ')
        print()
# } Driver Code Ends