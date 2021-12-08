1. 滑动窗口
> [left,right)表示当前窗口的范围，是一个左闭右开区间，因此长度计算为right-left

```C++
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if(s.empty())   return 0;
        int ans=1;
        int left=0, right=0;
        vector<bool> record(128,false);
        while(left<=right&&right<s.size()){
            if(!record[s[right]]){
                record[s[right]]=true;
                ++right;
            }
            else{
                record[s[left]]=false;
                ++left;
            }
            ans=max(ans,right-left);
        }
        return ans;
    }
};
```