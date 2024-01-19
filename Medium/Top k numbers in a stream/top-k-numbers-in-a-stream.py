#User function Template for python3
from sortedcontainers import SortedSet
class Solution:
    def kTop(self,a, N, K):
        ans=[]
        m={}
        st=SortedSet()
        for i in a:
            if i in m and m[i]>0:
                st.remove((-m[i],i))
            m[i]=m.get(i,0)+1
            st.add((-m[i],i))
            temp=[]
            t=0
            for c,v in st:
                if t==k:
                    break
                temp.append(v)
                t+=1
            ans.append(temp)
            
        return ans

#{ 
 # Driver Code Starts


t=int(input())
for _ in range(0,t):
    n,k=list(map(int,input().split()))
    a=list(map(int,input().split()))
    ob = Solution()
    ans=ob.kTop(a,n,k)
    for line in ans:
        print(*line)



# } Driver Code Ends