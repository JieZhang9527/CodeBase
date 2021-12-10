1. 链表操作
> 新建伪头节点，避免头节点的额外处理

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
    ListNode* swapPairs(ListNode* head) {
        if(!head||!head->next)  return head;
        ListNode *node=new ListNode();
        node->next=head;
        ListNode *curr=node;
        ListNode *left=head, *right=head->next;
        while(left&&right){
            curr->next=right;
            left->next=right->next;
            right->next=left;
            if(left->next){
                right=left->next->next;
                left=left->next;
                curr=curr->next->next;
            }
            else    break;
        }
        return node->next;
    }
};
```