#include <iostream>
#include <map>
#include <vector>

using namespace std;

int main()
{
    int N, num, M;
    map<int, int> m;

    cin.tie(NULL);
    ios::sync_with_stdio(false);

    cin >> N;

    for(int i = 0; i < N; i++)
    {
        cin >> num;
        auto it = m.find(num);
        if(it == m.end()) m.insert({num, 1});
        else it->second++;
    }

    cin >> M;

    for(int i = 0; i < M; i++)
    {
        cin >> num;
        auto it = m.find(num);
        if(it == m.end()) cout << 0 << " ";
        else cout << it->second << " ";
    }

    return 0;
}