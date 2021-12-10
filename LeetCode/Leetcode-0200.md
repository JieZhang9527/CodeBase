> 其实就是求解图的连通量

1. DFS BFS

```C++
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        if(grid.empty()||grid[0].empty())   return 0;
        int rows=grid.size(), cols=grid[0].size();
        vector<vector<bool>> visited(rows,vector<bool>(cols,false));
        int ans=0;
        for(int i=0;i<rows;++i){
            for(int j=0;j<cols;++j){
                if(!visited[i][j]&&grid[i][j]=='1'){
                    BFS(grid,visited,i,j);
                    ++ans;
                }
            }
        }
        return ans;
    }
private:
    vector<vector<int>> directions={{0,1},{1,0},{0,-1},{-1,0}};
    bool help(vector<vector<char>> &grid,int i,int j){
        int rows=grid.size(), cols=grid[0].size();
        return i>=0&&i<rows&&j>=0&&j<cols;
    }
    void DFS(vector<vector<char>> &grid, vector<vector<bool>> &visited, int i, int j){
        visited[i][j]=true;
        for(int k=0;k<4;++k){
            int x=i+directions[k][0];
            int y=j+directions[k][1];
            if(help(grid,x,y)&&!visited[x][y]&&grid[i][j]=='1')
                DFS(grid,visited,x,y);
        }
    }
    void BFS(vector<vector<char>> &grid,vector<vector<bool>> &visited, int i, int j){
        queue<pair<int,int>> q;
        q.push(make_pair(i,j));
        visited[i][j]=true;
        while(!q.empty()){
            auto temp=q.front();
            q.pop();
            for(int k=0;k<4;++k){
                int x=temp.first+directions[k][0];
                int y=temp.second+directions[k][1];
                if(help(grid,x,y)&&!visited[x][y]&&grid[x][y]=='1'){
                    q.push(make_pair(x,y));
                    visited[x][y]=true;
                }
            }
        }
    }
};
```