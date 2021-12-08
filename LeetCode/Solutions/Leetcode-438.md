1. 滑动窗口

> 两个数组分别记录当前窗口内每个元素的数量和模式串每个元素的数量

```C++
class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        vector<int> ans;
        if(s.size()<p.size())   return ans;
        vector<int> count_p(128,0), count_s(128,0);
        for(auto c : p) count_p[c]++;
        for(int left=0, right=0; right<s.size();++right){
            count_s[s[right]]++;
            while(count_s[s[right]]>count_p[s[right]]){
                count_s[s[left]]--;
                ++left;
            }
            if(right-left+1==p.size())  ans.push_back(left);
        }
        return ans;
    }
};
```