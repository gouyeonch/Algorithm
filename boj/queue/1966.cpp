//프린터 큐
#include <iostream>
#include <queue>
#include <functional>

using namespace std;

struct node{
    int initind;
    int priority;

    node(int i, int p) : initind(i), priority(p) {}

    bool operator<(const node n) const{
        return this->priority > n.priority;
    }
};

int main(){

    int N,M,test;
    int p;

    cin>>test;

    //테스트 케이스 수에 따라 테스트 수행
    for (int i = 0; i < test; i++)
    {
        priority_queue<node, vector<node>, greater<node>> pq;

        cin>>N;
        cin>>M;

        for(int j=0;j<N;j++){
            cin>>p;

            pq.push(node(j,p));
        }
        
        for(int j=0;j<N;j++){
            node ts = pq.top(); pq.pop();
            if(ts.initind==M){
                cout<<j+1<<endl;
                break;
            }
        }

    }
    

    return 0;
}