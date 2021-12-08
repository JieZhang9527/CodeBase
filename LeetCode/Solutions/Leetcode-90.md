1. 回溯
> 排序是去重的前提

```C++
class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        vector<vector<int>> ans;
        vector<int> temp;
        backtrack(nums,0,temp,ans);
        return ans;
    }
private:
    void backtrack(vector<int> &nums, int index, vector<int> &temp, vector<vector<int>> &ans){
        ans.push_back(temp);
        for(int i=index;i<nums.size();++i){
            if(i>index&&nums[i]==nums[i-1]) continue;
            temp.push_back(nums[i]);
            backtrack(nums,i+1,temp,ans);
            temp.pop_back();
        }
    }
};
```

2. 循环添加
> 本题和78题思想相同，特别的是对于重复元素的处理，以nums=[1,2,2]为例：
> - {{}}
> - {{},{1}}
> - {{},{1},{2},{1,2}}
> - {{},{1},{2},{1,2},{2,2},{1,2,2}} 2和上一个元素重复，这时遍历的节点应是上上次结果的下一个节点{2}

```C++
class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        vector<vector<int>> ans={{}};
        int start=-1;
        for(int i=0;i<nums.size();++i){
            start=(i>0&&nums[i]==nums[i-1])?start:0;
            // 上一个状态的个数
            int count=ans.size();
            // 填充当前状态
            for(int j=start;j<count;++j){
                auto temp=ans[j];
                temp.push_back(nums[i]);
                ans.push_back(temp);
            }
            // 赋值上个状态的长度，下次遍历时就是上上次的长度
            start=count;
        }
        return ans;
    }
};
```