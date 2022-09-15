//오큰수
#include <iostream>
#include <stack>

using namespace std;

int origin[1000001];
int pntary[1000001];

int main()
{

    int N, c;

    stack<int> s;

    cin>>N;

    for(int i=0;i<N;i++)
        cin>>origin[i];

    for(int i=N-1;i>=0;i--)
    {
        while(!s.empty()&&s.top()<=origin[i])
            s.pop();
        
        if(s.empty()) pntary[i] = -1;
        else pntary[i] = s.top();

        s.push(origin[i]);
    }

    for(int i=0;i<N;i++)
        cout<<pntary[i]<<" ";


    return 0;
}