#User function Template for python3

class Solution:
    #Complete this function
    def power(self,N,R):
        m = 10**9+7
        res = 1
        while R!=0:
            if R%2 != 0:
                R-=1
                res = res%m * N%m
            else:
                R = R//2
                N = N%m * N%m
        return res%m

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
    
    T=int(input())
    
    while(T>0):
        
        N=input()
        R=N[::-1]
        
        ob=Solution();
        ans=ob.power(int(N),int(R))
        print(ans)
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends