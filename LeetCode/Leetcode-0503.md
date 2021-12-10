1. 单调栈

> 数组是一个循环数组，元素的下一个更大元素可能出现在左面，将原始数组翻倍就可以使其出现在右面。因为是寻找下一个更大元素，所以我们从右向左遍历，维持一个单调栈，栈中的元素从小到大，对于当前索引i的元素，栈中的元素是其右边元素从小到大。

```C++
class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        int len=nums.size();
        vector<int> ans(len,0);
        stack<int> st;
        for(int i=2*len-1;i>=0;--i){
            while(!st.empty()&&nums[i%len]>=st.top())   st.pop();
            ans[i%len]=st.empty()?-1:st.top();
            st.push(nums[i%len]);   
        } 
        return ans;
    }
};
```