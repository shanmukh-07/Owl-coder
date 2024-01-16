#User function Template for python3

def rotate(matrix): 
    l = []
    for i in matrix:
        l.append(i[::-1])
    ll = list(zip(*l))
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i][j] = ll[i][j]
    return matrix


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t = int(input())
	for _ in range(t):
		N=int(input())
		arr=[int(x) for x in input().split()]
		matrix=[]

		for i in range(0,N*N,N):
			matrix.append(arr[i:i+N])

		rotate(matrix)
		for i in range(N): 
			for j in range(N): 
				print(matrix[i][j], end =' ') 
			print() 
        

# } Driver Code Ends