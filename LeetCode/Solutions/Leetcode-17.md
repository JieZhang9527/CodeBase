1. 回溯
> 回溯标准模版

```C++
class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string> ans;
        if(digits.empty())  return ans;
        DFS(digits,0,string(),ans);
        return ans;
    }
private:
    void DFS(string &digits, int index, string path, vector<string> &ans){
        if(path.size()==digits.size()){
            ans.push_back(path);
            return;
        }
        for(int i=0;i<mp[digits[index]].size();++i){
            path.push_back(mp[digits[index]][i]);
            DFS(digits,index+1,path,ans);
            path.pop_back();
        }
    }
    unordered_map<char,string> mp={
        {'2', "abc"}, {'3', "def"}, {'4', "ghi"}, {'5', "jkl"},
        {'6', "mno"},{'7', "pqrs"}, {'8', "tuv"}, {'9', "wxyz"}
    };
};
```