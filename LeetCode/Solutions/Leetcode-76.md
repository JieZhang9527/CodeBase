1. 滑动窗口
> left和right分别表示窗口的左右边界

```C++
class Solution {
public:
    string minWindow(string s, string t) {
        if(s.empty()||t.empty())    return string();
        // 记录每个字符需要的个数
        vector<int> need(128,0);
        for(auto c : t) need[c]++;
        // len窗口大小，start目标串起始索引，count需要的字符个数
        int len=INT_MAX, count=t.size(), start=0;
        int left=0, right=0;
        while(right<s.size()){
            char c=s[right];
            if(need[c]>0)   --count;
            --need[c];
            if(count==0){
                // 从左侧删减不必要的字符
                while(left<right&&need[s[left]]<0){
                    need[s[left]]++;
                    ++left;
                }
                if(right-left+1<len){
                    len=right-left+1;
                    start=left;
                }
                // ++left，使得当前窗口不满足条件
                need[s[left]]++;
                ++count;
                ++left;
            }
            ++right;
        }
        return len==INT_MAX?string():s.substr(start,len);
    }
};
```