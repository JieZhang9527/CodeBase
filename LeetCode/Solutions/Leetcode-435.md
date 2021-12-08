1. 遍历

```C++
class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        int ans=0;
        if(intervals.size()<=1) return ans;
        sort(intervals.begin(),intervals.end(),[](vector<int> &a, vector<int> &b){return a[0]<b[0];});
        vector<vector<int>> temp;
        temp.push_back(intervals[0]);
        for(int i=1;i<intervals.size();++i){
            if(intervals[i][0]>=temp.back()[1]) temp.push_back(intervals[i]);
            else{
                ++ans;
                temp.back()[1]=min(temp.back()[1],intervals[i][1]);
            }
        }
        return ans;
    }
};
```