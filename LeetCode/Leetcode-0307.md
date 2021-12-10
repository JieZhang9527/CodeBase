1. 保存连续和

> 超时

```C++
class NumArray {
private:
    vector<int> dp;
public:
    NumArray(vector<int>& nums) {
        if(!nums.empty()){
            dp.push_back(nums[0]);
            for(int i=1;i<nums.size();++i)  dp.push_back(dp[i-1]+nums[i]);
        }
    }
    
    void update(int i, int val) {
        int difference;
        if(i==0)  difference=val-dp[i];
        else  difference=val-(dp[i]-dp[i-1]);
        for(int k=i;k<dp.size();++k)  dp[k]+=difference;
    }
    
    int sumRange(int i, int j) {
        int ans=0;
        if(i==0)  ans=dp[j];
        else ans=dp[j]-dp[i-1];
        return ans;
    }
};
```