1. 大整型
> 创建大整型保存当前反转后可能溢出的数，虽然简化了溢出判断条件，但是不满足题目要求

```C++
class Solution {
public:
    int reverse(int x) {
        long ans=0;
        while(x){
            ans=ans*10+x%10;
            x/=10;
        }
        if(ans>INT_MAX||ans<INT_MIN)    return 0;
        return ans;
    }
};
```

2. 溢出判断
> 注意溢出条件需结合整型的最大值和最小值

```C++
class Solution {
public:
    int reverse(int x) {
        long ans=0;
        while(x){
            if(ans>INT_MAX/10||(ans==INT_MAX/10&&x%10>7))   return 0;
            if(ans<INT_MIN/10||(ans==INT_MIN/10&&x%10<-8))  return 0;
            ans=ans*10+x%10;
            x/=10;
        }
        return ans;
    }
};
```
