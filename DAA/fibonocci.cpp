#include<iostream>
using namespace std;

int feb(int n){
    if(n==0)return 0;

    if(n==1)return 1;

    return feb(n-1)+feb(n-2);
}

int main(){

    int n,choice;
    int a,b,c;

    while(choice<3){

        cout<<"1.Non-recursive Fibonacci";
        cout<<"\n2.Recursive Fibonacci";
        cout<<"\nExit";
        cout<<"\nEnter your choice:";

        cin>>choice;

        switch(choice){
            case 1:
                a = 0;
                b = 1;

                cout<<"Enter no of terms:";
                cin>>n;

                for(int i=0;i<n;i++){
                    cout<<a<<" ";
                    c=a+b;
                    a = b;
                    b = c;
                }
                cout<<endl;
                break;
            
            case 2:
                cout<<"Enter no of terms:";
                
                cin>>n;

                for(int i=0;i<n;i++){
                    cout<<feb(i)<<" ";
                }
                cout<<endl;
                break;
            
            case 3:
                cout<<"Exiting.....";
                break;
            
            default:
                cout<<"Enter valid choice";
        }
    }
    return 0;
}