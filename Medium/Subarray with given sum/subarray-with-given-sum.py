#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n,s):
        ps = 0
        ind = 0
        for i in range(n):
            ps += arr[i]
            while ps > s and i > ind:
                ps -= arr[ind]
                ind += 1
            if ps == s:
                return [ind+1,i+1]
        return [-1]
        
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Endshttps://media.geeksforgeeks.org/img-practice/fab-icon-new.gif