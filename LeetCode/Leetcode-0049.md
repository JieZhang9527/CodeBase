1. 暴力排序
> 将同一个单词的所有异位词排序后形式相同

```C++
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> ans;
        unordered_map<string,vector<string>> ump;
        for(auto &str : strs){
            auto temp=str;
            sort(temp.begin(),temp.end());
            ump[temp].push_back(str);
        }
        for(auto &it : ump) ans.push_back(it.second);
        return ans;
    }
};
```