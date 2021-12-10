1. DFS

> 暴力深度优先搜索

```C++
class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        for(int i=0;i<board.size();++i){
            for(int j=0;j<board[0].size();++j){
                if(DFS(board,word,i,j,0))   return true;
            }
        }
        return false;
    }
    bool DFS(vector<vector<char>> &board,string word,int i,int j,int index){
        if(board[i][j]!=word[index])  return false;
        if(index==word.size()-1)    return true;
        char temp=board[i][j];board[i][j]=0;
        if((i-1>=0&&DFS(board,word,i-1,j,index+1))
        ||(i+1<board.size()&&DFS(board,word,i+1,j,index+1))
        ||(j-1>=0&&DFS(board,word,i,j-1,index+1))
        ||(j+1<board[0].size()&&DFS(board,word,i,j+1,index+1)))
            return true;
        board[i][j]=temp;
        return false;
    }
};
```