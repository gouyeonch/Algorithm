//대표값2
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
    vector<int> list;
    int avg = 0, cen, n;

    for(int i = 0; i < 5; i++)
    {
        cin >> n;

        list.push_back(n);
        avg += n;
    }

    sort(list.begin(), list.end());

    cout << avg/5 << endl;
    cout << list[2] << endl;

    return 0;
}