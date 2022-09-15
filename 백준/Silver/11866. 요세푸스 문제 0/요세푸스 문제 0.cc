//요세푸스 문제 0
#include <iostream>
#include <queue>

using namespace std;

int main(){
    queue<int> q;
    int N,K;

    cin>>N;
    cin>>K;

    cout<<"<";

    for(int i=1;i<=N;i++)
        q.push(i);

    while(!q.empty()){
        for(int i=0;i<K-1;i++){
            q.push(q.front());
            q.pop();
        }

        cout<<q.front();
        q.pop();

        if(!q.empty()) cout<<", ";
    }
    cout<<">";
    

    return 0;
}