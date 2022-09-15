//수 정렬하기2
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int  main()
{
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    int N, num;
    int* list;
    
    cin>>N;
    list = new int[N];

    for(int i = 0 ; i < N ; i++)
    {
        cin>>num;
        list[i] = num;
    }

    sort(list, list + N);

    cout << list[0] << endl;
    for(int i = 1 ; i < N ; i++)
    {
        if(list[i-1] != list[i]) cout << list[i] << "\n";
    }
        

    return 0;
}