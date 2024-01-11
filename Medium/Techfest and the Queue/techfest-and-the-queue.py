class Solution:
    def sumOfPowers(self, a : int, b : int) -> int:
        def pf(n):
            s = 0
            while n%2 == 0:
                s += 1
                n//=2
            i = 3
            while i*i<=n:
                while n%i == 0:
                    s += 1
                    n//=i
                i += 2
            if n>2:
                s += 1
            return s
        ss = 0
        for i in range(a,b+1):
            ss += pf(i)
        return ss
        



#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=int(input())
        b=int(input())
        
        obj = Solution()
        res = obj.sumOfPowers(a,b)
        
        print(res)
        

# } Driver Code Ends