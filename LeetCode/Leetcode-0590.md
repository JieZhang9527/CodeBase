1. 递归

```C++
class Solution {
public:
    vector<int> postorder(Node* root) {
        vector<int> ans;
        postOrder(root,ans);
        return ans;
    }
    void postOrder(Node *root,vector<int> &ans){
        if(!root)   return;
        for(auto it : root->children)
            postOrder(it,ans);
        ans.push_back(root->val);
    }
};
```

2. 非递归

> 转化为修改后的先序遍历：
> 二叉树的先序遍历：根左右，将其改为：根右左，结果翻转就是：左右根，得到后序遍历结果。同理，N叉树先序：根左中右，改为：根右中左，翻转：左中右根

```C++
class Solution {
public:
    vector<int> postorder(Node* root) {
        vector<int> ans;
        if(!root)   return ans;
        stack<Node*> st;
        while(root||!st.empty()){
            while(root){
                ans.push_back(root->val);
                int len=(root->children).size();
                for(int i=0;i<len-1;++i)
                    st.push((root->children)[i]);
                if(len>0)   root=(root->children)[len-1];
                else    root=NULL;
            }
            if(!st.empty()){    //!!!
                root=st.top();
                st.pop();
            }
        }
        reverse(ans.begin(),ans.end());
        return ans;
    }
};
```