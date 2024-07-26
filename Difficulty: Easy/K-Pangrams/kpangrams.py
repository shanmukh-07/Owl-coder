#User function Template for python3
class Solution:
    def kPangram(self,string, k):
        l = []
        for i in string:
            if i.islower():
                l.append(i)
        if len(l)<26:
            return False
        ll = len(set(l))
        if ll+k < 26:
            return False
        return True


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        string = input()
        K = int(input())
        ob = Solution()
        a = ob.kPangram(string, K)
        if a:
            print("true")
        else:
            print("false")

# } Driver Code Ends