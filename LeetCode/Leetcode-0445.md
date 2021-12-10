1. 双栈

> 可以采用头插法或栈反转链表

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
        stack<ListNode*> st1, st2;
        while(l1){
            st1.push(l1);
            l1=l1->next;
        }
        while(l2){
            st2.push(l2);
            l2=l2->next;
        }
        ListNode *new_head=NULL;
        int carry=0;
        while(!st1.empty()||!st2.empty()){
            int a=st1.empty()?0:st1.top()->val;
            int b=st2.empty()?0:st2.top()->val;
            int temp=carry+a+b;
            ListNode *node=new ListNode(temp%10);
            carry=temp/10;
            node->next=new_head;
            new_head=node;
            if(!st1.empty())    st1.pop();
            if(!st2.empty())    st2.pop();
        }
        if(carry){
            ListNode *node=new ListNode(carry);
            node->next=new_head;
            new_head=node;
        }
        return new_head;
    }
};
```