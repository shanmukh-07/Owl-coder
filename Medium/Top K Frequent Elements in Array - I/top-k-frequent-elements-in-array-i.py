class Solution:
	def topK(self, nums, k):
		d = {}
		for i in nums:
		    if i not in d:
		        d[i] = 1
		    else:
		        d[i] += 1
		l = []
		for i,j in d.items():
		    l.append([j,i])
		l.sort(reverse = True)
		a = []
		c = 0
		for i,j in l:
		    c+=1
		    a.append(j)
		    if c == k:
		        return a
#{ 
 # Driver Code Starts
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	a = list(map(int, input().strip().split()))
    	n = a[0]
    	nums = a[1:]
    	k = int(input().strip())
    	obj = Solution()
    	ans = obj.topK(nums, k)
    	for i in ans:
    		print(i, end = " ")
    	print()
    	
# } Driver Code Ends