#include <iostream>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <vector>

using namespace std;

int second(int* list, int N, int min, int max)
{
    int count = 0, middle = N/2+1;

    for(int i = min ; i <= max ; i++)
    {
        for(int j = 0 ; j < list[i] ; j++)
        {
            count++;
            if(count == middle) return i;
        }
    }
}

int main()
{
    int N, num, max = -4001, min = 4001, offenMax = 0, back;
    int list[8001];
    double sum = 0;

    vector<int> offen;

    memset(list, 0, sizeof(list));

    cin >> N;

    for(int i = 0 ; i < N ; i++)
    {
        cin >> num;

        list[num + 4000]++;
        
        sum += num;
        
        if(num < min) min = num;
        if(num > max) max = num;
    }

    max += 4000;
    min += 4000;

    //산술기하
    int rround = round(sum/N);
    if(rround == -0) rround =0;
    cout << rround << "\n";

    //중앙값
    cout << second(list, N, min, max)-4000 << "\n";

    //최빈값
    for(int i = max ; i >= min ; i--)
    {
        if(list[i] >= offenMax)
        {
            offenMax = list[i];
            offen.push_back(i);
        }
    }
    back = offen.back();

    if(offen.size() == 1) cout << back-4000 << "\n";
    else{
        offen.pop_back();
        if(list[back] == list[offen.back()]) cout << offen.back()-4000 << "\n";
        else cout << back-4000 << "\n";
    }
    

    //범위
    cout << max - min << "\n";

    return 0;
}