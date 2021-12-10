1. 双指针

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
    ListNode* removeElements(ListNode* head, int val) {
        while(head&&head->val==val)    head=head->next; 
        if(!head)   return head;
        ListNode *pre=head, *curr=head->next;
        while(curr){
            while(curr&&curr->val==val) curr=curr->next;
            if(!curr){
                pre->next=NULL;
                break;
            }
            else{
                pre->next=curr;
                pre=curr;
                curr=curr->next;
            }
        }
        return head;
    }
};
```