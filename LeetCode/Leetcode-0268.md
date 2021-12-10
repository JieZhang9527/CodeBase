1. 位运算

> 异或运算的特性：  
> 一个数与另一个数异或两次是其本身((a^b)^b)=a  
> 一个数与自身异或等于0  (a^a)=0  
> 一个数与0异或等于自身  (a^0)=a

```C++
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int ans=0;
        for(int i=0;i<=nums.size();++i)   ans ^=i;
        for(auto num : nums)    ans ^=num;
        return ans;
    }
};
```