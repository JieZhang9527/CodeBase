1. 回溯
> 超时。对于每个节点，跳跃到所能达到的节点，如果没有到达最后一个节点，就继续回溯

```C++
class Solution {
public:
    bool canJump(vector<int>& nums) {
        if(nums.empty()||nums.size()==1)    return true;
        return backtrack(nums,0);
    }
private:
    bool backtrack(vector<int> &nums, int curr){
        if(curr==nums.size()-1) return true;
        int farthest=min(curr+nums[curr],(int)nums.size()-1);
        for(int i=curr+1;i<=farthest;++i){
            if(backtrack(nums,i))   return true;
        }
        return false;
    }
};
```

2. 基于回溯的优化/自顶向下的动态规划
> 原始的回溯包含很多重复计算：不同节点可能跳到相同的节点，重复回溯  
> 空间换时间，用一个含有三个状态的数组记录某个节点是否可以达到终点（依然超时):
> - 1表示可到达
> - 0表示不知道
> - -1表示不可达  

```C++
class Solution {
public:
    bool canJump(vector<int>& nums) {
        if(nums.empty()||nums.size()==1)    return true;
        vector<int> status(nums.size(),0);
        return backtrack(nums,0,status);
    }
private:
    bool backtrack(vector<int> &nums, int curr, vector<int> &status){
        if(curr==nums.size()-1) return true;
        int farthest=min(curr+nums[curr],(int)nums.size()-1);
        for(int i=curr+1;i<=farthest;++i){
            if(status[i]==1)    return true;
            if(backtrack(nums,i,status)){
                status[i]=1;
                return true;
            }
        }
        status[curr]=-1;
        return false;
    }
};
```

3. 自底向上的动态规划
> 如果从目标往前跳跃就消除了回溯，因为右边的值都已经记录

```C++
class Solution {
public:
    bool canJump(vector<int>& nums) {
        if(nums.empty()||nums.size()==1)    return true;
        vector<bool> dp(nums.size(),false);
        dp.back()=true;
        for(int i=dp.size()-2;i>=0;--i){
            int farthest=min(nums[i]+i,(int)nums.size()-1);
            for(int j=i+1;j<=farthest;++j){
                if(dp[j]){
                    dp[i]=true;
                    break;
                }
            }
        }
        return dp[0];
    }
};
```
4. 贪心算法

```C++
class Solution {
public:
    bool canJump(vector<int>& nums) {
        int target=nums.size()-1;
        for(int i=target-1;i>=0;--i){
            if(i+nums[i]>=target)   target=i;
        }
        return target==0;
    }
};
```