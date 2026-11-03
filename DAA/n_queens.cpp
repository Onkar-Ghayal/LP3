#include<iostream>
using namespace std;

int n;
int mat[20][20];


void printChess(){
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            cout<<mat[i][j]<<" ";
        }
        cout<<endl;
    }
}

bool isSafe(int row ,int col){
    
    for(int i=0;i<n;i++){
        if(mat[i][col]==1){
            return false;
        }
    }

    for(int i=row-1,j=col-1;i>=0 && j>=0;i--,j--){
        if(mat[i][j]==1){
            return false;
        }
    }

    for(int i=row-1,j=col+1;i>=0 && j<n;i--,j++){
        if(mat[i][j]==1){
            return false;
        }
    }
    return true;
}

bool n_queen(int row){

    if(row==n){
        return true;
    }

    for(int col=0;col<n;col++){
        if(isSafe(row,col)){

            mat[row][col]=1;

            if(n_queen(row+1)){
                return true;
            }

            mat[row][col]=0;
        }
    }
    return 0;
}

int main(){

    cout<<"Enter Size of chess board:";
    cin>>n;

    if(n<1 || n>20){
        cout<<"Enter valid size (1 to 20)";
        return 0;
    }

    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            mat[i][j]=0;
        }
    }

    mat[0][0]=1;

    if(n_queen(1)){
        cout<<"Final n_queen chess Board"<<endl;
        printChess();
    }
    else{
        cout<<"Not valid chess Board";
    }

    return 0;
}

