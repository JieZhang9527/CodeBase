1. 回溯

```C++
class Solution {
public:
    vector<vector<int>> combinationSum3(int k, int n) {
        vector<vector<int>> ans;
        help(k,n,1,vector<int>(),ans);
        return ans;
    }
private:
    void help(int k, int n, int start, vector<int> path, vector<vector<int>> &ans){
        if(n<0) return;
        if(k==0){
            if(n==0)    ans.push_back(path);
            return;
        }
        for(int i=start;i<10;++i){
            path.push_back(i);
            help(k-1,n-i,i+1,path,ans);
            path.pop_back();
        }
    }
};
```