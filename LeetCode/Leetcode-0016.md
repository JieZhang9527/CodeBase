1. 双指针法
> 注意初始化方式

```C++
class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(),nums.end());
        int ans=nums[0]+nums[1]+nums[2];
        for(int i=0;i+2<nums.size();++i){
            int left=i+1, right=nums.size()-1;
            while(left<right){
                int temp=nums[i]+nums[left]+nums[right];
                if(abs(temp-target)<abs(ans-target))
                    ans=temp;
                if(temp==target)    break;
                else if(temp>target)    --right;
                else    ++left;
            }
        }
        return ans;
    }
};
```