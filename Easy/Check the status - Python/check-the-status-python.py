#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

# Function to check value and 
# return accordingly
def check_status(a, b, flag):
    c = 0
    if a<0 and b<0 and flag == True:
        c = 1
    elif flag == False:
        if (a<0 and b>=0) or (a>=0 and b<0):
            c = 1
    return c == 1
    
    
    

#{ 
 # Driver Code Starts.

# Driver Code
def main():
    
    # Testcase input
    testcases = int(input())
    
    # Looping through testcases
    while(testcases > 0):
        a = int(input())
        b = int(input())
        flag = input()
        
        if(flag == "True"):
            flag = True
        else:
            flag = False
        
        if(check_status(a, b, flag) is True):
            print ("True")
        else:
            print ("False")
        
        testcases -= 1
 
if __name__ == '__main__':
    main()
# } Driver Code Ends