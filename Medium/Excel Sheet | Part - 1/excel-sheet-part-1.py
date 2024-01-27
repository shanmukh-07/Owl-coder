#User function Template for python3

class Solution:
    def ExcelColumn(self, N):
        s = ""
        while N>0:
            a = N%26
            if a == 0:
                s += "Z"
                N = (N//26)-1
            else:
                s += chr(a-1+ord("A"))
                N = N//26
        return s[::-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for tcs in range(t):
        n=int(input())
        ob=Solution()
        print(ob.ExcelColumn(n))

# } Driver Code Ends