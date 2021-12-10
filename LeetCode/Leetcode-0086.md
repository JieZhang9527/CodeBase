1. 遍历
> 遍历链表节点分别加入新建的两个链表

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
    ListNode* partition(ListNode* head, int x) {
        ListNode *small_head=new ListNode(), *small_curr=small_head;
        ListNode *big_head=new ListNode(), *big_curr=big_head;
        while(head){
            ListNode *temp=head;
            head=head->next;
            if(temp->val<x){
                small_curr->next=temp;
                small_curr=small_curr->next;
            }
            else{
                big_curr->next=temp;
                big_curr=big_curr->next;
            }
        }
        small_curr->next=big_head->next;
        big_curr->next=NULL;
        return small_head->next;
    }
};
```