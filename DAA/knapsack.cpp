#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cout<<"Enter Numbers of items:";
    cin>>n;

    int wt[n];
    int profit[n];

    cout<<"Enter Weights of items:";
    for(int i=0;i<n;i++){
        cin>>wt[i];
    }

    cout<<"Enter Profit of items:";
    for(int i=0;i<n;i++){
        cin>>profit[i];
    }

    int w ;
    cout<<"Enter Maximum Weight:";
    cin>>w;

    int dp[n+1][w+1];

    for(int i=0;i<=n;i++){
        for(int j = 0;j<=w;j++){
            if(i==0 || j==0){
                dp[i][j]=0;
            }
            else if(wt[i-1]<=j){
                dp[i][j] = max(profit[i-1]+dp[i-1][j-wt[i-1]],dp[i-1][j]);
            }
            else{
                dp[i][j] = dp[i-1][j];
            }
        }
    }

    cout<<"Maximum Profit:";
    cout<<dp[n][w];

    return 0;
}