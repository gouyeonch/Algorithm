//단어 정렬
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

bool compare(string a, string b)
{
    if(a.length() == b.length()) return a < b;
    else return a.length() < b.length();
}

int main()
{
    int N;
    string str;
    vector<string> list;

    cin >> N;

    for(int i = 0 ; i < N ; i++)
    {
        cin >> str;
        list.push_back(str);
    }

    sort(list.begin(), list.end(), compare);

    cout << list[0] << "\n";
    for(int i = 1 ; i < N ; i++)
    {
        if(list[i-1] != list[i]) cout << list[i] << "\n";
    }

    return 0;
}