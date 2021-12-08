1. 水平扫描法
> 我们将一组字符串的公共前缀定义为LCP(S1,S2,...,Sn)，那么LCP(S1,S2,...,Sn)=LCP(LCP(LCP(S1,S2),S3),...Sn)

```C++
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if(strs.empty())    return string();
        string ans=strs[0];
        for(int i=1;i<strs.size();++i){
            while(strs[i].find(ans)!=0){
                if(ans.empty()) return ans;
                ans.pop_back();
            }
        }
        return ans;
    }
};
```

2. 水平扫描法优化
> 将上述两两之间的比较，变为竖列对比，这样可以在遇到短字符串时提前退出

```C++
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if(strs.empty())    return string();
        for(int i=0;i<strs[0].size();++i){
            for(int j=1;j<strs.size();++j){
                if(i==strs[j].size()||strs[0][i]!=strs[j][i])
                    return strs[0].substr(0,i);
            }
        }
        return strs[0];
    }   
};
```