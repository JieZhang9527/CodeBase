1. 位运算
> 运用布莱恩·柯林汉算法: n & (n-1) 去除二进制位中最右边的一个1  
> 如果一个数是2的幂次方,则必然二进制位中只有一个1

```C++
class Solution {
public:
    bool isPowerOfTwo(int n) {
        // n & (n-1) 去除最右边的一个1
        return n>0 && (n & (n-1))==0;
    }
};
```