#User function Template for python3


class Solution:
    def compareFrac (self, st):
        l = st.split(", ")
        a = eval(l[0])
        b = eval(l[1])
        if a > b:
            return l[0]
        elif a < b:
            return l[1]
        return "equal"



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import re

if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        str = input()
        print(ob.compareFrac(str))

# } Driver Code Ends