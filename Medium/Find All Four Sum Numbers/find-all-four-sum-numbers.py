#User function Template for python3

# arr[] : int input array of integers
# k : the quadruple sum required
class Solution:
    def fourSum(self, arr, k):
        arr.sort()
        s=[]
        n=len(arr)
        for i in range(n-3):
            if i>0 and arr[i]==arr[i-1]:
                continue
            for j in range(i+1,n-2):
               if j>i+1 and arr[j]==arr[j-1]:
                   continue
               start=j+1;
               end=n-1;
               while(start<end):
                    newtarget=arr[i]+arr[j]+arr[start]+arr[end]
                    if newtarget==k:
                        s.append([arr[i],arr[j],arr[start],arr[end]])
                        while start<end and arr[start]==arr[start+1]:
                            start+=1
                        while start<end and arr[end]==arr[end-1]:
                            end-=1
                        start+=1
                        end-=1
                    elif newtarget<k:
                        start+=1
                    else:
                        end-=1
        return s  
#{ 
 # Driver Code Starts
#Initial Template for Python 3


#Main
if __name__=='__main__':
    t = int(input())
    while t:
        t-=1
        n, k=map(int,input().split())
        # print(n, k)
        a=list(map(int,input().strip().split()))[:n]
        # print(a)
        ob=Solution()
        ans=ob.fourSum(a, k)
        # print(ans)
        for v in ans:
            for u in v:
                print(u, end=" ")
            print("$", end="")
        if(len(ans)==0):
            print(-1, end="")
        print()
        
        

# } Driver Code Ends