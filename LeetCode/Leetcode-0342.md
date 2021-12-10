1. 位运算

> 4的幂是2的幂的特殊情况,在2的幂的基础上要求1所在的位置是二进制的偶数位
0x55555555 = 0101 0101 0101 0101 0101 0101 0101 0101  
> 注意: (num & (num-1)) == 0  与运算一定要加上括号，为了不引起算数优先级问题,尽量都加上括号。

```C++
class Solution {
public:
    bool isPowerOfFour(int num) {
        return num>0 && ((num & (num-1)) ==0) && (num & 0x55555555);
    }
};
```