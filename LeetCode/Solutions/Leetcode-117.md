1. 层序遍历

```C++
class Solution {
public:
    Node* connect(Node* root) {
        if(!root)   return root;
        queue<Node*> q;
        q.push(root);
        Node *pre=NULL;
        while(!q.empty()){
            int count=q.size();
            for(int i=0;i<count;++i){
                auto temp=q.front();
                q.pop();
                if(i>0) pre->next=temp;
                pre=temp;
                if(temp->left)  q.push(temp->left);
                if(temp->right) q.push(temp->right);
            }
        }
        return root;
    }
};
```