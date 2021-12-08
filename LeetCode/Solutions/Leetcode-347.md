1. 暴力排序

> 使用lambda表达式排序

```C++
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> ans;
        unordered_map<int,int> ump;
        for(auto num : nums)    ump[num]++;
        sort(nums.begin(),nums.end(),[&ump](int &a, int &b){return ump[a]==ump[b]?a<b:ump[a]>ump[b];});
        for(int i=0;i<nums.size();++i){
            if(ans.empty()||nums[i]!=ans.back())
                ans.push_back(nums[i]);
            if(ans.size()==k)   break;
        }
        for(int i=0;i<nums.size();++i)  cout<<nums[i]<<" ";
        return ans;
    }
};
```