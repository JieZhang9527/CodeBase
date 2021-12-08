1. 遍历
> 注意i和j的值范围

```C++
class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> ans;
        if(numRows==0)  return ans;
        ans.push_back({1});
        for(int i=1;i<numRows;++i){
            vector<int> nums={1};
            for(int j=1;j<i;++j){
                nums.push_back(ans.back()[j-1]+ans.back()[j]);
            }
            nums.push_back(1);
            ans.push_back(nums);
        }
        return ans;
    }
};
```