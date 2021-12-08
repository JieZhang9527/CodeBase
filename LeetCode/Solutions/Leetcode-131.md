1. 回溯

```C++
class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>> ans;
        vector<string> path;
        backtrack(s,0,path,ans);
        return ans;
    }
    void backtrack(string &s,int start,vector<string> &path,vector<vector<string>> &ans){
        if(start==s.size()){
            ans.push_back(path);
            return;
        }
        for(int i=start;i<s.size();++i){
            if(!isPalindrome(s,start,i)) continue;
            path.push_back(s.substr(start,i-start+1));
            backtrack(s,i+1,path,ans);
            path.pop_back();
        }
    }
    bool isPalindrome(string &s,int left,int right){
        while(left<right){
            if(s[left]!=s[right])   return false;
            ++left;
            --right;
        }
        return true;
    }
};
```