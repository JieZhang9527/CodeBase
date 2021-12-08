1. 递归

```C++
class Solution {
public:
    vector<int> lexicalOrder(int n) {
        vector<int> ans;
        help(-1,n,ans);
        return ans;
    }
private:
    void help(int curr, int n, vector<int> &ans){
        if(curr!=-1&&curr>n)    return;
        if(curr!=-1)    ans.push_back(curr);
        for(int num=0;num<=9;++num){
            if(curr==-1){
                if(num==0)  continue;
                else    curr=0;
            }
            help(curr*10+num,n,ans);
        }
    }
};
