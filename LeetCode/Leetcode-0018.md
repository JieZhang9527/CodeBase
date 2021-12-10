1. 双指针法
> 该题和三数之和的不同以及注意点：
> - 不能像三数之和一样固定某点后提前判断退出，因为这里的目标值为target而不是0
> - 和三数之和有相同的去除重复方式
> - 四数之和有可能整型溢出，因此需要将右值临时量修改为long

```C++
class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> ans;
        if(nums.size()<4)   return ans;
        sort(nums.begin(),nums.end());
        for(int i=0;i<nums.size();++i){
            if(i>0&&nums[i]==nums[i-1]) continue;
            for(int j=i+1;j<nums.size();++j){
                if(j>i+1&&nums[j]==nums[j-1]) continue;
                int left=j+1, right=nums.size()-1;
                while(left<right){
                    long sum=(long)nums[i]+nums[j]+nums[left]+nums[right];
                    if(sum==target){
                        ans.push_back({nums[i],nums[j],nums[left],nums[right]});
                        while(left<right&&nums[left+1]==nums[left]) ++left;
                        while(left<right&&nums[right-1]==nums[right])   --right;
                        ++left;
                        --right;
                    }
                    else if(sum<target)  ++left;
                    else    --right;  
                }
            }
        }
        return ans;
    }
};
```