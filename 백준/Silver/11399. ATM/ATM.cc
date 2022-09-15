//ATM
#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int N, num, sol = 0;
    int* list;

    cin>>N;

    list = new int[N];

    for(int i = 0 ; i < N ; i++)
    {
        cin >> num;
        list[i] = num;
    }

    sort(list, list + N);

    sol = list[0];
    for(int i = 1 ; i < N ; i++)
    {
        list[i] += list[i-1];
        sol += list[i];
    }

    cout << sol << endl;

    delete[] list;

    return 0;
}