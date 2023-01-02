//어린 왕자
#include <iostream>
#include <cmath>

using namespace std;

//내부 점이면 1, 외부 점이면 0
bool iOo(int x1, int y1, int x2, int y2, int r)
{
    if(sqrt(pow<int,int>(x1-x2, 2) + pow<int,int>(y1-y2, 2)) < r) return 1;
    else return 0;
}

int main()
{
    int T, n, Sx, Sy, Ox, Oy, Tx, Ty, R, cnt = 0;

    cin >> T;

    for(int i = 0; i < T; i++)
    {
        cin >> Sx >> Sy >> Ox >> Oy >> n;

        cnt = 0;

        for(int j = 0; j < n; j++)
        {
            cin >> Tx >> Ty >> R;
            
            if(iOo(Sx, Sy, Tx, Ty, R) != iOo(Ox, Oy, Tx, Ty, R)) cnt++;
        }
        cout << cnt << endl;
    }

    return 0;
}