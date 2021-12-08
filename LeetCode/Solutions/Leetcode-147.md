1. 链表插入排序
> temp表示当前遍历结点,pre表示当前遍历结点的前一个结点，curr表示在已经排序的链表中遍历,找到插入位置后将当前结点插入
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
    ListNode* insertionSortList(ListNode* head) {
        ListNode* first=new ListNode(INT_MIN);
        first->next=head;
        ListNode* pre=first;
        while(head){
            ListNode* temp=head;
            head=head->next;
            ListNode* curr=first;
            while(curr){
                if(curr->next==temp){
                    pre=temp;  //!!!
                    break;
                } 
                else if(curr->val<=temp->val&&(curr->next)->val>temp->val){
                    pre->next=head;
                    temp->next=curr->next;
                    curr->next=temp;
                    break;
                }
                else  curr=curr->next;
            }
        }
        return first->next;
    }
};
```