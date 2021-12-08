1. 栈
> 栈用于存储每一级的目录名  
> - 如果是上一级目录且栈不为空就出栈  
> - 如果获取一个目录名就入栈
```C++
class Solution {
public:
    string simplifyPath(string path) {
        stack<string> st;
        int index=0;
        while(index<path.size()){
            while(index<path.size()&&path[index]=='/')  ++index;
            string temp=string();
            while(index<path.size()&&path[index]!='/'){
                temp+=path[index];
                ++index;
            }
            if(temp==".")   continue;
            else if(temp==".."){
                if(!st.empty()) st.pop();
                else    continue;
            }
            // !!
            else if(!temp.empty())  st.push(temp);
        }
        string ans=string();
        stack<string> help;
        while(!st.empty()){
            help.push(st.top());
            st.pop();
        }
        while(!help.empty()){
            ans+='/';
            ans+=help.top();
            help.pop();
        
        }
        return ans.empty()?"/":ans;
    }
};
```