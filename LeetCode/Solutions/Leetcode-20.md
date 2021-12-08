1. 栈
> 针对有多种括号，可以将其映射为一个整数，从而判断是否为同一种括号对应

```C++
class Solution {
public:
    bool isValid(string s) {
        unordered_map<char,int> mp={{'(',1},{')',2},{'{',4},{'}',5},{'[',7},{']',8}};
        stack<int> st;
        for(auto c : s){
            if(!st.empty()&&mp[c]-st.top()==1)  st.pop();
            else    st.push(mp[c]);
        }
        return st.empty();
    }
};
```