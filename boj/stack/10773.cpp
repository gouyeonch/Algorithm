//제로
#include <iostream>
#include <stack>

using namespace std;

int main(){

    int K,c,ans=0;
    stack<int> s;

    cin>>K;

    for(int i=0;i<K;i++){
        cin>>c;
        if(!c) s.pop();
        else s.push(c);
    }

    int size = s.size();
    for(int i=0;i<size;i++){
        ans += s.top();
        s.pop();
    }

    cout<<ans;

    return 0;
}