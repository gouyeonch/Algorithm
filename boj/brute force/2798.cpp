//블랙잭
#include <iostream>

using namespace std;

int main(){

    int n,m,e,ary[101];
    int maxSimul=1000000;

    cin>>n>>m;

    for(int i=0;i<n;i++){
        cin>>e;
        ary[i]=e;
    }

    for (int i = 2; i < n; i++)
    {
        for(int j = 1; j < i; j++)
        {
            for(int k = 0; k < j; k++)
            {
                int simul = m - (ary[i]+ary[j]+ary[k]);
                simul = abs(simul);
                if(simul == 0){
                    cout<<m;
                    return 0;
                }

                if(abs(simul) < abs(m-maxSimul))
                    maxSimul = ary[i]+ary[j]+ary[k];              
            }
        }
    }

    cout<<maxSimul;
    

    return 0;
}