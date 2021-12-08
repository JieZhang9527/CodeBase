1. DFS

> 时空复杂度较高

```C++
class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int S) {
        int ans=0;
        long long sum=0;
        DFS(nums,0,S,sum,ans);
        return ans;
    }
    void DFS(const vector<int> &nums,int index,int S,long long sum,int &ans){
        if(index==nums.size()){
            if(S==sum)  ++ans;
            return ;
        }
        DFS(nums,index+1,S,sum+nums[index],ans);
        DFS(nums,index+1,S,sum-nums[index],ans);
    }
};
```

2. 01背包问题

> 特征：求解和为target的组合个数，就是01背包。转换一下：设+的正数positive，-的负数为negative,数组和为sum  
> positive+negative=S  &  positive-negative=sum  $\rightarrow$ 2positive=sum+S

```C++
class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int S) {
        long sum=0;
        for(auto i : nums)  sum+=i;
        if((sum+S)%2||S>sum)  return 0;
        int target=(sum+S)/2;
        //dp[i]表示背包容量为i时的方法数
        vector<int> dp(target+1,0);
        //背包的容量为0时，什么都不取这种方法
        dp[0]=1;
        for(auto num : nums){
            for(int j=target;j>=num;--j)
            //dp[j]=dp[j]+dp[j-num]
            //表示选取num和不选取num的方法数只和
            dp[j]+=dp[j-num];
        }
        return dp[target];
    }
};
```