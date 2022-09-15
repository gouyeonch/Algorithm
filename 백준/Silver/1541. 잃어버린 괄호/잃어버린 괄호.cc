//잃어버린 괄호
#include <iostream>
#include <string>

using namespace std;

int main()
{
    string str, num;
    int sol= 0, min = 0, size;
    bool plus = 1;

    cin >> str;
    str.push_back('+');
    size = str.length();

    for(int i = 0; i < size; i++)
    {
        if('0' <= str[i] && str[i] <= '9') num += str[i];
        else
        {
            if(plus == true) sol += stoi(num);
            else min += stoi(num);

            if(str[i] == '-') plus = false;

            num = string();
        }
    }

    sol -= min;

    cout << sol;

    return 0;
}