//덩치
#include <iostream>

using namespace std;

typedef struct big
{
    int weight;
    int height;
    int scr = 1;
}big;

int main()
{
    int N;
    big* list;

    cin>>N;

    list = new big[N];

    for(int i = 0 ; i < N ; i++)
        cin >> list[i].weight >> list[i].height;

    for(int i = 0 ; i < N ; i++)
    {
        for(int j = 0 ; j < N ; j++)
        {
            if(list[i].height < list[j].height && list[i].weight < list[j].weight) list[i].scr++;
        }
        cout << list[i].scr << " ";
    }

    return 0;
}