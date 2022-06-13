//AC
#include <iostream>
#include <deque>
#include <string>

using namespace std;

int main()
{
    int N, n, num, size, length, filp;
    string p, ary;

    cin.tie(nullptr);
    ios::sync_with_stdio(false); 

    cin >> N;

    for(int i = 0; i < N; i++)
    {
        cin >> p >> size >> ary;

        filp = 1;
        deque<int> dq;

        length = ary.length();
        for(int j = 1; j < length - 1; j++)
        {
            string str;
            while(ary[j] != ',')
            {
                str += ary[j++];
            }
            dq.push_back(stoi(str));
        }

        length = p.length();
        for(int j = 0; j < length; j++)
        {
            if(dq.empty())
            {
                length = -1;
                break;
            }

            if(p[j] == 'R') filp *= -1;
            else
            {    
                if(filp == -1)
                {
                    dq.pop_back();
                }
                else
                {
                    dq.pop_front();
                }
            }
        }

        if(length == -1)
        {
            cout << "error" << "\n";
        }
        else
        {
            cout << "[";

            size = dq.size();

            if(filp == -1)
            {
                for(int j = 0; j < size + (size-1); j++)
                {
                    if(j % 2 == 0)
                    {
                        cout << dq.back();
                        dq.pop_back();
                    }
                    else cout << ",";
                }
            }
            else
            {
                for(int j = 0; j < size + (size-1); j++)
                {
                    if(j % 2 == 0)
                    {
                        cout << dq.front();
                        dq.pop_front();
                    }
                    else cout << ",";
                }
            }

            cout << "]" << "\n";
        }
    }

    return 0;
}