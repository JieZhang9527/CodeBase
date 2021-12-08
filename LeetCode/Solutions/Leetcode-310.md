1. BFS

> 像洋葱一样一层一层向内剥，每次剥掉一层叶子节点  
> 终止条件：最后根节点的数量只可能为1个或2个节点（可以图解，如果为3个及以上，则必定出现环）

```C++
class Solution {
public:
    vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {
        vector<int> ans;
        vector<int> degrees(n,0); //保存每个节点的度
        vector<vector<int>> adjacents(n,vector<int>());
        for(auto edge : edges){
            adjacents[edge[0]].push_back(edge[1]);
            adjacents[edge[1]].push_back(edge[0]);
            degrees[edge[0]]++;
            degrees[edge[1]]++;
        }
        queue<int> leaf;
        for(int i=0;i<n;++i){
            if(degrees[i]==1)   leaf.push(i);   //叶节点度为1
        }
        if(n==1)  ans.push_back(0);   //特殊处理
        while(n!=1&&n!=2){
            int count=leaf.size();
            for(int i=0;i<count;++i){
                int temp=leaf.front();  leaf.pop();
                --n;    //剩余节点个数减一
                for(auto it : adjacents[temp]){
                    if(--degrees[it]==1)    leaf.push(it);
                }
            }
        }
        while(!leaf.empty()){
            ans.push_back(leaf.front());
            leaf.pop();
        }
        return ans;
    }
};
```