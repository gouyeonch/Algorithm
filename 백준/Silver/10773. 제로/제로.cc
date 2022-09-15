//제로

#include <iostream>
#include <stack>

using namespace std;

int main() 
{
	
	int K,order,sum=0;
	stack<int> s;
	
	cin>>K;
	
	for(int i=0;i<K;i++){
		
		cin>>order;
		
		if(order==0) {
			sum-=s.top();
			s.pop();
		}
		else {
			sum+=order;
			s.push(order);
		}
	}
	
	cout<<sum<<endl;
		
	return 0;
}

