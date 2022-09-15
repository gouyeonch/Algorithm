#include <iostream>
#include <queue>
#include <string>

using namespace std;

int main(){
    cin.tie(nullptr);
    ios::sync_with_stdio(false); 

    int N,e;
    string c;
    queue<int> q;

    cin>>N;

    for(int i=0;i<N;i++){
        cin>>c;

        if(c == "push"){
            cin>>e;
            q.push(e);
        }
        else if(c == "pop"){
            if(q.empty()) cout<<-1<<"\n";
            else{
                cout<<q.front()<<"\n";
                q.pop();
            }
        }
        else if(c == "size"){
            cout<<q.size()<<"\n";
        }
        else if(c == "empty"){
            cout<<q.empty()<<"\n";
        }
        else if(c == "front"){
            if(q.empty()) cout<<-1<<"\n";
            else cout<<q.front()<<"\n";
        }
        else{
            if(q.empty()) cout<<-1<<"\n";
            else cout<<q.back()<<"\n";
        }
    }

    return 0;
}