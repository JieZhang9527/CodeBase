1. 原地哈希

> 空间复杂度为O(N)  
> 抽屉原理：一个萝卜一个坑。将萝卜放在自己的坑里，剩下不匹配的或是多的就是。第一个for循环，将萝卜放在自己的坑里，第二个for循环，寻找不匹配的萝卜。

```C++
class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        vector<int> ans;
        for(int i=0;i<nums.size();++i){
            while(nums[i]!=nums[nums[i]-1])
                swap(nums[i],nums[nums[i]-1]);
        }
        for(int i=0;i<nums.size();++i){
            if(nums[i]-1!=i)
                ans.push_back(nums[i]);
        }
        return ans;
    }
};
```