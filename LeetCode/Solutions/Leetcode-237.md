1. 移动节点值

```C++
class Solution {
public:
    void deleteNode(ListNode* node) {
        ListNode *pre=nullptr;
        while(node->next!=nullptr){
            node->val=node->next->val;
            pre=node;
            node=node->next;
        }
        pre->next=nullptr;
    }
};
```