1. 遍历

> 如果是全部乘起来然后除以每个数，如果这个数是0，就会出问题  
> 左右乘积列表，L[i]表示左边的乘积，R[i]表示右边的乘积

```C++
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> ans(nums.size(),0);
        vector<int> left(nums.size(),0), right(nums.size(),0);
        left[0]=1;  right[nums.size()-1]=1;
        for(int i=1;i<nums.size();++i)  left[i]=left[i-1]*nums[i-1];
        for(int i=nums.size()-2;i>=0;--i)   right[i]=right[i+1]*nums[i+1];
        for(int i=0;i<nums.size();++i)  ans[i]=left[i]*right[i];
        return ans;
    }
};
```