#include <iostream>

using namespace std;

int main()
{
    int a=1, b=1;

    while(1)
    {
        cin >> a >> b;
        if(a==0&&b==0) break;

        if(a > b)
        {
            if(a%b == 0) cout << "multiple" << endl;
            else cout << "neither" << endl;
        }
        else
        {
            if(b%a == 0) cout << "factor" << endl;
            else cout << "neither" << endl;
        }
    }

    

    return 0;
}