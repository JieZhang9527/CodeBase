1. 快慢指针
> 快指针先走，将链表截断  
> 注意K可能大于链表长度，因此需要先求余

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
    ListNode* rotateRight(ListNode* head, int k) {
        if(!head||!head->next)  return head;  
        int len=0;
        ListNode *curr=head;
        while(curr){
            len++;
            curr=curr->next;
        }
        k=k%len;
        if(k==0)    return head;
        ListNode *slow=head, *fast=head;
        for(int i=0;i<k;++i)    fast=fast->next;
        while(fast->next){
            slow=slow->next;
            fast=fast->next;
        }   
        ListNode *new_head=slow->next;
        slow->next=NULL;
        fast->next=head;
        return new_head;
    }
};
```