1. 快慢指针
> 前面有道判断循环链表的题,查找的过程中是会循环到初始状态的,通过设置快慢指针,判断是否执行了一遍循环,从而作出判断

```C++
class Solution {
public:
    bool isHappy(int n) {
        int slow=n,fast=n;
        do{
            slow=everySquare(slow);
            fast=everySquare(fast);
            fast=everySquare(fast);
        }while(slow!=fast);
        return slow==1;
    }
    int everySquare(int n){
        int result=0;
        while(n){
            int temp=n%10;
            result+=temp*temp;
            n/=10;
        }
        return result;
    }
};
```