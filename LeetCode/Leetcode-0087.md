1. 递归
> 超时

```C++
class Solution {
public:
    bool isScramble(string s1, string s2) {
        if(s1.size()!=s2.size())    return false;
        if(s1==s2)  return true;
        vector<int> count(128,0);
        for(int i=0;i<s1.size();++i){
            count[s1[i]]++;
            count[s2[i]]--;
        }
        for(auto num : count){
            if(num) return false;
        }
        for(int i=1;i<s1.size();++i){
            bool state1=isScramble(s1.substr(0,i),s2.substr(0,i));
            bool state2=isScramble(s1.substr(i),s2.substr(i));
            if(state1&&state2)  return true;
            bool state3=isScramble(s1.substr(0,i),s2.substr(s2.size()-i));
            bool state4=isScramble(s1.substr(i),s2.substr(0,s2.size()-i));
            if(state3&&state4)  return true;
        }        
        return false;
    }
};
```

1. dp
> 既然可以使用递归解决，可以将其改为动态规划  
> dp[len][i][j]表示s1[i,i+len) s2[j,j+len) 是否满足条件

```C++
class Solution {
public:
    bool isScramble(string s1, string s2) {
        if(s1.size()!=s2.size())    return false;
        if(s1==s2)  return true;
        vector<int> count(128,0);
        for(int i=0;i<s1.size();++i){
            count[s1[i]]++;
            count[s2[i]]--;
        }
        for(auto num : count){
            if(num) return false;
        }
        int len=s2.size();
    vector<vector<vector<bool>>>dp(len+1,vector<vector<bool>>(len,vector<bool>(len,false)));
        for(int l=1;l<=len;++l){
            for(int i=0;i+l<=len;++i){
                for(int j=0;j+l<=len;++j){
                    if(l==1)    dp[l][i][j]=(s1[i]==s2[j]);
                    else{
                        for(int q=1;q<l;++q){
                            bool state1=dp[q][i][j]&&dp[l-q][i+q][j+q];
                            bool state2=dp[q][i][j+l-q]&&dp[l-q][i+q][j];
                            dp[l][i][j]=state1||state2;
                            if(dp[l][i][j]) break;
                        }
                    }  
                }
            }
        }
        return dp[len][0][0];
    }
};
```