//{ Driver Code Starts
//Initial Template for C++
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution{   
    void solve(vector<int>&sieve){
        sieve[0]=0;
        sieve[1]=0;
        for(int i=2;i*i<=100000;i++){
            if(sieve[i]==1){
                for(int j=i*i;j<=100000;j+=i){
                    sieve[j]=0;
                }
            }
        }
    }
public:
    int solve(int num1,int num2)
    {   
      vector<int>sieve(100001,1);
      solve(sieve);
      queue<int>q;
      q.push(num1);
      int level=0;
      while(!q.empty()){
          int s=q.size();
          for(int i=0;i<s;i++){
              int num=q.front();
              q.pop();
              if(num==num2){
                  return level;
              }
              string str1=to_string(num);
              for(int i=0;i<4;i++){
                  string str2=str1;
                  for(int j='0';j<='9';j++){
                      if(i==0&j=='0') continue;
                      str2[i]=j;
                      int new_num=stoi(str2);
                      if(sieve[new_num]==1){
                          q.push(new_num);
                          sieve[new_num]=0;
                      }
                  }
              }
          }
          level++;
      }
      return -1;
    }
};


//{ Driver Code Starts.
signed main()
{
  int t;
  cin>>t;
  while(t--)
  {
      int num1,num2;
      cin>>num1>>num2;
      Solution obj;
      int answer=obj.solve(num1,num2);
      cout<<answer<<endl;
  }
}
// } Driver Code Ends