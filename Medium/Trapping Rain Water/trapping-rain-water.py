
class Solution:
    def trappingWater(self, arr,n):
        p,s = [],[]
        mp,ms = 0,0
        for i in range(n):
            mp = max(mp,arr[i])
            p.append(mp)
        for j in range(n-1,-1,-1):
            ms = max(ms,arr[j])
            s.append(ms)
        s = s[::-1]
        fs = 0
        for i in range(n):
            fs += min(p[i]-arr[i],s[i]-arr[i])
        return fs


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()



# } Driver Code Ends