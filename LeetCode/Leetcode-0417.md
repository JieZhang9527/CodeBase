> 两种方案：从水到陆地和从陆地到水。从陆地到水较为复杂，从水到陆地采用BFS和DFS，分别记录大西洋和太平洋的联通情况，如果两个都联通就是目标坐标值。

1. DFS

```C++
class Solution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& matrix) {
        vector<vector<int>> ans;
        if(matrix.empty()||matrix[0].empty())  return ans;
        int rows=matrix.size(),cols=matrix[0].size();
        vector<vector<bool>> pacific(rows,vector<bool>(cols,false));
        vector<vector<bool>> atlantic(rows,vector<bool>(cols,false));
        for(int i=0;i<rows;++i){
            for(int j=0;j<cols;++j){
                if(i==0||j==0)  DFS(matrix,pacific,i,j,matrix[i][j]);
                if(i==rows-1||j==cols-1)  DFS(matrix,atlantic,i,j,matrix[i][j]);
            }
        }
        for(int i=0;i<rows;++i){
            for(int j=0;j<cols;++j){
                if(pacific[i][j]&&atlantic[i][j])
                    ans.push_back({i,j});
            }
        }
        return ans;
    }
private:
    vector<vector<int>> dis={{-1,0},{1,0},{0,-1},{0,1}};
    void DFS(const vector<vector<int>> &matrix,vector<vector<bool>> &visited,int i,int j,int pre){
        if(i<0||i>=matrix.size()||j<0||j>=matrix[0].size()||visited[i][j]||matrix[i][j]<pre)
            return;
        visited[i][j]=true;
        for(int k=0;k<4;++k)
            DFS(matrix,visited,dis[k][0]+i,dis[k][1]+j,matrix[i][j]);
    }
};
```