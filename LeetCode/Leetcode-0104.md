1. DFS
> 递归

```C++
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if(!root)   return 0;
        return max(maxDepth(root->left),maxDepth(root->right))+1;
    }
};
```

2. BFS
> 二叉树层序遍历