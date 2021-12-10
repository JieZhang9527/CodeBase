1. 贪心算法

> 当前一支箭应该引爆含有当前起始气球开始尽可能多的气球，也就是说当前的箭位置应该是当前起始气球的最右端。

```C++
class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        if(points.empty())  return 0;
        sort(points.begin(),points.end(),[](vector<int> &a,vector<int> &b){return a[0]==b[0]?a[1]<b[1]:a[0]<b[0];});
        int ans=0;
        int remote=points[0][1];
        for(int i=0;i<points.size();++i){
            // !!! remote应该可能会因为后续而变小
            if(points[i][0]<=remote)    remote=min(remote,points[i][1]);
            else{
                remote=points[i][1];
                ++ans;
            }
        }
        ++ans;
        return ans;
    }
};
```