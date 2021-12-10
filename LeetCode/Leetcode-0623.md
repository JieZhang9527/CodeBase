1. 层序遍历(BFS)

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
class Solution {
public:
    TreeNode* addOneRow(TreeNode* root, int v, int d) {
        if(d==1){
            TreeNode *Node=new TreeNode(v);
            Node->left=root;
            return Node;
        }
        levelOrder(root,v,d);
        return root;
    }
private:
    void levelOrder(TreeNode *root, int v, int d){
        if(!root)   return;
        int depth=1;
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty()){
            int count=q.size();
            for(int i=0;i<count;++i){
                auto temp=q.front();
                q.pop();
                if(depth==d-1){
                    TreeNode *leftNode=new TreeNode(v);
                    TreeNode *rightNode=new TreeNode(v);
                    leftNode->left=temp->left;
                    temp->left=leftNode;
                    rightNode->right=temp->right;
                    temp->right=rightNode;
                }
                if(temp->left) q.push(temp->left);
                if(temp->right) q.push(temp->right);
            }
            ++depth;
        }
    }
};
```

2. DFS(递归)

```C++
class Solution {
public:
    TreeNode* addOneRow(TreeNode* root, int v, int d) {
        if(d==1){
            TreeNode *Node=new TreeNode(v);
            Node->left=root;
            return Node;
        }
        DFS(root,v,d,1);
        return root;
    }
private:
    void DFS(TreeNode *root, int v, int d, int depth){
        if(!root)   return;
        if(depth==d-1){
            TreeNode *leftNode=new TreeNode(v);
            TreeNode *rightNode=new TreeNode(v);
            leftNode->left=root->left;
            rightNode->right=root->right;
            root->left=leftNode;
            root->right=rightNode;
        }
        DFS(root->left,v,d,depth+1);
        DFS(root->right,v,d,depth+1);
    }
};
```

3. DFS(非递归)

> 借助stack