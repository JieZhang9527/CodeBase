1. 递归

```C++
class Solution {
public:
    vector<int> preorder(Node* root) {
        vector<int> ans;
        preOrder(root,ans);
        return ans;
    }
    void preOrder(Node *root,vector<int> &ans){
        if(!root)   return;
        ans.push_back(root->val);
        for(auto it : root->children)
            preOrder(it,ans);
    }
};

```

2. 非递归

> 将N叉树的最左边结点作为下一个要访问的结点，其余孩子结点要注意从右至左进栈，因为栈是后进先出的

```C++
/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/
class Solution {
public:
    vector<int> preorder(Node* root) {
        vector<int> ans;
        if(!root)   return ans;
        stack<Node*> st;
        while(root||!st.empty()){
            while(root){
                ans.push_back(root->val);
                for(int i=(root->children).size()-1;i>=1;--i)    st.push((root->children)[i]);            
                root=(root->children).size()?(root->children)[0]:nullptr;
            }
            if(!st.empty()){
                root=st.top();
                st.pop();
            }
        }
        return ans;
    }
};
```