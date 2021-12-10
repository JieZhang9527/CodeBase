1. 二叉搜索
> 从矩阵的左下角看，类似于一棵二叉搜索树，向上变小，向右变大

```C++
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if(matrix.empty()||matrix[0].empty())   return false;
        int row=matrix.size()-1, col=0;
        while(row>=0&&col<matrix[0].size()){
            if(matrix[row][col]==target)    return true;
            else if(matrix[row][col]<target)    ++col;
            else --row;
        }
        return false;
    }
};
```