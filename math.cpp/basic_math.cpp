#include<bits/stdc++.h>
using namespace std;
int main(){
    #ifndef ONLINE_JUDGE
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    #endif
    int n;
    cin>>n;
    vector<int>v;
    int p = 1;
    for(int i=1;i<=n;i++){
        p*=i;
    }
    while(p!=0){
        int a = p%10;
        v.insert(v.begin(),a);
        p = p/10;
    }
    for(auto i:v){
        cout<<i;
    }
    return 0;
}