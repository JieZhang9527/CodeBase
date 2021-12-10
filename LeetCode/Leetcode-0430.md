1. 栈

> 利用栈存储每次处理链表的后半部分

```C++
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* prev;
    Node* next;
    Node* child;
};
*/
class Solution {
public:
    Node* flatten(Node* head) {
        Node* root=head;
        stack<Node*> st;
        Node *target=nullptr;
        while(helper(root,target)){
            st.push(target->next);
            target->next=target->child;
            target->child->prev=target;
            target->child=nullptr;
            root=target->next;
        }
        while(!st.empty()){
            while(root->next) root=root->next;   
            Node *start=st.top();st.pop();
            if(root&&start){
                root->next=start;
                start->prev=root;
            }
        }
        return head;
    }
    bool helper(Node* head,Node* &target){
        while(head){
            if(head->child){
                target=head;
                return true;
            }
            head=head->next;
        }
        return false;
    }
};
```