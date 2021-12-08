> 通用的解法是DFS或BFS寻找连通图的数量

> 本题的每个连通图都是矩形。可以这样计算：如果遍历到一个'X',如果它的上边或左边也是'X',说明已经计算过。

```C++
class Solution {
public:
    int countBattleships(vector<vector<char>>& board) {
        int ans=0;
        if(board.empty()||board[0].empty())  return ans;
        for(int i=0;i<board.size();++i){
            for(int j=0;j<board[0].size();++j){
                if(board[i][j]=='X'){
                    if((i-1>=0&&board[i-1][j]=='X')||(j-1>=0&&board[i][j-1]=='X'))
                        continue;
                    ++ans;
                }
            }
        }
        return ans;
    }
};
```