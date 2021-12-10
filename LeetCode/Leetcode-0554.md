1. 哈希

> 计算每个缝隙的位置，缝隙最多的垂线穿过最少的砖墙，unordered_map记录每个缝隙，及其个数

```C++
class Solution {
public:
    int leastBricks(vector<vector<int>>& wall) {
        if(wall.empty()||wall[0].empty())   return 0;
        unordered_map<int,int> ump;
        for(int i=0;i<wall.size();++i){
            int curr=0;
            for(int j=0;j<wall[i].size()-1;++j){
                curr+=wall[i][j];
                ++ump[curr];
            }
        } 
        int max_gap=0;
        for(auto &it : ump)
            max_gap=max(max_gap,it.second);
        return wall.size()-max_gap;
    }
};
```

