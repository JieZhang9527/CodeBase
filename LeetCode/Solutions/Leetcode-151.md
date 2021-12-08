1. stringstream 
> 如何处理字符串中的空字符

```C++
class Solution {
public:
    string reverseWords(string s) {
        string ans=string(),word=string();
        vector<string> words;
        stringstream ss(s);
        while(ss>>word) words.push_back(word);
        for(int i=words.size()-1;i>=0;--i) ans+=words[i]+" ";
        if(ans.empty()) return ans;
        ans.pop_back();
        return ans;
    }
};
```