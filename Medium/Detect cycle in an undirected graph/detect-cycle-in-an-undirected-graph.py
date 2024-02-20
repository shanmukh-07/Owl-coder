from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		v = [0]*V
		def fun(node,prev):
		    v[node] = 1
		    for i in adj[node]:
		        if v[i] and i != prev:
		            return 1
		        if not v[i]:
		            if fun(i,node):
		                return 1
		    return 0
		
		for i in range(V):
		    if v[i] == 0:
		        if fun(i,i) == 1:
		            return 1
		return 0
		        
		
#{ 
 # Driver Code Starts

if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends