1. 数学题

> 问题的实质是求解n中包含的完全平方数，假设n=18，那么会在轮次：1，18，2，9，3，6反转，偶数次反转最终为灭，只有完全平方数，比如4，1，4，2，会变为奇数

```C++
class Solution {
public:
    int bulbSwitch(int n) {
        return sqrt(n);
    }
};
```