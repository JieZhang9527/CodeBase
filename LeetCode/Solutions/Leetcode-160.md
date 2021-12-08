> 假设两条链表非公共部分长度分别为a,b，公共部分为c，则a+c+b=b+c+a

```C++
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode *currA=headA, *currB=headB;
        while(currA!=currB){
            if(currA)   currA=currA->next;
            else    currA=headB;
            if(currB)   currB=currB->next;
            else    currB=headA;
        }
        return currA;
    }
};
```