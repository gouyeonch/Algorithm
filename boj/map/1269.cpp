#include <iostream>
#include <set>

using namespace std;

int main()
{
    int N, M, num, count = 0;
    set<int> s;

    cin >> N >> M;

    for(int i = 0; i < N; i++)
    {
        cin >> num;
        s.insert(num);
    }

    for(auto i : s)
    {
        cin >> num;
        count += s.count(num);
    }

    cout << N + M - count * 2;

    return 0;
}