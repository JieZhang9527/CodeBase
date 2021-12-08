> 三个数分别记录当前遍历到的第一大第二大和第三大数

```C++
class Solution {
public:
    int thirdMax(vector<int>& nums) {
        long top1=nums[0], top2=LONG_MIN, top3=LONG_MIN;
        for(int i=1;i<nums.size();++i){
            if(nums[i]==top1||nums[i]==top2||nums[i]==top3) continue;
            if(nums[i]>top1){
                top3=top2;
                top2=top1;
                top1=nums[i];
            }
            else if(nums[i]>top2){
                top3=top2;
                top2=nums[i];
            }
            else if(nums[i]>top3)   top3=nums[i];
        }
        return top3==LONG_MIN?top1:top3;
    }
};
```
