1. 回溯
> 遍历每个数有选和不选两种，如果选的数目达到要求就加入结果  
> 时空复杂度较高

```C++
class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<int> path;
        vector<vector<int>> ans;
        DFS(n,k,1,path,ans);
        return ans;
    }
private:
    void DFS(int n, int k, int curr, vector<int> path, vector<vector<int>> &ans){
        if(path.size()==k){
            ans.push_back(path);
            return;
        }
        for(int i=curr;i<=n;++i){
            path.push_back(i);
            DFS(n,k,i+1,path,ans);
            path.pop_back();
        }
    }
};
```