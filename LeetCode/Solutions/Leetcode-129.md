1. 层序遍历
> 需要修改二叉树的值

```C++
class Solution {
public:
    int sumNumbers(TreeNode* root) {
        if(!root)   return 0;
        queue<TreeNode*> q;
        q.push(root);
        int ans=0;
        while(!q.empty()){
            int count=q.size();
            for(int i=0;i<count;++i){
                TreeNode *temp=q.front();
                q.pop();
                if(!temp->left&&!temp->right)   ans+=temp->val;
                if(temp->left){
                    temp->left->val+=temp->val*10;
                    q.push(temp->left);
                }
                if(temp->right){
                    temp->right->val+=temp->val*10;
                    q.push(temp->right);
                }
            }
        }
        return ans;
    }
};
```


2. 递归

```C++
class Solution {
public:
    int sumNumbers(TreeNode* root) {
        return DFS(root,0);
    }
private:
    int DFS(TreeNode *root, int val){
        if(!root)   return 0;
        val=val*10+root->val;
        if(!root->left&&!root->right)   return val;
        return DFS(root->left,val)+DFS(root->right,val);
    }
};
```