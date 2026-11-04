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
    swap(arr[end],arr[indx]);

    return indx;
}

void deterministic(int arr[],int start,int end){
    if(start<end){
        int p = partition(arr,start,end);
        deterministic(arr,start,p-1);
        deterministic(arr,p+1,end);
    }
}

int rd(int arr[],int start,int end){
    int r = start+rand()%(end-start+1);

    swap(arr[r],arr[end]);

    return partition(arr,start,end);

}

void random(int arr[],int start,int end){
    if(start<end){
        int p = rd(arr,start,end);
        random(arr,start,p-1);
        random(arr,p+1,end);
    }
}

void printO(int arr[],int n){
    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
}

int main(){

    int n ;
    cout<<"Enter size of array:";
    cin>>n;

    int arr[n];

    cout<<"Enter elements in array";
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }

    int choice;

    while(true){
        cout<<"1.Deterministic";
        cout<<"\n2.Randomasized";
        cout<<"\n3.Exiting....";
        cout<<"\nEnter your choice";
        cin>>choice;

        switch(choice){

            case 1:
                deterministic(arr,0,n-1);
                cout<<"Sorted array using deterministic method"<<endl;
                printO(arr,n);
                break;

            case 2:
                random(arr,0,n-1);
                cout<<"Sorted array using random method"<<endl;
                printO(arr,n);
                break;
            
            case 3:
                cout<<"Exiting...";
                return 0;
            
            default:
                cout<<"Enter valid choice"<<endl;

        }
        
    }
    return 0;
}