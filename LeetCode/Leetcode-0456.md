1. 栈

> 从右向左遍历可以使得栈中存储的是元素右边的值

```C++
class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        if(nums.size()<3)  return false;
        // left_min[i]记录nums[0,i]的最小值
        vector<int> left_min(nums.size(),0);
        left_min[0]=nums[0];
        for(int i=1;i<nums.size();++i)  left_min[i]=min(left_min[i-1],nums[i]);
        // st中存储的是索引为K的值
        stack<int> st;
        for(int i=nums.size()-1;i>=0;--i){
            if(nums[i]>left_min[i]){
                while(!st.empty()&&st.top()<=left_min[i])   st.pop();
                if(!st.empty()&&nums[i]>st.top())   return true;
                st.push(nums[i]);
            }
        }
        return false;
    }
};
```