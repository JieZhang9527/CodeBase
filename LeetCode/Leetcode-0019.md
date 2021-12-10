1. 双指针法
> 添加一个头节点，使得头节点和非头节点的删除相同，设置快慢指针，快指针走到末尾时，慢指针走到要删除节点的前一个节点

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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        // 添加一个头节点，避免删除头节点比较麻烦
        ListNode *node=new ListNode();
        node->next=head;    head=node;
        ListNode *slow=head, *fast=head;
        for(int i=0;i<=n;++i)   fast=fast->next;
        while(fast){
            slow=slow->next;
            fast=fast->next;
        }
        slow->next=slow->next->next;
        return head->next;
    }
};
```