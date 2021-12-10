1. 双指针法
> 本题关键是去除重复，排序是去重的前提  
> 三数可以固定一个数nums[i]，从两边分别遍历nums[left],nums[right] 
> 排序算法$O(Nlog(N))$,遍历$O(N^2)$,时间复杂度$O(N^2)$

```C++
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> ans;
        if(nums.size()<3)   return ans;
        sort(nums.begin(),nums.end());
        for(int i=0;i<nums.size();++i){
            int left=i+1, right=nums.size()-1;
            if(nums[i]>0)   break;
            if(i>0&&nums[i]==nums[i-1]) continue;
            while(left<right){
                int sum=nums[i]+nums[left]+nums[right];
                if(sum==0){
                    ans.push_back({nums[i],nums[left],nums[right]});
                    while(left<right&&nums[left+1]==nums[left]) ++left;
                    while(left<right&&nums[right-1]==nums[right])   --right;
                    ++left;
                    --right;
                }
                else if(sum<0)  ++left;
                else    --right;
            }
        }
        return ans;
    }
};
```