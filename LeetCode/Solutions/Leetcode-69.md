1. 二叉搜索
> 为了缩小搜索范围，值的一半的平方一般大于这个值，例外：0 1 2 3 4，0和1需要特殊判断

```C++
class Solution {
public:
    int mySqrt(int x) {
        if(x==0||x==1)    return x;
        int left=0, right=x/2;
        while(left<right){
            // 取右中位数，防止陷入死循环
            long mid=(left+right+1)/2;
            if(mid*mid==x)  return mid;
            // 结果只保留整数部分，注意更新值
            else if(mid*mid>x)  right=mid-1;
            else    left=mid;   
        }
        return left;
    }
};
```