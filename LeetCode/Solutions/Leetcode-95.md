1. 递归
> - 遍历每个节点为根节点
> - 根节点左侧为左子树，右侧为右子树
> - 对左右子树的每个节点，分别将其设置为根节点

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
    vector<TreeNode*> generateTrees(int n) {
        if(n==0)    return vector<TreeNode*>();
        return constructBinarySearchTree(1,n);
    }
    vector<TreeNode*> constructBinarySearchTree(int start,int end){
        vector<TreeNode*> answer;
        if(start>end)   answer.push_back(NULL);
        for(int i=start;i<=end;++i){
            vector<TreeNode*> left=constructBinarySearchTree(start,i-1);
            vector<TreeNode*> right=constructBinarySearchTree(i+1,end);
            for(auto l : left){
                for(auto r : right){
                    TreeNode *root=new TreeNode(i);
                    root->left=l;
                    root->right=r;
                    answer.push_back(root);
                }
            }
        }
        return answer;
    }
};
```