1. 双指针法

```C++
class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string> ans;
        if(nums.empty())    return ans;
        int left=0, right=0;
        while(right<nums.size()){
            while(right<nums.size()&&(right==left||nums[right]==nums[right-1]+1)) 
                ++right;
            string temp="";
            if(nums[left]==nums[right-1]){
                temp+=to_string(nums[left]);
            }
            else{
                temp+=to_string(nums[left])+"->"+to_string(nums[right-1]);
            }
            ans.push_back(temp);
            left=right;
        }
        return ans;
    }
};
```