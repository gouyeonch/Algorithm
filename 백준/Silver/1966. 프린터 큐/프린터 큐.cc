//프린터 큐
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main()
{
    int test, N, M, imp, count = 0;
    priority_queue<int> ptyq;
    queue< pair<int, int> > q;

    cin >> test;

    for(int i = 0; i < test; i++)
    {
        cin >> N >> M;
        count = 0;
        ptyq = priority_queue<int>();
        q = queue< pair<int, int> >();

        for(int j = 0; j < N; j++)
        {
            cin >> imp;
            ptyq.emplace(imp);
            q.emplace(imp, j);
        }

        while(1)
        {
            if(q.front().first >= ptyq.top())
            {
                count++;
                if(q.front().second == M)
                {
                    cout << count << endl;
                    break;
                }
                q.pop();
                ptyq.pop();
            }
            else
            {
                q.emplace(q.front());
                q.pop();
            }
        }
    }

    return 0;
}