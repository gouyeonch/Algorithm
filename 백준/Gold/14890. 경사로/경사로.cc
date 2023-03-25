#include <iostream>

using namespace std;

int main()
{
    int N, L, i, j, mc, now, cnt = 0;
    int **map;
    bool down = false;

    cin >> N >> L;

    // 맵 입력
    map = new int *[N];
    for (i = 0; i < N; i++)
    {
        map[i] = new int[N];
        for (j = 0; j < N; j++)
        {
            cin >> map[i][j];
        }
    }

    // 가로
    for (i = 0; i < N; i++)
    {
        now = map[i][0];
        mc = 1;
        down = false;
        for (j = 1; j < N; j++)
        {
            int diff = map[i][j] - now;
            // 높이 차이 확인
            if (diff > 1 || diff < -1)
                break;
            // 높아질 때
            if (diff == 1)
            {
                if (down == true || mc < L)
                    break;
                now = map[i][j];
                mc = 1;
            } // 낮아질 때
            else if (diff == -1)
            {
                // 낮아지는 경우가 안될 때
                if (down == true)
                    break;
                mc = 1;
                now = map[i][j];
                down = true;
            } // 같을 때
            else
                mc++;

            if (down == true && mc >= L)
            {
                down = false;
                mc = 0;
            }
        }
        if (j == N && down == false)
            cnt++;
    }
    // 세로
    for (j = 0; j < N; j++)
    {
        now = map[0][j];
        mc = 1;
        down = false;
        for (i = 1; i < N; i++)
        {
            int diff = map[i][j] - now;
            // 높이 차이 확인
            if (diff > 1 || diff < -1)
                break;
            // 높아질 때
            if (diff == 1)
            {
                if (down == true || mc < L)
                    break;
                now = map[i][j];
                mc = 1;
            } // 낮아질 때
            else if (diff == -1)
            {
                // 낮아지는 경우가 안될 때
                if (down == true)
                    break;
                mc = 1;
                now = map[i][j];
                down = true;
            } // 같을 때
            else
                mc++;

            if (down == true && mc >= L)
            {
                down = false;
                mc = 0;
            }
        }
        if (i == N && down == false)
            cnt++;
    }

    cout << cnt << endl;
}