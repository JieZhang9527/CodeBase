1. map
> 使用两个map相互映射,实质是两个字符串是平等的关系

```C++
class Solution {
public:
    bool isIsomorphic(string s, string t) {
        if(s.size()!=t.size()){
            return false;
        }
        unordered_map<char,char> mps;
        unordered_map<char,char> mpt;
        int length=s.size();
        for(int i=0;i<length;++i){
            if(mps.find(s[i])!=mps.end()){
                if(mps[s[i]]!=t[i])  return false;
            }
            else if(mpt.find(t[i])!=mpt.end()){
                if(mpt[t[i]]!=s[i])  return false;
            }
            else{
                mps[s[i]]=t[i];
                mpt[t[i]]=s[i];
            }
        }
        return true;
    }
};
```