1. 单调栈

> 维护单调不增栈，将栈中元素反转即是结果 

```C++
class Solution {
public:
    string removeDuplicateLetters(string s) {
        // 记录字符串中每个元素的数量
        vector<int> count(256,0);
        for(auto c : s) count[c]++;
        // 单调不增栈
        stack<int> st;
        // 记录栈中是否存在某个元素
        vector<bool> exist(256,false);
        for(int i=0;i<s.size();++i){
            count[s[i]]--;
            if(exist[s[i]]) continue;
            while(!st.empty()&&st.top()>s[i]){
                if(count[st.top()]==0)  break;
                exist[st.top()]=false;
                st.pop();
            }
            st.push(s[i]);
            exist[s[i]]=true;
        }
        string ans=string();
        while(!st.empty()){
            ans+=st.top();
            st.pop();
        }
        reverse(ans.begin(),ans.end());
        return ans;
    }
};
```