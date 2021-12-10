1. dp
> dp[i]表示前i个单词是否能构成词典里的一句话，然后进行回溯，但是是从尾向头部回溯

```C++
class Solution {
public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> ust;
        for(auto word : wordDict)   ust.insert(word);
        vector<bool> dp(s.size()+1,false);
        dp[0]=true;
        for(int right=1;right<=s.size();++right){
            for(int left=right-1;left>=0;--left){
                if(ust.find(s.substr(left,right-left))!=ust.end()&&dp[left]){
                    dp[right]=true;
                    break;
                }
            }
        }
        vector<string> ans;
        if(dp.back()){
            vector<string> path;
            DFS(s,s.size(),ust,dp,path,ans);
            return ans;
        }
        return ans;
    }
private:
    string help(vector<string> &path){
        string ans=string();
        for(int i=0;i<path.size()-1;++i)    ans+=path[i]+" ";
        ans+=path.back();
        return ans;
    }
    void DFS(string &s, int len, unordered_set<string> &ust, vector<bool> &dp, vector<string> &path, vector<string> &ans){
        if(len==0){
            ans.push_back(help(path));
            return;
        }
        for(int i=len-1;i>=0;--i){
            string temp=s.substr(i,len-i);
            if(ust.find(temp)!=ust.end()&&dp[i]){
                path.insert(path.begin(),temp);
                DFS(s,i,ust,dp,path,ans);
                path.erase(path.begin());
            }
        }
    }
};
```