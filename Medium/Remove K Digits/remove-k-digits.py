class Solution:
    def removeKdigits(self, s, k):
        st = []#0
        if len(s)<=k:
            return 0
        for i in s:
            while st and k>0 and st[-1]>i:
                st.pop()
                k-=1
            st.append(i)
        while k:
            st.pop()
            k-=1
        # return st,k
        st = "".join(st).lstrip("0")
        return st if st else "0"
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()
        K = int(input())

        obj = Solution()

        ans = obj.removeKdigits(S, K)

        print(ans)


# } Driver Code Ends