//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;


class Matrix
{
public:
    template <class T>
    static void input(vector<vector<T>> &A,int n,int m)
    {
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                scanf("%d ",&A[i][j]);
            }
        }
    }
 
    template <class T>
    static void print(vector<vector<T>> &A)
    {
        for (int i = 0; i < A.size(); i++)
        {
            for (int j = 0; j < A[i].size(); j++)
            {
                cout << A[i][j] << " ";
            }
            cout << endl;
        }
    }
};


// } Driver Code Ends
class Solution {
  bool solve(unordered_map<int,vector<int>>&adj,vector<int>&vis,int src,int parent){
        vis[src]=1;
        for(auto it:adj[src]){
            if(!vis[it]){
                bool l=solve(adj,vis,it,src);
                if(l){
                    return true;
                }
            }else if(parent!=it){
                return true;
            }
        }
    }
  public:
    int isTree(int n, int m, vector<vector<int>> &adj) {
        unordered_map<int,vector<int>>adjlist;
        for(int i=0;i<adj.size();i++){
            adjlist[adj[i][0]].push_back(adj[i][1]);
            adjlist[adj[i][1]].push_back(adj[i][0]);
        }
        vector<int>vis(n,0);
        bool check=false;
        check=solve(adjlist,vis,0,-1);
        for(int i=0;i<n;i++){
            if(vis[i]==0){
                check=true;
            }
        }
        return check==true?0:1;
    }
};


//{ Driver Code Starts.

int main(){
    int t;
    scanf("%d ",&t);
    while(t--){
        
        int n; 
        scanf("%d",&n);
        
        
        int m; 
        scanf("%d",&m);
        
        
        vector<vector<int>> edges(m, vector<int>(2));
        Matrix::input(edges,m,2);
        
        Solution obj;
        int res = obj.isTree(n, m, edges);
        
        cout<<res<<endl;
        
    }
}

// } Driver Code Ends