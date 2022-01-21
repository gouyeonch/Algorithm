#include <iostream>
#include <string>
#include <stack>

using namespace std;

int main(){

    int N, e;
    string c;
    stack<int> s;

    cin>>N;

    for(int i=0;i<N;i++){
        cin>>c;

        if(c=="push"){
            cin>>e;
            s.push(e);
        }
        else if(c=="pop"){
            if(s.empty()) cout<<-1<<endl;
            else{
                cout<<s.top()<<endl;
                s.pop();
            }            
        }
        else if(c=="size"){
            cout<<s.size()<<endl;
        }
        else if(c=="empty"){
            cout<<s.empty()<<endl;
        }
        else{
            if(s.empty()) cout<<-1<<endl;
            else{
                cout<<s.top()<<endl;
            }           
        }
    }

    return 0;
}