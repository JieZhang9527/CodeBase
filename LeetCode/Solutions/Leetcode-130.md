> 解决本题的关键：对每个边界点深度或广度遍历找到所有的连通点，其余点统一为X

1. DFS递归

```C++
class Solution {
public:
    void solve(vector<vector<char>>& board) {
        if(board.size()==0||board[0].size()==0)  return;
        int rows=board.size();
        int cols=board[0].size();
        for(int i=0;i<rows;++i){
            for(int j=0;j<cols;++j){
                if((i==0||i==rows-1||j==0||j==cols-1)&&board[i][j]=='O')
                    DFS(board,i,j,rows,cols);
            }
        }
        for(int i=0;i<rows;++i){
            for(int j=0;j<cols;++j){
                if(board[i][j]=='#')  board[i][j]='O';
                else if(board[i][j]=='O') board[i][j]='X';
            }
        }
        return;
    }
    void DFS(vector<vector<char>>& board,int i,int j,int rows,int cols){
        if(i<0||i>=rows||j<0||j>=cols||board[i][j]=='X'||board[i][j]=='#')
            return;
        board[i][j]='#';
        DFS(board,i+1,j,rows,cols);
        DFS(board,i-1,j,rows,cols);
        DFS(board,i,j+1,rows,cols);
        DFS(board,i,j-1,rows,cols);
    }
};
```

2. DFS非递归

```C++
class Solution {
public:
    void solve(vector<vector<char>>& board) {
        if(board.size()==0||board[0].size()==0)  return;
        int rows=board.size();
        int cols=board[0].size();
        for(int i=0;i<rows;++i){
            for(int j=0;j<cols;++j){
                if((i==0||i==rows-1||j==0||j==cols-1)&&board[i][j]=='O')
                    DFS(board,i,j,rows,cols);
            }
        }
        for(int i=0;i<rows;++i){
            for(int j=0;j<cols;++j){
                if(board[i][j]=='#')  board[i][j]='O';
                else if(board[i][j]=='O') board[i][j]='X';
            }
        }
        return;
    }
    void DFS(vector<vector<char>>& board,int i,int j,int rows,int cols){
        stack<pair<int,int>> st;
        st.push(make_pair(i,j));
        board[i][j]='#';
        while(!st.empty()){
            pair<int,int> temp=st.top();
            int x=temp.first;
            int y=temp.second;
            if(x-1>=0&&board[x-1][y]=='O'){
                st.push(make_pair(x-1,y));
                board[x-1][y]='#';
                continue;
            }
            if(x+1<rows&&board[x+1][y]=='O'){
                st.push(make_pair(x+1,y));
                board[x+1][y]='#';
                continue;
            }
            if(y-1>=0&&board[x][y-1]=='O'){
                st.push(make_pair(x,y-1));
                board[x][y-1]='#';
                continue;
            }
            if(y+1<cols&&board[x][y+1]=='O'){
                st.push(make_pair(x,y+1));
                board[x][y+1]='#';
                continue;
            }
            st.pop();  // 上下左右都没有可访问的才返回
        }
    }
};
```


3. BFS非递归
   

```C++
class Solution {
public:
    void solve(vector<vector<char>>& board) {
        if(board.size()==0||board[0].size()==0)  return;
        int rows=board.size();
        int cols=board[0].size();
        for(int i=0;i<rows;++i){
            for(int j=0;j<cols;++j){
                if((i==0||i==rows-1||j==0||j==cols-1)&&board[i][j]=='O')
                    BFS(board,i,j,rows,cols);
            }
        }
        for(int i=0;i<rows;++i){
            for(int j=0;j<cols;++j){
                if(board[i][j]=='#')  board[i][j]='O';
                else if(board[i][j]=='O') board[i][j]='X';
            }
        }
        return;
    }
    void BFS(vector<vector<char>>& board,int i,int j,int rows,int cols){
        queue<pair<int,int>> q;
        q.push(make_pair(i,j));
        board[i][j]='#';
        while(!q.empty()){
            pair<int,int> temp=q.front();
            int x=temp.first;
            int y=temp.second;
            if(x-1>=0&&board[x-1][y]=='O'){
                q.push(make_pair(x-1,y));
                board[x-1][y]='#';
            }
            if(x+1<rows&&board[x+1][y]=='O'){
                q.push(make_pair(x+1,y));
                board[x+1][y]='#';
            }
            if(y-1>=0&&board[x][y-1]=='O'){
                q.push(make_pair(x,y-1));
                board[x][y-1]='#';
            }
            if(y+1<cols&&board[x][y+1]=='O'){
                q.push(make_pair(x,y+1));
                board[x][y+1]='#';
            }
            q.pop();  
        }
    }
};
```