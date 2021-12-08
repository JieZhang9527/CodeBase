1. 位运算
> 统计二进制下所有位中1的个数，如果出现次数大于数组长度的一半，则目标数字该位为1

```C++
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        vector<int> count(32,0);
        for(auto num : nums){
            for(int i=0;i<32;++i){
                count[i]+=num&1;
                num>>=1;
            }
        }
        int ans=0;
        for(int i=31;i>=0;--i){
            ans<<=1;
            if(count[i]>nums.size()/2)  ans|=1;
        }
        return ans;
    }
};
```

2. 摩尔投票法
> 求众数。寻找数组中出现次数超过一半的数字,这意味着其他数字出现次数的总和加起来都比不上这个数字，如果将众数计为+1,其他计为-1,和应该大于0

```C++
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int ans=nums[0], count=1;
        for(int i=1;i<nums.size();++i){
            if(count==0){
                ans=nums[i];
                count=1;
            }
            else if(nums[i]==ans)   ++count;
            else    --count;
        }
        return ans;
    }
};
```