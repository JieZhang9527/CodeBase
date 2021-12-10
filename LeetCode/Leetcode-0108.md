1. 递归

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
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        return rebuild(nums,0,nums.size()-1);
    }
private:
    TreeNode* rebuild(vector<int> &nums, int left, int right){
        if(left>right)  return nullptr;
        int mid=(left+right)/2;
        TreeNode *root=new TreeNode(nums[mid]);
        root->left=rebuild(nums,left,mid-1);
        root->right=rebuild(nums,mid+1,right);
        return root;
    }
};
```