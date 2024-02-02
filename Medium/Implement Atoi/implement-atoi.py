class Solution:
    def atoi(self,s):
        for i in range(1,len(s)):
            if not s[i].isdigit():
                return -1
        return int(s)
#{ 
 # Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        string = input().strip();
        ob=Solution()
        print(ob.atoi(string))
# } Driver Code Ends