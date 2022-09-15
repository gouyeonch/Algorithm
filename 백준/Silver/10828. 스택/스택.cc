#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main() {
	
	int N;
	string order;
	stack<int> s;
	
	cin>>N;
	
	for(int i=0;i<N;i++){
		
		cin>>order;
		
		if(order.compare("push")==0){
			int n;
			cin>>n;
			s.push(n);
		}
		else if(order.compare("pop")==0){
			if(s.empty()==1) cout<<-1<<endl;
			else{
				cout<<s.top()<<endl;;
				s.pop();
			}
		}
		else if(order.compare("size")==0){
			cout<<s.size()<<endl;
		}
		else if(order.compare("empty")==0){
			cout<<s.empty()<<endl;
		}
		else{
			if(s.empty()==1) cout<<-1<<endl;
			else cout<<s.top()<<endl;
		}
	}
	
	return 0;
}

