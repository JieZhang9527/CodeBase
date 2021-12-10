1. 栈
> 类似于中序表达式求值

```C++
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        if(tokens.empty())  return 0;
        stack<string> st;
        for(auto &token :tokens){
            if(token!="+"&&token!="-"&&token!="*"&&token!="/"){
                st.push(token);
                continue;
            }
            int right=stoi(st.top());
            st.pop();
            int left=stoi(st.top());
            st.pop();
            int val=left;
            if(token=="+")  val+=right;
            else if(token=="-") val-=right;
            else if(token=="*") val*=right;
            else if(token=="/") val/=right;
            st.push(to_string(val));
        }
        return stoi(st.top());
    }
};
```