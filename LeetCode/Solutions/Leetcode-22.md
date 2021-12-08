1. 条件递归
> 记录当前生成括号序列中左括号和右括号的数量，当右括号小于左括号的数量才能进行回溯

```C++
class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> ans;
        backtrack(ans,string(),0,0,n);
        return ans;
    }
private:
    void backtrack(vector<string> &ans, string curr, int open, int close, int pairs){
        if(curr.size()==pairs*2){
            ans.push_back(curr);
            return;
        }
        if(open<pairs)  backtrack(ans,curr+"(",open+1,close,pairs);
        if(close<open)  backtrack(ans,curr+")",open,close+1,pairs);
    }
};
```