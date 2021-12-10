1. 双指针法
> 指针从两头向中间走，下一步移动高度较小的那条边，因为只有这样才有可能在X轴缩小的情况下，增大面积值

```C++
class Solution {
public:
    int maxArea(vector<int>& height) {
        int ans=0;
        int left=0, right=height.size()-1;
        while(left<right){
            ans=max(ans,min(height[left],height[right])*(right-left));
            height[left]<height[right]?++left:--right;
        }
        return ans;
    }
};
```