1. 一次遍历

> 遍历每个元素，计算到此为止01数量之间的差值，如果当前的差值在之前出现过，那么这一段内的01数量相等

```C++
class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        unordered_map<int,int> ump;
        // !!!
        ump.insert({0,-1});
        int count=0,ans=0;
        for(int i=0;i<nums.size();++i){
            if(nums[i]==0)  --count;
            else  ++count;
            if(ump.find(count)==ump.end())
                ump.insert({count,i});
            else 
                ans=max(ans,i-ump[count]);
        }    
        return ans;
    }
};
```