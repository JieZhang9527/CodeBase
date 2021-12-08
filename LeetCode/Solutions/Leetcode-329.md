1. 记忆化深度优先搜索

> 从每个点开始深度优先搜索，找到该单元格开始的最长递增路径。但是直接深度优先搜索时间复杂度很高，每个点会被访问多次，每次都要重复计算。因此用record作为缓存矩阵，缓存已经计算过的单元格的结果


```C++
class Solution {
public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        if(matrix.empty()||matrix[0].empty())   return 0;
        int rows=matrix.size(),cols=matrix[0].size();
        vector<vector<int>> record(rows,vector<int>(cols,0));
        int ans=0;
        for(int i=0;i<rows;++i){
            for(int j=0;j<cols;++j){
                ans=max(ans,DFS(matrix,i,j,record));
            }
        }
        return ans;
    }
private:
    vector<vector<int>> steps={{-1,0},{1,0},{0,-1},{0,1}};
    bool help(int x,int y,vector<vector<int>> &matrix){
        int rows=matrix.size(),cols=matrix[0].size();
        return x>=0&&x<rows&&y>=0&&y<cols;
    }
    int DFS(vector<vector<int>> &matrix,int i,int j,vector<vector<int>> &record){
        if(record[i][j])    return record[i][j];
        record[i][j]=1;     //以自身作为递增序列就是长度为1
        for(auto step : steps){
            int x=step[0]+i;
            int y=step[1]+j;
            if(help(x,y,matrix)&&matrix[x][y]>matrix[i][j])
                record[i][j]=max(record[i][j],DFS(matrix,x,y,record)+1);
        }
        return record[i][j];
    }
};
```