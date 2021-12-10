1. DFS
> 对图上的每个点操作，涉及BFS和DFS  

```C++
class Solution {
public:
    Node* cloneGraph(Node* node) {
        unordered_map<Node*,Node*> visited;
        return DFS(node,visited);
    }
    Node *DFS(Node *node,unordered_map<Node*,Node*> &visited){
        if(!node)   return nullptr;
        if(visited.find(node)!=visited.end())   return visited[node];
        Node *clone=new Node(node->val);
        visited[node]=clone;
        for(auto it : node->neighbors){
            (clone->neighbors).push_back(DFS(it,visited));
        }
        return clone;
    }
};
```

1. BFS
> 对原始图广度优先遍历，没遍历到一个节点修改对应的克隆节点的邻接点，原节点和克隆节点对采用哈希存储

```C++
class Solution {
public:
    Node* cloneGraph(Node* node) {
        if(!node)   return nullptr;
        unordered_map<Node*,Node*> visited;
        queue<Node*> q;
        Node *temp=node;
        q.push(temp);
        visited[temp]=new Node(temp->val);
        while(!q.empty()){
            temp=q.front();
            q.pop();
            for(auto it : temp->neighbors){
                if(visited.find(it)==visited.end()){
                    q.push(it);
                    visited[it]=new Node(it->val);
                }
                visited[temp]->neighbors.push_back(visited[it]);
            }
        }
        return visited[node];
    }
};
```