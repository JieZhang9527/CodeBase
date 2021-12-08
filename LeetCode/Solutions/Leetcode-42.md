1. dp
> 记录每个点左侧和右侧最高点的高度

```C++
class Solution {
public:
    int trap(vector<int>& height) {
        if(height.size()<3) return 0;
        vector<int> max_left(height.size(),0);
        vector<int> max_right(height.size(),0);
        for(int i=1;i<height.size()-1;++i)  max_left[i]=max(max_left[i-1],height[i-1]);
        for(int i=height.size()-2;i>0;--i)  max_right[i]=max(max_right[i+1],height[i+1]);
        int ans=0;
        for(int i=1;i<height.size()-1;++i){
            ans+=max(0,min(max_left[i],max_right[i])-height[i]);
        }
        return ans;
    }
};
```