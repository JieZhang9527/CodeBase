1. 暴力模拟

> 统一从一个方向遍历，方向不同的入栈再退栈

```C++
class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& matrix) {
        vector<int> ans;
        if(matrix.empty()||matrix[0].empty())  return ans;
        int rows=matrix.size(),cols=matrix[0].size();
        int i=0,j=0;
        while(i+j<=rows+cols-2){
            if((i+j)%2){
                for(;j>=0;++i,--j)
                    ans.push_back(matrix[i][j]);
                --i;++j;
                if(j+1<cols)  ++j;
                else if(i+1<rows)  ++i;
            }
            else{
                for(;i>=0;--i,++j)
                    ans.push_back(matrix[i][j]);
                ++i,--j;
                if(i+1<rows)  ++i;
                else if(j+1<cols)  ++j;
            }
        }
        return ans;
    }
};
```