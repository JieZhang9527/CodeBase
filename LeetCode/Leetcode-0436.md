1. 哈希

> mp.lower_bound(k)  查找第一个关键字大于等于k的元素，返回其迭代器

```C++
class Solution {
public:
    vector<int> findRightInterval(vector<vector<int>>& intervals) {
        map<int,int> mp;
        for(int i=0;i<intervals.size();++i) mp[intervals[i][0]]=i;
        vector<int> ans;
        for(int i=0;i<intervals.size();++i){
            auto it=mp.lower_bound(intervals[i][1]);
            it==mp.end()?ans.push_back(-1):ans.push_back(it->second);
        }
        return ans;
    }
};
```