//괄호

#include <iostream>
#include <string>

using namespace std;

int main() {
	
	int T,size;
	string PS;
	
	cin>>T;
	
	for(int i=0;i<T;i++){
		cin>>PS;
		if(PS.size()%2==1){
			cout<<"NO"<<endl;
			i++;
			if(i==T)break;
			cin>>PS;
		}
		
		while(1){
			size=PS.size();
			for(int j=1;j<size;j++){
				if(PS[j-1]=='('&&PS[j]==')'){
					PS.erase(j-1,2);
					break;
				}
			}
			
			if(size==PS.size()){
				cout<<"NO"<<endl;
				break;
			}
			
			if(PS.empty()==1){
				cout<<"YES"<<endl;
				break;
			}
		}
	}
	
	return 0;
}

