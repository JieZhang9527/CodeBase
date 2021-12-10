1. 遍历

> 遍历链表，将奇结点放在一个链表，偶结点放在一个链表  
> 注意：要在原链表上修改，否则不满足空间复杂度O(1)

```C++
class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
        if(!head||!head->next)  return head;
        ListNode *odd_head=new ListNode(), *even_head=new ListNode();
        ListNode *odd=odd_head, *even=even_head;
        ListNode *curr=head;
        int count=0;
        while(curr){
            ++count;
            if(count%2==0){
                even->next=curr;
                even=even->next;
            }
            else{
                odd->next=curr;
                odd=odd->next;
            }
            curr=curr->next;
        }
        odd->next=even_head->next;
        even->next=NULL;
        return odd_head->next;
    }
};
```