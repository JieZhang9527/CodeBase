1. 回溯
> 二维回溯

```C++
class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        if(board.empty())   return word.empty();
        int rows=board.size(), cols=board[0].size();
        for(int i=0;i<rows;++i){
            for(int j=0;j<cols;++j){
                if(DFS(board,word,i,j,0))   return true;
            }
        }
        return false;
    }
private:
    bool DFS(vector<vector<char>> &board, string &word, int i, int j, int index){
        // 注意这里的写法
        if(board[i][j]!=word[index])    return false;
        if(index==word.size()-1) return true;
        auto temp=board[i][j]; board[i][j]=0;
        int rows=board.size(), cols=board[0].size();
        if(
            (i-1>=0&&DFS(board,word,i-1,j,index+1))||(i+1<rows&&DFS(board,word,i+1,j,index+1))||
            (j-1>=0&&DFS(board,word,i,j-1,index+1))||(j+1<cols&&DFS(board,word,i,j+1,index+1))
        )
            return true;
        board[i][j]=temp;
        return false;
    }
};
```