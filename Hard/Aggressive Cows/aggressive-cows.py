#User function Template for python3

class Solution:
    def solve(self,n,k,stalls):
        def fun(stalls,dis,k):
            c = 1
            lc = stalls[0]
            for i in range(1,len(stalls)):
                if stalls[i]-lc >= dis:
                    c += 1
                    lc = stalls[i]
            if c>=k:
                return True
            return False
                    
        stalls.sort()
        l = 0
        h = stalls[n-1]-stalls[0]
        while l <= h:
            m = (l+h)//2
            if fun(stalls,m,k):
                l = m+1
            else:
                h = m-1
        return h


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n, k = list(map(int, input().split()))
        stalls = list(map(int, input().split()))
        ob = Solution()
        res = ob.solve(n, k, stalls)
        print(res)

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends