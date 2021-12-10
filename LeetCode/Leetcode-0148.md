1. 归并排序
> 递归的形式实现归并排序

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
    ListNode* sortList(ListNode* head) {
        return mergeSort(head);
    }
private:
    ListNode *merge(ListNode *left, ListNode *right){
        ListNode *head=new ListNode(), *curr=head;
        while(left&&right){
            if(left->val<right->val){
                curr->next=left;
                left=left->next;
            }
            else{
                curr->next=right;
                right=right->next;
            }
            curr=curr->next;
        }
        if(left)    curr->next=left;
        if(right)   curr->next=right;
        return head->next;
    }
    ListNode *mergeSort(ListNode *head){
        if(!head||!head->next)  return head;
        ListNode *slow=head, *fast=head;
        while(fast->next&&fast->next->next){
            slow=slow->next;
            fast=fast->next->next;
        }
        ListNode *temp=slow->next;
        slow->next=NULL;
        ListNode *left=mergeSort(head);
        ListNode *right=mergeSort(temp);
        return merge(left,right);
    }
};
```