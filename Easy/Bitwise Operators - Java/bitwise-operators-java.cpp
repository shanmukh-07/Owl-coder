//{ Driver Code Starts
// Initial Template for C++

#include <iostream>
using namespace std;

// Function Prototype
void bitWiseOperation(int, int, int);


// } Driver Code Ends
// User function Template for C++

// Function to perform bitwise manipulations
// a, b and c are input integers
void bitWiseOp(int a, int b, int c) {
    int d,e,f,g;
    float h;
    d = a^a;
    e = c^b;
    f = a&b;
    g = c|(d);
    h = ~e;
    cout<<d<<endl;
    cout<<e<<endl;
    cout<<f<<endl;
    cout<<g<<endl;
    cout<<h<<endl;
}

//{ Driver Code Starts.

// Driver code to test above function
int main() {

    int t;
    cin >> t;

    while (t--) {
        int a, b, c;
        cin >> a >> b >> c;

        bitWiseOp(a, b, c);
    }

    return 0;
}
// } Driver Code Ends