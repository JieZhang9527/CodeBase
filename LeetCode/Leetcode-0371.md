1. 位运算

> 异或操作的一个重要特性是无进位加法:
> $$
    0 + 0 = 0  \\
    0 + 1 = 1  \\
    1 + 0 = 1  \\
    1 + 1 = 0（进位 1)  \\
> $$
> a ^ b 得到了一个无进位加法结果，如果要得到 a + b 的最终值，我们还要找到进位的数，把这二者相加。
在位运算中，我们可以使用与操作获得进位： ( a & b) << 1  
> 注意:
不进位加法结果与进位相加有可能再次造成进位，所以需要迭代处理，直到不再产生新的进位为止。当a & b的结果是负数时，左移就会造成符号位的溢出，所以此处需要转换为unsigned int来避免可能出现的左移越界行为。

```C++
class Solution {
public:
    int getSum(int a, int b) {
        while(b){
            int temp = a ^ b;
            b = ((unsigned int)(a & b)) << 1;
            a = temp;
        }
        return a;
    }
};
```