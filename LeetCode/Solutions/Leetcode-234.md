1. 快慢指针

> 快慢指针用于二分链表，采用头插法反转链表

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
    bool isPalindrome(ListNode* head) {
        if(!head||!head->next)   return true;
        ListNode *slow=head, *fast=head;
        ListNode *pre=NULL;
        while(fast&&fast->next){
            pre=slow;
            slow=slow->next;
            fast=fast->next->next;
        }
        pre->next=NULL;
        if(fast)    slow=slow->next;
        ListNode *new_head=reverse(slow);
        while(head&&new_head){
            if(head->val!=new_head->val)    return false;
            head=head->next;
            new_head=new_head->next;
        }
        if(head||new_head)  return false;
        return true;
    }
private:
    ListNode *reverse(ListNode *head){
        if(!head)   return head;
        ListNode *new_head=NULL;
        while(head){
            ListNode *temp=head;
            head=head->next;
            temp->next=new_head;
            new_head=temp;
        }
        return new_head;
    }
};
```