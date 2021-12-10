1. 双指针
> 分别设置快慢指针，快指针一次走两步，慢指针一次走一步，则有以下两种情况：
> - 快指针落后慢指针一步，下一次相遇
> - 快指针落后慢指针两步，下一步变成上述情况

```C++
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if(!head)   return false;
        ListNode *slow=head, *fast=head->next;
        while(slow!=fast){
            if(!fast||!fast->next)  return false;
            slow=slow->next;
            fast=fast->next->next;
        }
        return true;
    }
};
```