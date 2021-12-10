1. 快慢指针
> 假设起始节点到环入口节点长度为F，环入口到快慢指针相遇节点长度为a，相遇节点到环入口节点为b，则有：
> $$
2(F+a)=F+a+b+a
> $$
> 可得F=b，分别从相遇节点和头节点的分别遍历直至再次相遇，相遇节点即是入口节点


```C++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        if(!head||!head->next)  return NULL;
        // 避免初始化时slow==fast
        ListNode *slow=head->next;
        ListNode *fast=head->next->next;
        while(slow!=fast){
            if(!fast||!fast->next)  return NULL;
            slow=slow->next;
            fast=fast->next->next;
        }
        slow=head;
        while(slow!=fast){
            slow=slow->next;
            fast=fast->next;
        }
        return slow;
    }
};
```