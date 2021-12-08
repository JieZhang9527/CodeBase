1. 数学

> [a,b,c,d] 改变优先级使得 a/b/c/d 最大  
p/q最大，应该使得p大，q小  
数组中的每个数都是正整数，因此a不除以任何数就是最大数  
目标：使得b/c/d最小  
(b/c)/d  b/(c*d)  
b/(c/d)  (b*d)/c  
解得d=1时，两者相等，因此 b/(c/d) >= (b/c)/d  
因此，答案是 a/(b/c/d)  


```C++
class Solution {
public:
    string optimalDivision(vector<int>& nums) {
        if(nums.size()==1)  return to_string(nums[0]);
        if(nums.size()==2)  return to_string(nums[0])+'/'+to_string(nums[1]);
        string ans=to_string(nums[0])+"/("+to_string(nums[1]);
        for(int i=2;i<nums.size();++i)
            ans+='/'+to_string(nums[i]);
        ans+=')';
        return ans;
    }
};
```