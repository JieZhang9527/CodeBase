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
    ListNode* deleteDuplicates(ListNode* head) {
        if(!head||!head->next)  return head;
        ListNode *slow=head, *fast=head;
        while(fast){
            if(slow->val!=fast->val){
                slow->next=fast;
                slow=slow->next;
            }
            fast=fast->next;
        }
        slow->next=NULL;
        return head;
    }
};
```