1. 中序遍历

```C++
class Solution {
public:
    bool findTarget(TreeNode* root, int k) {
        vector<int> nums;
        inOrder(root,nums);
        int left=0, right=nums.size()-1;
        while(left<right){
            int sum=nums[left]+nums[right];
            if(sum==k)  return true;
            else if(sum<k)  ++left;
            else    --right;  
        }
        return false;
    }
private:
    void inOrder(TreeNode *root, vector<int> &nums){
        if(!root)   return;
        stack<TreeNode*> st;
        while(root||!st.empty()){
            while(root){
                st.push(root);
                root=root->left;
            }
            if(!st.empty()){
                nums.push_back(st.top()->val);
                root=st.top()->right;
                st.pop();
            }
        }
    }
};
```