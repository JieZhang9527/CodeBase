1. 哈希

> 假设sum[0……i]%k=a,sum[0……j]%k=b，如果a==b，那么i，j之间差了n个k,即构成连续子数组  

```C++
class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        unordered_map<int,int> ump;
        int sum=0;
        ump[0]=-1;  // 避免刚好整除的情况
        for(int i=0;i<nums.size();++i){
            sum+=nums[i];
            sum%=k;
            if(ump.find(sum)!=ump.end()){
                if(i-ump[sum]>1)    return true;
            }
            else ump[sum]=i;
        }
        return false;
    }
};
```