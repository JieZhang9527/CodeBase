1. 欧拉路径

> 按照字典序求解有向图的欧拉路径，欧拉路径：图是连通的，每个顶点的入度和出度相同  
> 寻找有向图的欧拉路径：Hierholzer算法:  
>从某个点出发，深度优先遍历到另一个顶点时需要删除这条边，如果没有可移动的边就将节点加入栈中，最后栈中保存的就是欧拉路径。

```C++
class Solution {
public:
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        //排序、去重、ID化
        vector<string> cities;
        for(const auto &ticket : tickets){
            cities.push_back(ticket[0]);
            cities.push_back(ticket[1]);
        }
        sort(cities.begin(),cities.end());
        cities.erase(unique(cities.begin(),cities.end()),cities.end());
        unordered_map<string,int> mp;
        for(int i=0;i<cities.size();++i)
            mp[cities[i]]=i;
        //邻接矩阵便于删除边，adjacents[i][j]表示i到j的路径数
        vector<vector<int>> adjacents(cities.size(),vector<int>(cities.size(),0));
        for(const auto &ticket : tickets)
            ++adjacents[mp[ticket[0]]][mp[ticket[1]]];
        vector<int> path;
        hierholzer(adjacents,mp["JFK"],path);
        vector<string> ans;
        for(auto i : path)  ans.push_back(cities[i]);
        reverse(ans.begin(),ans.end());
        return ans;
    }
    void hierholzer(vector<vector<int>> &adjacents,int start,vector<int> &path){
        for(int i=0;i<adjacents.size();++i){
            if(adjacents[start][i]>0){   
                --adjacents[start][i];
                hierholzer(adjacents,i,path);
            }
        }
        path.push_back(start);
    }
};
```