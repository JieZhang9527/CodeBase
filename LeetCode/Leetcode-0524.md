1. 暴力匹配

```C++
class Solution {
public:
    string findLongestWord(string s, vector<string>& d) {
        string ans;
        for(const string &str : d){
            int a=str.size(),b=ans.size();
            if(a<b||(a==b&&ans<str))  continue;
            if(helper(s,str)){
                ans=str;
            }                  
        }
        return ans;
    }
    bool helper(const string &s1,const string &s2){
        int p1=0,p2=0;
        while(p1<s1.size()&&p2<s2.size()){
            if(s1[p1]==s2[p2]){
                ++p1;
                ++p2;
            }
            else
                ++p1;
        }
        return p2==s2.size();
    }
};
```