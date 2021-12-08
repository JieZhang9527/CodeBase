1. 回溯

> 如果ump[curr-sum]=i,则当前值为curr时，必定有i个差为sum的值

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
    int pathSum(TreeNode* root, int sum) {
        int ans=0;
        unordered_map<int,int> ump;
        //空树中和为0的路径有一个
        ump[0]=1;
        helper(root,sum,0,ans,ump);
        return ans;
    }
private:
    void helper(TreeNode *root,int sum,int curr,int &ans,unordered_map<int,int> &ump){
        if(!root)   return;
        curr+=root->val;
        if(ump.find(curr-sum)!=ump.end()) ans+=ump[curr-sum];
        ump[curr]++;
        helper(root->left,sum,curr,ans,ump);
        helper(root->right,sum,curr,ans,ump);
        //回溯时，返回上面的结点，要避免下层已访问节点对其他结点的影响
        ump[curr]--;
    }
};
```
2. 双递归

> 递归遍历二叉树的每个值，计算以其为根的二叉树，路径和为给定值的路径总数