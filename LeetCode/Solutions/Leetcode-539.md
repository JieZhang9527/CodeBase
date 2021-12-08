1. 遍历

> 解决数组首尾相接问题，可以在数组后面添加一个相同的数组
> help数组记录某时间点出现的次数。比如换算为分钟数的时间点为time,则help[time]++,help[24*60+time]++，遍历help数组寻找最小时间间隔。

```C++
class Solution {
public:
    int findMinDifference(vector<string>& timePoints) {
        vector<int> help(2*24*60+1,0);
        for(const auto &point : timePoints){
            int time=stoi(string(point.begin(),point.begin()+2))*60+
                        stoi(string(point.begin()+3,point.end()));
            help[time]++;
            help[24*60+time]++;
        }
        int ans=INT_MAX;
        int pre=-1;
        for(int i=0;i<2*24*60+1;++i){
            if(help[i]>1)  return 0;
            if(help[i]==1){
                if(pre!=-1)  ans=min(ans,i-pre);
                pre=i;
            }
        }
        return ans;
    }
};
```