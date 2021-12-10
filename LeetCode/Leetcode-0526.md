1. 带鱼处理的回溯

```C++
class Solution {
public:
    int countArrangement(int N) {
        vector<vector<int>> permutations(N+1);
        vector<bool> visited(N+1,false);
        for(int i=1;i<=N;++i){
            for(int j=1;j<=N;++j){
                if(i%j==0||j%i==0){
                    permutations[i].push_back(j);
                }
            }
        }
        int ans=0;
        DFS(1,N,permutations,visited,ans);
        return ans;
    }
private:
    void DFS(int index,int n,vector<vector<int>> &permutations,vector<bool> &visited,int &ans){
        if(index==n+1){
            ++ans;
            return;
        }
        for(auto &num : permutations[index]){
            if(!visited[num]){
                visited[num]=true;
                DFS(index+1,n,permutations,visited,ans);
                visited[num]=false;
            }
        }
    }
};
```