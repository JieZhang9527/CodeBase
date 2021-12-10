1. 二叉搜索树

```C++
class Solution {
public:
    bool findNumberIn2DArray(vector<vector<int>>& matrix, int target) {
        if(matrix.empty()||matrix[0].empty())   return false;
        int row=matrix.size()-1, col=0;
        while(row>=0&&col<matrix[0].size()){
            if(matrix[row][col]==target)    return true;
            else if(matrix[row][col]>target)    --row;
            else    ++col;
        }
        return false;
    }
};
```