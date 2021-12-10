1. 暴力

```C++
class Solution {
public:
    vector<string> restoreIpAddresses(string s) {
        vector<string> ans;
        if(s.empty())   return ans;
        for(int a=1;a<4;++a){
            for(int b=1;b<4;++b){
                for(int c=1;c<4;++c){
                    for(int d=1;d<4;++d){
                        if(a+b+c+d==s.size()){
                        auto ip1=stoi(s.substr(0,a));
                        auto ip2=stoi(s.substr(a,b));
                        auto ip3=stoi(s.substr(a+b,c));
                        auto ip4=stoi(s.substr(a+b+c,d));
                            if(ip1<=255&&ip2<=255&&ip3<=255&&ip4<=255){
                                string ip=to_string(ip1)+'.'+to_string(ip2)+'.'+to_string(ip3)+'.'+to_string(ip4);
                                if(ip.size()==s.size()+3)   ans.push_back(ip);
                            }
                        }
                    }
                }
            }
        }
        return ans;
    }
};