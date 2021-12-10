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
class Codec {
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        stringstream ss;
        help(root,ss);
        return ss.str();
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        stringstream ss(data);
        TreeNode *root;
        rebuild(root,ss);
        return root;
    }
private:
    void help(TreeNode *root, stringstream &ss){
        if(!root){
            ss<<"#";
            return;
        }
        ss<<to_string(root->val);
        ss<<" ";
        help(root->left, ss);
        ss<<" ";
        help(root->right,ss);
    }
    void rebuild(TreeNode *&root,stringstream &ss){
        string temp;
        ss>>temp;
        if(temp=="#"){
            root=NULL;
            return;
        }
        root=new TreeNode(stoi(temp));
        rebuild(root->left,ss);
        rebuild(root->right,ss);
    }
};
```