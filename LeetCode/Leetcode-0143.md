1. 快慢指针
> 快慢指针用于寻找链表中间节点。将原始链表分为左右两半部分，左面的保持原来的顺序,右面反转，然后将两个链表的结点依次连接。

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
    void reorderList(ListNode* head) {
        if(!head||!head->next)  return;
        ListNode *slow=head, *fast=head;
        while(fast->next&&fast->next->next){
            slow=slow->next;
            fast=fast->next->next;
        }
        ListNode *head1=head, *head2=slow->next;
        slow->next=NULL;
        head2=reverse(head2);
        ListNode *new_head=new ListNode(), *curr=new_head;
        while(head1&&head2){
            curr->next=head1;
            head1=head1->next;
            curr=curr->next;

            curr->next=head2;
            head2=head2->next;
            curr=curr->next;
        }    
        if(head1)   curr->next=head1;
        else if(head2)   curr->next=head2;  
        else    curr->next=NULL;
        head=new_head->next;
    }
private:
    ListNode *reverse(ListNode *head){
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