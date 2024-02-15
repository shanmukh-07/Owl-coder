#User function Template for python3

class Solution:
    def CamelCase(self,N,D,P):
        l = []
        for i in D:
            k = ""
            for j in i:
                if j.isupper():
                    k+=j
                    if P == k:
                        l.append(i)
                        break
        if len(l) == 0:return [-1]
        return l

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        Dictionary=list(map(str,input().split()))
        Pattern=input()
        ob=Solution()
        ans=ob.CamelCase(N,Dictionary,Pattern)
        ans.sort()
        for i in ans:
            print(i,end=" ")
        print()    
# } Driver Code Ends