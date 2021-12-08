1. 中序遍历
> 交换的两个节点不满足中序递增，找到这两个节点并交换他们的值

```C++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    void recoverTree(TreeNode* root) {
        vector<TreeNode*> nodes;
        inOrder(root,nodes);
        int index1=-1, index2=-1;
        for(int i=1;i<nodes.size();++i){
            if(nodes[i]->val<nodes[i-1]->val){
                index1=i-1;
                break;
            }
        }
        for(int i=nodes.size()-2;i>=0;--i){
            if(nodes[i]->val>nodes[i+1]->val){
                index2=i+1;
                break;
            }
        }
        swap(nodes[index1]->val,nodes[index2]->val);
    }
private:
    void inOrder(TreeNode *root, vector<TreeNode*> &nodes){
        if(!root)   return;
        stack<TreeNode*> st;
        while(root||!st.empty()){   
            while(root){
                st.push(root);
                root=root->left;
            }
            if(!st.empty()){
                nodes.push_back(st.top());
                root=st.top()->right;
                st.pop();
            }
        }
    }
};
```
2. 中序遍历优化
> 找出排序数组中两个交换元素可在线性时间解决

```C++
class Solution {
public:
    void recoverTree(TreeNode* root) {
        vector<TreeNode*> nodes;
        inOrder(root,nodes);
        int index1=-1, index2=-1;
        for(int i=0;i<nodes.size()-1;++i){
            if(nodes[i+1]->val<nodes[i]->val){
                index2=i+1;
                if(index1==-1)  index1=i;
                else    break;
            }
        }
        swap(nodes[index1]->val,nodes[index2]->val);
    }
private:
    void inOrder(TreeNode *root, vector<TreeNode*> &nodes){
        if(!root)   return;
        stack<TreeNode*> st;
        while(root||!st.empty()){   
            while(root){
                st.push(root);
                root=root->left;
            }
            if(!st.empty()){
                nodes.push_back(st.top());
                root=st.top()->right;
                st.pop();
            }
        }
    }
};
```
3. 遍历时获取需要交换元素的指针

```C++
class Solution {
public:
    void recoverTree(TreeNode* root) {
        TreeNode *pointer1=nullptr,*pointer2=nullptr,*previous=nullptr;
        inOrder(root,previous,pointer1,pointer2);
        swap(pointer1->val,pointer2->val); 
    }
    void inOrder(TreeNode *root,TreeNode *&previous,TreeNode *&pointer1,TreeNode *&pointer2){
        stack<TreeNode*> st;
        TreeNode *temp=root;
        while(temp||!st.empty()){
            while(temp){
                st.push(temp);
                temp=temp->left;
            }
            if(!st.empty()){
                if(previous&&st.top()->val<previous->val){
                    pointer2=st.top();
                    if(!pointer1)   pointer1=previous;
                    else    break;
                }
                previous=st.top();
                temp=st.top()->right;
                st.pop();
            }
        }
    }
};
```