from typing import List
from collections import deque
class Solution:
    def findShortestPath(self, mat : List[List[int]]) -> int:
        if not mat or not mat[0]:
            return -1
        n,m = len(mat),len(mat[0])
        dr = [(-1,0),(0,1),(1,0),(0,-1)]
        def fun(a,b):
            if mat[a][b] == 0:
                return True
            for da,db in dr:
                na,nb = a+da,b+db
                if 0 <= na < n and 0 <= nb < m and mat[na][nb] == 0:
                    return True
            return False
        qu = deque([(i,0,1) for i in range(n) if not fun(i,0)])
        v = [[False for _ in range(m)] for _ in range(n)]
        while qu:
            x,y,dist = qu.popleft()
            if y == m-1:
                return dist
            for dx,dy in dr:
                nx,ny = x+dx,y+dy
                if 0 <= nx < n and 0 <= ny < m and not v[nx][ny] and not fun(nx, ny):
                    v[nx][ny] = True  
                    qu.append((nx, ny, dist + 1))
        
        return -1   
            

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



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(2)
        
        
        mat=IntMatrix().Input(a[0], a[1])
        
        obj = Solution()
        res = obj.findShortestPath(mat)
        
        print(res)
        

# } Driver Code Ends