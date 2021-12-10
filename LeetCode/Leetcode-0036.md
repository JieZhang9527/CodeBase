1. hash
> 设置三个哈希数组分别记录行、列、九宫格是否出现了这个数字  
> 九宫格按照从左到右，从上到下划定序号

```C++
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int hash[9][9]={0};//用于判断九宫格的重复性
        int hash_rows[9][9]={0};//判断行的重复性
        int hash_cols[9][9]={0};//判断列的重复性
        for(int rows=0;rows<9;++rows){
            for(int cols=0;cols<9;++cols){
                int temp=transform(board[rows][cols]);
                if(temp==-1)  continue;
                if(hash_rows[rows][temp]==1)  return false;
                else  hash_rows[rows][temp]=1;
                if(hash_cols[cols][temp]==1)  return false;
                else  hash_cols[cols][temp]=1;
                if(hash[(rows/3)*3+cols/3][temp]==1) return false;
                else   hash[(rows/3)*3+cols/3][temp]=1;
            }
        }
        return true;
    }
    int transform(char c){
        if(c>='1'&&c<='9')  return c-'1';
        else  return -1;
    }
};
```