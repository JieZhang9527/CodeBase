1. BFS

```C++
class Solution {
public:
    vector<string> removeInvalidParentheses(string s) {
        vector<string> ans;
        // 不合法半括号个数，即需要删除的个数
        int left=0, right=0;
        for(auto c : s){
            if(c=='(')  ++left;
            else if(c==')'){
                if(left>0)  --left;
                else    ++right;
            }
        }
        BFS(s,left,right,ans);
        return ans;
    }
private:
    bool isValid(string &s){
        int count=0;
        for(auto c : s){
            if(c=='(')  ++count;
            else if(c==')')    --count;
            if(count<0) return false;
        }
        return count==0;
    }
    void BFS(string s, int left, int right, vector<string> &ans){
        if(s.empty())   return;
        queue<string> q;    q.push(s);
        unordered_set<string> visited;  visited.insert(s);
        bool flag=false;
        while(!q.empty()){
            int count=q.size();
            for(int i=0;i<count;++i){
                auto temp=q.front();
                q.pop();
                if(isValid(temp)){
                    ans.push_back(temp);
                    flag=true;
                }
                for(int j=0;j<temp.size();++j){
                    if(temp[j]!='('&&temp[j]!=')')  continue;
                    auto next=temp.substr(0,j)+temp.substr(j+1,temp.size()-j-1);
                    if(visited.find(next)==visited.end()){
                        q.push(next);
                        visited.insert(next);
                    }
                }
            }
            if(flag)    break;
        }
    }
};
```

2. DFS

```C++
class Solution {
public:
    vector<string> removeInvalidParentheses(string s) {
        vector<string> ans;
        // 不合法半括号个数，即需要删除的个数
        int left=0, right=0;
        for(auto c : s){
            if(c=='(')  ++left;
            else if(c==')'){
                if(left>0)  --left;
                else    ++right;
            }
        }
        DFS(s,0,left,right,ans);
        return ans;
    }
private:
    bool isValid(string &s){
        int count=0;
        for(auto c : s){
            if(c=='(')  ++count;
            else if(c==')')    --count;
            if(count<0) return false;
        }
        return count==0;
    }
    void DFS(string s, int start, int left, int right, vector<string> &ans){
        if(left==0&&right==0){
            if(isValid(s))  ans.push_back(s);
            return;
        }
        for(int i=start;i<s.size();++i){
            // 去除重复
            if(i>start&&s[i]==s[i-1])   continue;
            if(left>0&&s[i]=='(')   DFS(s.substr(0,i)+s.substr(i+1,s.size()-i-1),i,left-1,right,ans);
            if(right>0&&s[i]==')')  DFS(s.substr(0,i)+s.substr(i+1,s.size()-i-1),i,left,right-1,ans);
        }
    }
};
```