1. 遍历
> 遍历矩阵，如果某个值为0，就将所在行和所在列的第一个数置为0，避免重复操作  
> 分别用两个布尔值标记第一行和第一列是否需要置0

```C++
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        // 标记第一行和第一列是否需要置0
        bool flag_rows=false;
        bool flag_cols=false;
        int rows=matrix.size(),cols=matrix[0].size();
        for(int i=0;i<rows;++i){
            if(matrix[i][0]==0)  flag_rows=true;
        }
        for(int j=0;j<cols;++j){
            if(matrix[0][j]==0)  flag_cols=true;
        }
        for(int i=1;i<rows;++i){
            for(int j=1;j<cols;++j){
                if(matrix[i][j]==0){
                    matrix[0][j]=0;
                    matrix[i][0]=0;
                }
            }
        }
        for(int i=1;i<rows;++i){
            if(matrix[i][0]==0){
                for(int j=1;j<cols;++j)  matrix[i][j]=0;
            }
        }
        for(int j=1;j<cols;++j){
            if(matrix[0][j]==0){
                for(int i=1;i<rows;++i)  matrix[i][j]=0;
            }
        }
        if(flag_rows==true){
            for(int i=0;i<rows;++i)  matrix[i][0]=0;
        }
        if(flag_cols==true){
            for(int j=0;j<cols;++j)  matrix[0][j]=0;
        }
    }
};
```