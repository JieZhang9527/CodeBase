1. 递归
> 先把链表转换为数组，使得能够随机存取

```C++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
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
    TreeNode* sortedListToBST(ListNode* head) {
        vector<int> list;
        while(head){
            list.push_back(head->val);
            head=head->next;
        }
        return build(list,0,list.size()-1);
    }
private:
    TreeNode* build(vector<int> &list, int left, int right){
        if(left>right)  return NULL;
        int mid=(left+right)/2;
        TreeNode *root=new TreeNode(list[mid]);
        root->left=build(list,left,mid-1);
        root->right=build(list,mid+1,right);
        return root;
    }
};
```