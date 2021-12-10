1. 层序遍历

```C++
class Solution {
public:
    vector<vector<int>> levelOrder(Node* root) {
        vector<vector<int>> ans;
        if(!root)   return ans;
        queue<Node*> q;
        Node *temp=root;
        q.push(temp);
        while(!q.empty()){
            int count=q.size();
            vector<int> curr;
            for(int i=0;i<count;++i){
                temp=q.front();
                q.pop();
                curr.push_back(temp->val);
                for(auto node : temp->children)
                    q.push(node);
            }
            ans.push_back(curr);
        }
        return ans;
    }
};
```