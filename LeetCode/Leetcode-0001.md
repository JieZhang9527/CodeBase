1. 暴力解决
> 针对每一个元素，遍历是否存在另一元素使得和为target

```C++
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ans;
        for(int i=0;i<nums.size();++i){
            for(int j=i+1;j<nums.size();++j){
                if(nums[i]+nums[j]==target){
                    return {i,j};
                }
            }
        }
        return ans;
    }
};
```

2. 哈希法
> 以时间换空间，``unordered_map`` 记录当前还需要哪些数即可构成target

```C++
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ans;
        unordered_map<int,int> ump;
        for(int i=0;i<nums.size();++i){
            if(ump.find(nums[i])!=ump.end()){
                return {ump[nums[i]],i};
            }
            ump[target-nums[i]]=i;
        }
        return ans;
    }
};
```