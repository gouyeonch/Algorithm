//나는야 포켓몬 마스터
#include <iostream>
#include <map>
#include <vector>

using namespace std;

int main()
{
    map<string, int> m;
    vector<string> name;
    int N, M;
    string pkmon, c;

    cin.tie(NULL);
    ios::sync_with_stdio(false);

    cin >> N >> M;

    for(int i = 1; i <= N; i++)
    {
        cin >> pkmon;
        m.insert({pkmon, i});
        name.push_back(pkmon);
    }

    for(int i = 0; i < M; i++)
    {
        cin >> c;

        if(isdigit(c[0])) cout << name[stoi(c)-1] << "\n";
        else
        {
            auto find = m.find(c);
            if(find != m.end()) cout << find->second << "\n";
        }
    }

    return 0;
}