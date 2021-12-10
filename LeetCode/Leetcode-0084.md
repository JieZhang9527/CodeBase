1. 单调栈
> 栈中的元素为元素的索引值，保持对应值单调不减  
> 为了便于处理头和尾，可以在两端分别添加0值

```C++
class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        if(heights.empty()) return 0;
        heights.push_back(0);
        stack<int> st;
        st.push(0);
        int ans=0;
        for(int i=0;i<heights.size();++i){
            while(!st.empty()&&heights[st.top()]>heights[i]){
                int height=heights[st.top()];
                st.pop();
                int width=st.empty()?i:i-st.top()-1;
                ans=max(ans,height*width);
            }
            st.push(i);
        }
        return ans;
    }
};
```