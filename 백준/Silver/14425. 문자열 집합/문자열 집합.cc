#include <iostream>
#include <string>
#include <vector>

using namespace std;

int hashing(string str)
{
    int idx = 0, len = str.length();

    for(int i = 0; i < len; i++)
    {
        idx += str[i];
    }

    return idx;
}

int main()
{
    int N, M, sol = 0, idx;
    string str;
    vector<string> S[62000];

    cin.tie(NULL);
    ios::sync_with_stdio(false);

    cin >> N >> M;
    
    for(int i = 0; i < N; i++)
    {
        cin >> str;
        S[hashing(str)].push_back(str);
    }
  
    for(int i = 0; i < M; i++)
    {
        cin >> str;

        idx = hashing(str);
        
        for(int j = 0; j < S[idx].size(); j++)
        {
            if(S[idx][j] == str)
            {
                sol++;
                break;
            }
        }
    }

    cout << sol;

    return 0;
}