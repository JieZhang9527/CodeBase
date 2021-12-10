1. 栈
> 栈是反转的利器

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
    ListNode* reverseKGroup(ListNode* head, int k) {
        if(!head||!head->next)  return head;
        stack<ListNode*> st;
        ListNode *rever=new ListNode(), *curr=rever;
        while(head){
            // 用一个临时量复制head，处理剩余节小于k个
            ListNode *temp=head;
            while(temp&&st.size()<k){
                st.push(temp);
                temp=temp->next;
            }
            if(st.size()<k){
                curr->next=head;
                break;
            }
            while(!st.empty()){
                curr->next=st.top();
                st.pop();
                curr=curr->next;
            }
            // !! 避免环路
            curr->next=NULL;
            head=temp;
        }
        return rever->next;
    }
};
```