//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution {
public:
    long long int killinSpree(long long int n)
    {
        int i = 1;
        int c = 0;
        while(1){
            if(i*i<=n){
                c++;
                n-=i*i;
            }
            else{
                break;
            }
            i++;
        }
        return c;
    }
};


//{ Driver Code Starts.

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        long long int n; cin>>n;
        Solution obj;
        long long int ans = obj.killinSpree(n);
        cout<<ans<<"\n";
    }
    return 0;
}

// } Driver Code Ends