//숫자 카드
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
    int N, num, M;
    int a, l, mid;
    vector<int> list;

    cin.tie(NULL);
    ios::sync_with_stdio(false);

    cin >> N;
    for(int i = 0; i < N ; i++)
    {
        cin >> num;
        list.push_back(num);
    }
    sort(list.begin(), list.end());

    cin >> M;
    for(int i = 0; i < M; i++)
    {
        cin >> num;
        a = 0;
        l = list.size() - 1;
        while(1)
        {
            mid = (a + l)/2;

            if(list[mid] == num)
            {
                cout << 1 << " ";
                break;
            }          
            else if(list[mid] == list[a])
            {
                if(num == list[l]) cout << 1 << " ";
                else cout << 0 << " ";
                break;
            }
            else if(list[mid] > num) l = mid;
            else a = mid;
        }
    }

    return 0;
}