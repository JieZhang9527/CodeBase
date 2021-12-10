1. 二分法
> div函数用于求取除数，注意需要将除数和被除数提前转换为long，否则除数为INT_MIN，被除数为-1时，结果越界

```C++
class Solution {
public:
    int divide(int dividend, int divisor) {
        if(divisor==0)  return 0;
        bool flag=true; // 记录结果正负
        if((dividend<0&&divisor>0)||(dividend>0&&divisor<0))    flag=false;
        long ans=div(abs(dividend),abs(divisor));
        if(ans>INT_MAX&&flag) ans=INT_MAX;
        return flag?ans:-ans;
    }
private:
    long div(long a, long b){
        if(a<b) return 0;
        long ans=1;
        long tb=b;
        while(tb+tb<=a){
            ans*=2;
            tb*=2;
        }
        return ans+div(a-tb,b);
    }
};
```