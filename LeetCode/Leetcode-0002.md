1. 模拟法
> 新建一个头节点head，简化链表创建

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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *head=new ListNode(-1);
        ListNode *curr=head;
        int carry=0;
        while(l1||l2){
            int a=l1?l1->val:0;
            int b=l2?l2->val:0;
            int sum=a+b+carry;
            carry=sum/10;
            curr->next=new ListNode(sum%10);
            curr=curr->next;
            if(l1)  l1=l1->next;
            if(l2)  l2=l2->next;
        }
        if(carry)   curr->next=new ListNode(carry);
        return head->next;
    }
};
```