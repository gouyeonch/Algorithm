//덱
#include <iostream>
#include <deque>
#include <string>

using namespace std;

int main()
{
    deque<int> dq;
    int N, num;
    string c;

    cin.tie(nullptr);
    ios::sync_with_stdio(false); 

    cin >> N;

    for(int i = 0; i < N; i++)
    {
        cin >> c;
        if(c == "push_front")
        {
            cin >> num;
            dq.push_front(num);
        }
        else if(c == "push_back")
        {
            cin >> num;
            dq.push_back(num);
        }
        else if(c == "pop_front")
        {
            if(dq.empty()) cout << -1 << "\n";
            else
            {
                cout << dq.front() << "\n";
                dq.pop_front();
            }
        }
        else if(c == "pop_back")
        {
            if(dq.empty()) cout << -1 << "\n";
            else
            {
                cout << dq.back() << "\n";
                dq.pop_back();
            }
        }
        else if(c == "front")
        {
            if(dq.empty()) cout << -1 << "\n";
            else
            {
                cout << dq.front() << "\n";
            }
        }
        else if(c == "back")
        {
            if(dq.empty()) cout << -1 << "\n";
            else
            {
                cout << dq.back() << "\n";
            }
        }
        else if(c == "size")
        {
            cout << dq.size() << "\n";
        }
        else
        {
            cout << dq.empty() << "\n";
        }
    }

    return 0;
}