1. 遍历
> 和螺旋矩阵遍历思路一致

```C++
class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        //创建二维矩阵
        vector<vector<int>> ans(n,vector<int>(n,0));
        int up=0,down=n-1,left=0,right=n-1;
        int count=1;
        while(true){
            for(int i=left;i<=right;++i)  ans[up][i]=count++;
            if(++up>down)  break;
            for(int i=up;i<=down;++i)  ans[i][right]=count++;
            if(--right<left)  break;
            for(int i=right;i>=left;--i)  ans[down][i]=count++;
            if(--down<up)  break;
            for(int i=down;i>=up;--i)  ans[i][left]=count++;
            if(++left>right)  break;
        }
        return ans;
    }
};
```