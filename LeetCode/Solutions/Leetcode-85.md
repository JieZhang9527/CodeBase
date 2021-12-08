1. 单调栈
> 和84题思路相同

```C++
class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        if(matrix.empty()||matrix[0].empty())   return 0;
        int rows=matrix.size(), cols=matrix[0].size();
        vector<int> heights(cols,0);
        int ans=0;
        for(int i=0;i<rows;++i){
            for(int j=0;j<cols;++j){
                if(matrix[i][j]=='0')   heights[j]=0;
                else    heights[j]++;
            }
            ans=max(ans,help(heights));
        }
        return ans;
    }
private:
    int help(vector<int> &heights){
        if(heights.empty()) return 0;
        heights.push_back(0);
        stack<int> st;
        st.push(0);
        int ans=0;
        for(int i=0;i<heights.size();++i){
            while(!st.empty()&&heights[i]<heights[st.top()]){
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