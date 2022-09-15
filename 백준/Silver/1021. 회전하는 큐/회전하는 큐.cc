//회전하는 큐
#include <iostream>
#include <deque>

using namespace std;

int main()
{
    int N, M, num, count = 0, find, size, mid;
    deque<int> dq;

    cin >> N >> M;

    for(int i = 0; i < N; i++)
        dq.push_back(i);

    for(int i = 0; i < M; i++)
    {
        cin >> num;
        num--;

        size = dq.size();
        for(int j = 0; j < size; j++)
        {
            if(num == dq[j])
            {
                find = j;
                break;
            }
        }

        mid = (++size)/2;
        if(find < mid)
        {
            while(dq.front() != num)
            {
                dq.push_back(dq.front());
                dq.pop_front();
                count++;
            }
            dq.pop_front();
        }
        else
        {
            while(dq.back() != num)
            {
                dq.push_front(dq.back());
                dq.pop_back();
                count++;
            }
            count++;
            dq.pop_back();
        }
    }

    cout << count << endl;

    return 0;
}