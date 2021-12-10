1. 滑动窗口

```C++
class Solution {
public:
    int minSubArrayLen(int s, vector<int>& nums) {
        if(nums.empty())    return 0;
        int ans=INT_MAX;
        int left=0, right=0;
        int sum=0;
        while(right<nums.size()){
            sum+=nums[right];
            while(sum>=s){
                ans=min(ans,right-left+1);
                sum-=nums[left];
                ++left;
            }
            ++right;
        }
        return ans==INT_MAX?0:ans;
    }
};
```