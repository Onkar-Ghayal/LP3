#include<iostream>
#include<queue>
#include<vector>
using namespace std;

struct Node{
    char ch;
    int freq;
    Node* left;
    Node* right;

    Node(char c,int f){
        ch=c;
        freq=f;
        left=right=nullptr;
    }
};

struct Compare{
    bool operator()(Node* a,Node* b){
        return a->freq > b->freq;
    }
};

void printCode(Node* root, string s){
    if(root==nullptr){
        return;
    }
    if(root->left==nullptr && root->right==nullptr){
        cout<<root->ch<<" : "<< s <<endl;
    }
    printCode(root->left,s+'0');
    printCode(root->right,s+'1');
}

int main(){
    int n;
    char ch;
    int freq;

    priority_queue<Node*,vector<Node*>,Compare>pq;

    cout<<"Enter number of characters:";
    cin>>n;

    cout<<"Enter character and Frquency:"<<endl;
    for(int i=0;i<n;i++){
        cin>>ch>>freq;
        pq.push(new Node(ch,freq));
    }

    while(pq.size()>1){
        Node* left = pq.top();
        pq.pop();

        Node* right = pq.top();
        pq.pop();

        Node* newNode = new Node('$',left->freq+right->freq);

        newNode->left = left;
        newNode->right = right;

        pq.push(newNode);
    }

    Node* root = pq.top();

    cout<<"After Huffman Encoding"<<endl;

    printCode(root,"");

    return 0;
}