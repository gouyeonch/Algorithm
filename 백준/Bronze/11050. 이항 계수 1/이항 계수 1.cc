#include <iostream>

using namespace std;

int fac(int n);

int main() {
	
	int N,K,C;
	
	cin>>N>>K;
	
	cout<<fac(N)/fac(N-K)/fac(K);
	
	return 0;
}

int fac(int n){
	int sum=1;
	
	for(int i=0;i<n;i++) sum*=(i+1);
	
	return sum;
}