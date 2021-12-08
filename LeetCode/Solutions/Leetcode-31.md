1. 贪心
> 从后向前遍历，寻找该数后大于当前值的最小值并和当前值交换，将其后所有值从小到大排列

```C++
class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        if(nums.size()<=1)  return;
        for(int i=nums.size()-2;i>=0;--i){
            int index=-1, val=INT_MAX;
            for(int j=nums.size()-1;j>i;--j){
                if(nums[j]>nums[i]&&nums[j]<val){
                    index=j;
                    val=nums[j];
                }
            }
            if(index!=-1){
                swap(nums[i],nums[index]);
                sort(nums.begin()+i+1,nums.end());
                return;
            }
        }
        reverse(nums.begin(),nums.end());
    }
};
```