#include <iostream>

using namespace std;

int main()
{
    int a, b, c, x, y, z;
    int w[51][51][51];

    for(int i = 0; i < 51; i++)
    {
        for(int j = 0; j < 51; j++)
        {
            w[0][i][j] = 1;
            w[i][0][j] = 1;
            w[i][j][0] = 1;
        }
    }

    while(1)
    {
        cin >> a >> b >> c;

        if(a == -1 && b == -1 && c == -1) break;

        x = a;
        y = b;
        z = c;
       
        if(a < 0) a = 0;
        if(b < 0) b = 0;
        if(c < 0) c = 0;

        if(a > 20) a = 20;
        if(b > 20) b = 20;
        if(c > 20) c = 20;

        for(int i = 1; i <= a; i++)
        {
            for(int j = 1; j <= b; j++)
            {
                for(int k = 1; k <= c; k++)
                {
                    if(i < j && j < k) w[i][j][k] = w[i][j][k-1] + w[i][j-1][k-1] - w[i][j-1][k];
                    else w[i][j][k] = w[i-1][j][k] + w[i-1][j-1][k] + w[i-1][j][k-1] - w[i-1][j-1][k-1];
                }
            }
        }

        cout << "w(" << x << ", " << y << ", " << z << ") = " << w[a][b][c] << "\n";
    }
    return 0;
}