#include <iostream>

using namespace std;

int main()
{
    int N, a, b, c, dpA, dpB, dpC, tempA, tempB, min;

    cin >> N;

    cin >> a >> b >> c;
    dpA = a;
    dpB = b;
    dpC = c;

    for(int i = 1; i < N; i++)
    {
        cin >> a >> b >> c;

        tempA = dpA;
        tempB = dpB;

        if(dpB < dpC) dpA = a + dpB;
        else dpA = a + dpC;

        if(tempA < dpC) dpB = b + tempA;
        else dpB = b + dpC;

        if(tempB < tempA) dpC = c + tempB;
        else dpC = c + tempA;
    }

    if(dpA < dpB && dpA < dpC) cout << dpA << endl;
    else if(dpB < dpC) cout << dpB << endl;
    else cout << dpC << endl;

    return 0;
}