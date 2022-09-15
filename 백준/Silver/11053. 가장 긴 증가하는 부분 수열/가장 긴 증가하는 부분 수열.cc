//가장 긴 증가하는 부분 수열
#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int N, num, min = 1000, max = 0;
    vector<pair<int,int>> A;

    cin >> N;

    for(int i = 0; i < N; i++)
    {
        cin >> num;
        A.push_back(pair<int,int>(num, 1));

        for(int j = 0; j < i; j++)
        {
            if(A[j].first < A[i].first && A[j].second >= A[i].second)
                A[i].second = A[j].second + 1;
        }
        if(A[i].second > max) max = A[i].second;
    }

    cout << max;

    return 0;
}