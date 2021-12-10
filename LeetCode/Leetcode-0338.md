1. 位运算

> 奇数一定比前面那个偶数多一个 1，因为多的就是最低位的 1。  
> 偶数中 1 的个数一定和除以 2 之后的那个数一样多。因为最低位是 0，除以 2 就是右移一位，也就是把那个 0 抹掉而已，所以 1 的个数是不变的

```C++
class Solution {
public:
    vector<int> countBits(int num) {
        vector<int> ans(num+1,0);
        for(int i=0;i<=num;++i){
            if( 1 & i)  ans[i]=ans[i-1]+1;  //如果为奇数
            else    ans[i]=ans[i/2];
        }
        return ans;
    }
};
```