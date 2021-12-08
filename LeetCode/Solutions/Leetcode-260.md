1. 位运算

> 假设最终要求解的是 x y，异或运算消除出现偶数次的数字,则全体数字进行异或结果为 temp=x^y，异或运算是求解两个数之间的差异,因此 mask=temp & (-temp) 求解temp最低的非0位，要使得mask的该位为1,则要么来源于x 要么来源于y,因此可以用于分离两者，假设遍历数字该位为0,异或计算x,由此得出y。

```C++
class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        int temp=0; 
        for(auto num : nums)    temp ^= num;
        int mask=temp & (-temp);
        int ans=0;
        for(auto num : nums){
            if((mask&num)==0)    ans ^= num;
        }
        return {ans,ans^temp};
    }
};
```