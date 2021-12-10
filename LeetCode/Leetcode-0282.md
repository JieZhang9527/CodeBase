1. 回溯

```C++
class Solution {
public:
    vector<string> addOperators(string num, int target) {
        vector<string> ans;
        help(num,target,string(),ans,0,0,0);
        return ans;
    }
private:
    void help(string num, int target, string path, vector<string> &ans, int start, long val,long pre){
        if(start==num.size()){
            if(val==target) ans.push_back(path);
            return;
        }
        for(int i=start;i<num.size();++i){
            // 数字不能以0开头
            if(num[start]=='0'&&i>start)    break;
            long curr=stol(num.substr(start,i+1-start));
            auto curr_word=to_string(curr);
            if(start==0)    help(num,target,path+curr_word,ans,i+1,curr,curr);
            else{
                // 加当前值
                help(num,target,path+"+"+curr_word,ans,i+1,val+curr,curr);
                // 减当前值
                help(num,target,path+"-"+curr_word,ans,i+1,val-curr,-curr);
                
                help(num,target,path+"*"+curr_word,ans,i+1,val-pre+pre*curr,pre*curr);
            }
        }
    }
};
```