1. 旋转矩阵
> 先旋转整个数组，然后按正对角线交换两边的数
$$
\begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{bmatrix} 
\quad
\begin{bmatrix} 7 & 8 & 9 \\ 4 & 5 & 6 \\ 1 & 2 & 3 \end{bmatrix}
\quad
\begin{bmatrix} 7 & 4 & 1 \\ 8 & 5 & 2 \\ 9 & 6 & 3 \end{bmatrix}
$$

```C++
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        if(matrix.empty()||matrix[0].empty())   return;
        int rows=matrix.size(), cols=matrix[0].size();
        for(int i=0;i<rows/2;++i)   swap(matrix[i],matrix[rows-i-1]);
        for(int i=0;i<rows;++i){
            for(int j=i+1;j<cols;++j){
                swap(matrix[i][j],matrix[j][i]);
            }
        }
    }
};
```