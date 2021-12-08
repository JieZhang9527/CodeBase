1. 位运算

> 二进制位数与num相同且全为1的数与num异或运算就是结果 

```C++
class Solution {
public:
    int findComplement(int num) {
        int temp=0,copy=num;
        while(copy){
            copy >>= 1;
            temp=(temp<<1)+1;
        }
        return temp^num;
    }
};
```