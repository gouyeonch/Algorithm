//균형잡힌 세상
#include <iostream>
#include <stack>
#include <string>

using namespace std;
int main(){

    string c;
    string str;

    while(1){
        getline(cin, c);

        if(c ==".")return 0;
        stack<char> s;
        
        for(int i=0;i<c.length()+1;i++){
            if(c[i]=='.') {
                if(!s.empty()) cout<<"no"<<endl;
                else cout<<"yes"<<endl;
            }
            else if(c[i]=='('||c[i]=='[') s.push(c[i]);
            else if(c[i]==')'){
                if(!s.empty()&&s.top()=='(') s.pop();
                else{
                    do{
                        i++;
                    }while(c[i]!='.');        
                    i++;
                    cout<<"no"<<endl;
                }
            }
            else if(c[i]==']'){
                if(!s.empty()&&s.top()=='[') s.pop();
                else{
                    do{
                        i++;
                    }while(c[i]!='.');
                    i++;
                    cout<<"no"<<endl;
                }
            }
        }
    }
    
    return 0;
    }