1. 哈希

> 两个map实现哈希双向映射

```C++
class Solution {
public:
    bool wordPattern(string pattern, string str) {
        unordered_map<string,char> mp1;
        unordered_map<char,string> mp2;
        vector<string> words=getStr(str);
        if(pattern.size()!= words.size())  return false;
        for(int i=0;i<pattern.size();++i){
            if(mp1.find(words[i])==mp1.end())   mp1[words[i]]=pattern[i];
            if(mp2.find(pattern[i])==mp2.end()) mp2[pattern[i]]=words[i];
            if(mp1[words[i]]!=pattern[i]||mp2[pattern[i]]!=words[i])    return false;
        }
        return true;
    }
    vector<string> getStr(string &str){
        vector<string> ans;
        string temp=string();
        for(char c : str){
            if(c==' '){
                ans.push_back(temp);
                temp.clear();
            }
            else  temp+=c;
        }
        ans.push_back(temp);
        return ans;
    }
};
```