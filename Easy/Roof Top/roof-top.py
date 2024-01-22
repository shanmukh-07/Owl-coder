#User function Template for python3

class Solution:
    
    #Function to find maximum number of consecutive steps 
    #to gain an increase in altitude with each step.
    def maxStep(self,A, N):
        l = []
        c = 0
        for i in range(1,N):
            if A[i-1]<A[i]:
                c+=1
            else:
                l.append(c)
                c = 0
        if c>0:
            l.append(c)
        if len(l) == 0:
            return 0
        return max(l)
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



    
def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            ob=Solution()
            print(ob.maxStep(A,N))
            
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends