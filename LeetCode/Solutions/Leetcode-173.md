1. 中序遍历
> 非递归中序遍历，但是要记录当前遍历节点和栈的状态，使用全局变量
```C++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class BSTIterator {
public:
    BSTIterator(TreeNode* root) {
        curr=root;
    }
    
    /** @return the next smallest number */
    int next() {
        int ans=0;
        while(curr||!st.empty()){
            while(curr){
                st.push(curr);
                curr=curr->left;
            }
            if(!st.empty()){
                ans=st.top()->val;
                curr=st.top()->right;
                st.pop();
                break;
            }
        }
        return ans;
    }
    
    /** @return whether we have a next smallest number */
    bool hasNext() {
        return curr||!st.empty();
    }
private:
    stack<TreeNode*> st;
    TreeNode *curr=nullptr;
};
```