#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main(){
    cin.tie(nullptr);
    ios::sync_with_stdio(false); 

    stack<int> s;
    int num=1, c, N;
    string ans;

    s.push(0);

    cin>>N;

    for(int i=0;i<N;i++){
        cin>>c;

        if(s.top()>c) {
            cout<<"NO";
            return 0;
        }

        while(c!=s.top()){
            s.push(num++);
            ans+="+\n";
        }
        s.pop();
        ans+="-\n";
    }

    cout<<ans;

    return 0;
}