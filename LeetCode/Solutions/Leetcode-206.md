1. 头插法

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
    ListNode* reverseList(ListNode* head) {
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