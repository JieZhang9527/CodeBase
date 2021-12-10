1. 双指针法
> 新建new_head节点避免头节点特殊处理

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
    ListNode* deleteDuplicates(ListNode* head) {
        if(!head||!head->next)  return head;
        ListNode *new_head=new ListNode(INT_MAX);
        new_head->next=head;
        ListNode *pre=new_head;
        ListNode *left=head, *right=head->next;
        while(right){
            while(right&&left->val==right->val) right=right->next;
            if(left->next==right){
                pre->next=left;
                pre=pre->next;
                left=left->next;
                if(right)   right=right->next;
            }
            else{
                left=right;
                if(right)   right=right->next;
            }
        }
        // !!! 勿忘最后一部分
        pre->next=left;
        return new_head->next;
    }
};
```