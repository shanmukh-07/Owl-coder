#User function Template for python3

class Solution:

    #Function to perform case-specific sorting of strings.
    def caseSort(self,s,n):
        l = list(s)
        C,ci = [],[]
        S,si = [],[]
        for i in range(n):
            if s[i].isupper():
                C.append(s[i])
                ci.append(i)
            else:
                S.append(s[i])
                si.append(i)
        C.sort()
        S.sort()
        s1 = list(zip(C,ci))
        s2 = list(zip(S,si))
        for i,j in s2:
            l[j] = i
        for i,j in s1:
            l[j] = i
        return "".join(l)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n=int(input())
        s=str(input())
        print(Solution().caseSort(s,n))
# } Driver Code Ends