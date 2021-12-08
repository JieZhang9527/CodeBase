1. 记忆化搜索

> help(left,right) 将(left,right)填满气球可获得的硬币数目

```C++
class Solution {
public:
    int maxCoins(vector<int>& nums) {
        nums.insert(nums.begin(),1);
        nums.push_back(1);
        vector<vector<int>> ans(nums.size(),vector<int>(nums.size(),-1));
        return help(0,nums.size()-1,nums,ans);
    }
private:
    int help(int left, int right,vector<int> &nums,vector<vector<int>> &ans){
        if(right-left<=1){
            ans[left][right]=0;
            return 0;
        }
        if(ans[left][right]!=-1)    return ans[left][right];
        for(int i=left+1;i<right;++i){
            int sum=nums[left]*nums[i]*nums[right];
            sum+=help(left,i,nums,ans)+help(i,right,nums,ans);
            ans[left][right]=max(ans[left][right],sum);
        }
        return ans[left][right];
    }
};
```

2. dp

> 将自顶向下的记忆化搜索变为自底向上的动态规划，dp[i][j]表示填满开区间 (i,j)可以获得的硬币数  
> 注意如何遍历计算，从中间向两边拓展

```C++
class Solution {
public:
    int maxCoins(vector<int>& nums) {
        nums.insert(nums.begin(),1);
        nums.push_back(1);
        // 初始化必须为0
        vector<vector<int>> ans(nums.size(),vector<int>(nums.size(),0));
        for(int left=nums.size()-3;left>=0;--left){
            for(int right=left+2;right<nums.size();++right){
                for(int k=left+1;k<right;++k){
                    int sum=nums[left]*nums[k]*nums[right];
                    sum+=ans[left][k]+ans[k][right];
                    ans[left][right]=max(ans[left][right],sum);
                }
            }
        }
        return ans[0][nums.size()-1];
    }
};
```