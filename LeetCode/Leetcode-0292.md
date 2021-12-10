1. 数学题

> 如果是4的倍数个，对方总可以让你变为n-4,如此循环到只剩4个，就赢不了

```C++
class Solution {
public:
    bool canWinNim(int n) {
        return n%4!=0;
    }
};
```