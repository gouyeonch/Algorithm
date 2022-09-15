//알고리즘 수업 - 피보나치 수 1
#include <iostream>

using namespace std;

int count1 = 0;
int count2 = 0;

int fib(int n)
{
    
    if(n == 1 || n == 2)
    {
        count1++;
        return 1;
    }
    else return (fib(n - 1) + fib(n - 2));
}

int fibonacchi(int n)
{
    int f[n];
    f[0] = f[1] =1;

    for(int i = 2; i < n; i++)
    {
        f[i] = f[i - 1] + f[i - 2];
        count2++;
    }

    return f[n];
}

int main()
{
    int n;
    cin >> n;

    fib(n);
    fibonacchi(n);

    cout << count1 << " " << count2;

    return 0;
}