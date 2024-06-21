class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self,A,N,X):
        if X == 0:
            return -1
        m = 0
        for i in A:
            if i<=X:
                m = max(m,i)
        if m == 0:
            return -1
        return A.index(m)


#{ 
 # Driver Code Starts
#Initial Template for Python 3


import math


def main():
        T=int(input())
        while(T>0):
            
            NX=[int(x) for x in input().strip().split()]
            N=NX[0]
            X=NX[1]

            A=[int(x) for x in input().strip().split()]
            
            obj = Solution()
            print(obj.findFloor(A,N,X))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends