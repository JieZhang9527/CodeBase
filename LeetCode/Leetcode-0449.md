1. 序列化二叉树

> 递归实现

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
class Codec {
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        stringstream ss;
        preOrder(root,ss);
        return ss.str();
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        stringstream ss(data);
        TreeNode *root=nullptr;
        rebuild(root,ss);
        return root;
    }
private:
    void preOrder(TreeNode *root,stringstream &ss){
        if(!root){
            ss<<"#"<<" ";
            return;
        }
        ss<<to_string(root->val)<<" ";
        preOrder(root->left,ss);
        preOrder(root->right,ss);
    }
    void rebuild(TreeNode *&root,stringstream &ss){
        string str;
        ss>>str;
        if(str=="#"){
            root=nullptr;
            return;
        }
        root=new TreeNode(stoi(str));
        rebuild(root->left,ss);
        rebuild(root->right,ss);
    }
};
```