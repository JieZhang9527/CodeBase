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
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        ListNode *fake=new ListNode();
        fake->next=head;    head=fake;
        ListNode *slow=head, *fast=head;
        for(int i=0;i<n;++i)    fast=fast->next;
        for(int i=0;i<m-1;++i)  slow=slow->next;
        ListNode *left=slow, *mid=slow->next, *right=fast->next;
        slow->next=NULL;    fast->next=NULL;
        ListNode *curr=reverse(mid);
        left->next=curr;
        while(curr->next)   curr=curr->next;
        curr->next=right;
        return head->next;
    }
private:
    ListNode *reverse(ListNode *head){
        ListNode *newHead=NULL;
        while(head){
            ListNode *temp=head;
            head=head->next;
            temp->next=newHead;
            newHead=temp;
        }
        return newHead;
    }
};
```