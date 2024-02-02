#User function Template for python3

class Solution:
    def segregateElements(self, arr, n):
        ps,ng = [],[]
        for i in arr:
            if i > 0:
                ps.append(i)
            else:
                ng.append(i)
        l = ps+ng
        for i in range(n):
            arr[i] = l[i]
        return arr



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        ob.segregateElements(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends