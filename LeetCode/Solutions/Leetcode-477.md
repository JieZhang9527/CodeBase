1. 位运算

> 假设二进制的某一位 有x个0,y个1,且有x+y=nums.size(),则该位所有汉明距离的为 x*y

```C++
class Solution {
public:
    int totalHammingDistance(vector<int>& nums) {
        int count[32]={};
        for(auto num : nums){
            int i=0;
            while(num>0){
                count[i] += num  & 1;
                num >>= 1;
                ++i; 
            }
        }
        int ans=0;
        for(auto cnt : count)   ans+=cnt*(nums.size()-cnt);
        return ans;
    }
};
```