#User function Template for python3

class Solution:
    def Anagrams(self, words, n):
        l = []
        for i in words:
            x = "".join(sorted(i))
            l.append([x,i])
        d = {}
        for i,j in l:
            if i not in d:
                d[i] = []
                d[i].append(j)
            else:
                d[i].append(j)
        s = []
        for i in d.values():
            s.append(i)
        return s

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n= int(input())
        words=input().split()
        
        ob = Solution()
        ans = ob.Anagrams(words,n)
        
        for grp in sorted(ans):
            for word in grp:
                print(word,end=' ')
            print()

# } Driver Code Ends