1. STL

```C++
class Solution {
public:
    string complexNumberMultiply(string a, string b) {
        int p=stoi(string(a.begin(),a.begin()+a.find('+')));
        int q=stoi(string(a.begin()+a.find('+')+1,a.end()-1));
        int m=stoi(string(b.begin(),b.begin()+b.find('+')));
        int n=stoi(string(b.begin()+b.find('+')+1,b.end()-1));

        string str1=to_string(p*m+q*n*(-1)),str2=to_string(p*n+q*m);
        string ans=str1+"+"+str2+"i";
        return ans;
    }
};
```