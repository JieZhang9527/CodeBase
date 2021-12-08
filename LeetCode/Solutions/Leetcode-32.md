1. 栈
> 栈中每个元素记录的是字符串的索引值，为便于处理，栈中初始索引值为-1

```C++
class Solution {
public:
    int longestValidParentheses(string s) {
        if(s.empty())   return 0;
        int ans=0;
        stack<int> st;
        st.push(-1);
        for(int i=0;i<s.size();++i){
            if(s[i]=='(')   st.push(i);
            else{
                st.pop();
                if(st.empty())  st.push(i);
                else    ans=max(ans,i-st.top());
            }
        }
        return ans;
    }
};
```