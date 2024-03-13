# Your task is to complete this function

class Solution:
    def matrixDiagonally(self,mat):
        l = [mat[0][0]]
        i = 0
        s = 0
        n = len(mat)
        d = 1
        for s in range(1,2*n-1):
            for i in range(max(s+1-n,0),min(n,s+1)):
                if d == 1:
                    l.append(mat[i][s-i])
                else:
                    l.append(mat[s-i][i])
            d *= -1
        return l

#{ 
 # Driver Code Starts
# Driver Program
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        a = Solution().matrixDiagonally(matrix)
        for x in a:
            print(x,end=' ')
        print('')
# Contributed by: Harshit Sidhwa
# } Driver Code Ends