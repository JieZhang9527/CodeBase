1. 技巧题

> $38=(3*1+3*9)+8$，也就是说第一次运算的结果是38对9取余的结果，重复就可得到结果  
> $99=(9*1+9*9)+9$，对9取余，结果为0，为了避免这种情况，打破这种条件，num减一后来再加一

```C++
class Solution {
public:
    int addDigits(int num) {
        return (num-1)%9+1;
    }
};
```