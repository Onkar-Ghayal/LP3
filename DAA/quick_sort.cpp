#include<bits/stdc++.h>
using namespace std;

int partition(int arr[],int start,int end){

    int indx = start-1;

    int pivot = arr[end];

    for(int i=start;i<end;i++){
        if(arr[i]<=pivot){
            indx++;
            swap(arr[i],arr[indx]);
        }
    }
    indx++;
    swap(arr[indx],arr[end]);
    return indx;
}

int random(int arr[],int start,int end){

    int r = start+rand()%(end-start+1);

    swap(arr[r],arr[end]);

    return partition(arr,start,end);
}

void deterministic(int arr[],int start,int end){

    if(start<end){
        int p = partition(arr,start,end);

        deterministic(arr,start,p-1);
        deterministic(arr,p+1,end);
    }
}

void randomized(int arr[],int start,int end){

    if(start<end){
        int r = random(arr,start,end);

        randomized(arr,start,r-1);
        randomized(arr,r+1,end);
    }
}

void display(int arr[],int n){
    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
}


int main(){

    int n, choice=0;

    cout<<"Enter size of array:";
    cin>>n;

    int arr[n];

    for(int i=0;i<n;i++){
        cin>>arr[i];
    }

    while(choice<3){
        cout<<"1.Deterministic quick sort";
        cout<<"\n2.Randomized quick sort";
        cout<<"\n3.Exit";

        cout<<"\nEnter your choice:";
        cin>>choice;

        switch(choice){

            case 1:
                deterministic(arr,0,n-1);
                cout<<"Array after Deterministic Sort:";
                display(arr,n);
                break;
            
            case 2:
                randomized(arr,0,n-1);
                cout<<"Array after Randomized sort:";
                display(arr,n);
                break;
            
            case 3:
                cout<<"Exiting....";
                break;

            default:
                cout<<"Enter valid choice";
        }
    }
    return 0;
}