1. 贪心算法
> min_left表示每个孩子像左看，至少需要多少糖果；min_right表示每个孩子向右看，至少需要的糖果；取左右两边的大者即是最少需要的糖果数。

```C++
class Solution {
public:
    int candy(vector<int>& ratings) {
        vector<int> min_left(ratings.size(),1);
        vector<int> min_right(ratings.size(),1);
        for(int i=1;i<ratings.size();++i){
            if(ratings[i]>ratings[i-1]) min_left[i]=min_left[i-1]+1;
        }
        for(int i=ratings.size()-2;i>=0;--i){
            if(ratings[i]>ratings[i+1]) min_right[i]=min_right[i+1]+1;
        }
        int ans=0;
        for(int i=0;i<ratings.size();++i){
            ans+=max(min_left[i],min_right[i]);
        }
        return ans;
    }
};
```