#include <iostream>
#include <string>
#include <set>

using namespace std;

int main()
{
    string S, tmp;
    set<string> sol;
    int size;

    cin >> S;

    size = S.length();
    for(int i = 1; i <= size; i++)
    {
        for(int j = 0; j < size - i + 1; j++)
        {
            sol.insert(S.substr(j, i));
        }
    }

    cout << sol.size();

    return 0;
}