1. 归并排序
> 本题实质考察的是归并排序

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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if(lists.empty())   return NULL;
        return mergeList(lists,0,lists.size()-1);
    }
private:
    ListNode *merge(ListNode *head1, ListNode *head2){
        ListNode *head=new ListNode(), *curr=head;
        while(head1&&head2){
            if(head1->val<head2->val){
                curr->next=head1;
                head1=head1->next;
            }
            else{
                curr->next=head2;
                head2=head2->next;
            }
            curr=curr->next;
        }
        if(head1)   curr->next=head1;
        if(head2)   curr->next=head2;
        return head->next;
    }
    ListNode *mergeList(vector<ListNode*> &lists, int left, int right){
        if(left==right) return lists[left];
        int mid=(left+right)/2;
        ListNode *head1=mergeList(lists,left,mid);
        ListNode *head2=mergeList(lists,mid+1,right);
        return merge(head1,head2);
    }
};
```